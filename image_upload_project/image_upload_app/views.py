from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import parser_classes
from .models import Image, Plan, ThumbnailSize
from .serializers import ImageSerializer, PlanSerializer, ThumbnailSizeSerializer
from django.core.signing import TimestampSigner
from django.contrib.auth.models import User
from PIL import Image as PILImage


def generate_thumbnail(original_image, size):
    thumbnail = original_image.copy()
    thumbnail.thumbnail((size, size), PILImage.ANTIALIAS)
    return thumbnail


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    @action(detail=True, methods=["get"])
    def expiring_link(self, request, pk=None):
        image = self.get_object()
        expiration_time = int(request.query_params.get("expiration_time", 300))
        signer = TimestampSigner()
        expiring_link = signer.sign_object(
            {"image_id": image.id, "expiration_time": expiration_time}
        )
        return Response({"expiring_link": expiring_link})

    def create(self, request, *args, **kwargs):
        uploaded_image = request.data.get("image")
        if hasattr(request.user, "plan"):
            image = Image(user=request.user, image=uploaded_image)
            plan = request.user.plan
            thumbnail_sizes = plan.thumbnail_sizes.all()

            thumbnail_links = {
                "thumbnail_200": image.thumbnail_200.url,
                "thumbnail_400": image.thumbnail_400.url
                if thumbnail_sizes.filter(size=400).exists()
                else None,
                "original_image": image.original_image.url
                if plan.include_original_link
                else None,
            }
            return Response({"image_id": image.id, "thumbnail_links": thumbnail_links})
        else:
            return Response({"error": "User does not have a plan."})

    @parser_classes((MultiPartParser, FormParser))
    def perform_create(self, request):
        uploaded_image = request.data.get("image")
        image = Image(user=request.user, image=uploaded_image)
        image.thumbnail_200 = generate_thumbnail(uploaded_image, size=200)
        image.thumbnail_400 = generate_thumbnail(uploaded_image, size=400)
        image.original_image = uploaded_image
        image.save()
        return image


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

    @action(detail=True, methods=["put"])
    def set_plan(self, request, pk=None):
        user = self.get_object()
        plan_id = request.data.get("plan_id")

        try:
            plan = Plan.objects.get(id=plan_id)
            user.plan = plan
            user.save()
            return Response({"message": "Plan set successfully."})
        except Plan.DoesNotExist:
            return Response({"error": "Plan not found."})


class ThumbnailSizeViewSet(viewsets.ModelViewSet):
    queryset = ThumbnailSize.objects.all()
    serializer_class = ThumbnailSizeSerializer
