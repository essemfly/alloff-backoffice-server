from datetime import datetime

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets

from tagger.core.drf.search_filter import CustomSearchFilter
from tagger.core.mongo.models.alloff_product import AlloffProduct
from tagger.serializers.timedeal_product import TimedealProductSerializer


class TimedealProductViewSet(viewsets.ModelViewSet):
    queryset = AlloffProduct.objects(removed=False).order_by("-id")
    filter_backends = [CustomSearchFilter]
    search_fields = [
        "brand__korname",
        "name"
    ]
    permission_classes = [IsAuthenticated]
    serializer_class = TimedealProductSerializer

    def destroy(self, request: Request, id=None):
        product = self.get_object()  # type: AlloffProduct
        product.removed = True
        product.updated = datetime.utcnow()
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
