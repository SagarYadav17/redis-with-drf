from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework.viewsets import ModelViewSet

from test_app.models import TestModel
from test_app.serializers import TestSerializer


class TestView(ModelViewSet):
    serializer_class = TestSerializer
    queryset = TestModel.objects.all()

    http_method_names = ["get", "post", "patch", "delete"]

    @method_decorator(cache_page(60, key_prefix="test-view"))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
