from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets
from tagger.core.drf.search_filter import CustomSearchFilter
from tagger.core.mongo.models.alloff_product import AlloffProduct
from tagger.core.mongo.models.alloff_product_group import AlloffProductGroup
from tagger.serializers.timedeal import TimedealSerializer
from tagger.serializers.timedeal_product import TimedealProductSerializer


class TimedealViewSet(viewsets.ModelViewSet):
    queryset = AlloffProductGroup.objects().order_by("-id")
    filter_backends = [CustomSearchFilter]
    search_fields = [
        "title",
        "shorttitle"
    ]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if action == 'products':
            return TimedealProductSerializer
        return TimedealSerializer

    @extend_schema(responses=TimedealProductSerializer(many=True))
    @action(methods=["GET"], detail=True, pagination_class=None)
    def products(self, request: Request, id=None):
        products = AlloffProduct.objects(productgroupid=id, removed=False).order_by('-created').all()
        serializer = TimedealProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request: Request, id=None):
        timedeal = self.get_object()  # type: AlloffProductGroup
        timedeal.hidden = True
        timedeal.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
