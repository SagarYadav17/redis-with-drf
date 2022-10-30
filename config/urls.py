from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from core.views import CityView

router = DefaultRouter()
router.register("", CityView, basename="root")

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
]
