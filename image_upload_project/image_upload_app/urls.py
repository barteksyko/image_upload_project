from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r"images", views.ImageViewSet)
router.register(r"plans", views.PlanViewSet)
router.register(r"thumbnail_sizes", views.ThumbnailSizeViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
