from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from test_app.views import TestView

router = DefaultRouter()
router.register("", TestView, basename="root")

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
]
