from rest_framework import serializers
from .models import Image, Plan, ThumbnailSize


class ThumbnailSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThumbnailSize
        fields = ("size",)


class PlanSerializer(serializers.ModelSerializer):
    thumbnail_sizes = ThumbnailSizeSerializer(many=True)

    class Meta:
        model = Plan
        fields = (
            "id",
            "name",
            "thumbnail_sizes",
            "include_original_link",
            "generate_expiring_link",
        )


class ImageSerializer(serializers.ModelSerializer):
    thumbnail_200 = serializers.SerializerMethodField()
    thumbnail_400 = serializers.SerializerMethodField()
    expiring_link = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = (
            "id",
            "image",
            "thumbnail_200",
            "thumbnail_400",
            "original_image",
            "expiring_link",
        )
