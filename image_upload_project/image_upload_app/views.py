from rest_framework import viewsets
from django.shortcuts import redirect, render
from .models import Image, Plan, ThumbnailSize
from .serializers import ImageSerializer, PlanSerializer, ThumbnailSizeSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class ThumbnailSizeViewSet(viewsets.ModelViewSet):
    queryset = ThumbnailSize.objects.all()
    serializer_class = ThumbnailSizeSerializer
