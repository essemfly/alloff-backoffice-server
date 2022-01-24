from rest_framework import serializers, status
from rest_framework.request import Request
from rest_framework.response import Response

from tagger.core.mongo.models.order import Order
from tagger.models.inventory import ProductType
from tagger.viewsets.received_items import make_ri


class RemakeRiSerializer(serializers.Serializer):
    product_type = serializers.ChoiceField(ProductType.choices, required=True)
    product_id = serializers.CharField(required=True)


def remake_ri(self, request: Request, id: str = None):
    order = Order.get(id)
    serializer = self.get_serializer(data=request.data)  # type: RemakeRiSerializer
    serializer.is_valid(raise_exception=True)
    product_type = serializer.validated_data.get("product_type")
    product_id = serializer.validated_data.get("product_id")

    make_ri(order, True, product_type, product_id)[0]
    return Response({"result": "ok"}, status=status.HTTP_200_OK)
