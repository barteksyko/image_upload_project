from django.db import models


class Image(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
    thumbnail_200 = models.ImageField(
        upload_to="thumbnails/200/", null=True, blank=True
    )
    thumbnail_400 = models.ImageField(
        upload_to="thumbnails/400/", null=True, blank=True
    )
    original_image = models.ImageField(upload_to="originals/", null=True, blank=True)
    expiring_link = models.URLField(null=True, blank=True)


class Plan(models.Model):
    name = models.CharField(max_length=100)
    thumbnail_sizes = models.ManyToManyField("ThumbnailSize")
    include_original_link = models.BooleanField(default=False)
    generate_expiring_link = models.BooleanField(default=False)


class ThumbnailSize(models.Model):
    size = models.IntegerField()
