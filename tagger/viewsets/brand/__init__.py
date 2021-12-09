from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_mongoengine import viewsets

from tagger.core.mongo.models.brand import Brand
from tagger.serializers.brand import BrandSerializer


class BrandViewSet(
    viewsets.ModelViewSet
):
    queryset = Brand.objects().order_by("-created")
    permission_classes = [IsAuthenticated]
    serializer_class = BrandSerializer
    pagination_class = None

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)