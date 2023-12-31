from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
    thumbnail_200 = models.ImageField(
        upload_to="thumbnails/200/", null=True, blank=True
    )
    thumbnail_400 = models.ImageField(
        upload_to="thumbnails/400/", null=True, blank=True
    )
    original_image = models.ImageField(upload_to="originals/", null=True, blank=True)
    expiring_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"Image {self.id}"


class ThumbnailSize(models.Model):
    size = models.IntegerField()

    def __str__(self):
        return f"Thumbnail Size: {self.size}"


class Plan(models.Model):
    BASIC = "BASIC"
    PREMIUM = "PREMIUM"
    ENTERPRISE = "ENTERPRISE"

    LEVEL_CHOICES = [
        (BASIC, "Basic"),
        (PREMIUM, "Premium"),
        (ENTERPRISE, "Enterprise"),
    ]

    name = models.CharField(max_length=100)
    thumbnail_sizes = models.ManyToManyField(ThumbnailSize)
    include_original_link = models.BooleanField(default=False)
    generate_expiring_link = models.BooleanField(default=False)
    level = models.CharField(choices=LEVEL_CHOICES, max_length=20)

    def __str__(self):
        return self.name
