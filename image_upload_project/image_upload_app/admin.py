from django.contrib import admin
from . import models
from django.contrib.admin import ModelAdmin


admin.site.register(models.Image, ModelAdmin)
admin.site.register(models.Plan, ModelAdmin)
admin.site.register(models.ThumbnailSize, ModelAdmin)
