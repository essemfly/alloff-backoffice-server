from datetime import datetime

from rest_framework import serializers, status
from rest_framework.request import Request
from rest_framework.response import Response
from tagger.core.mongo.models.order import Order, Refund
from tagger.serializers.refund import RefundSerializer


class UpdateRefundSerializer(serializers.Serializer):
    refund_amount = serializers.IntegerField(min_value=0)  # refundamount
    refund_delivery_price = serializers.IntegerField(min_value=0)  # refunddeliveryprice
    refund_price = serializers.IntegerField(min_value=0)  # refundprice

    def validate(self, attrs):
        order = self.instance  # type: Order
        refund_fee = attrs.get("refund_price") + attrs.get("refund_delivery_price")

        if refund_fee + attrs.get("refund_amount") != order.totalprice:
            raise serializers.ValidationError(
                "Refund amount and fee does not match (order total: {}, fee + amount: {})".format(
                    order.totalprice, refund_fee + attrs.get("refund_amount")
                )
            )

        return super().validate(attrs)


def update_refund(self, request: Request, id=None):
    serializer = self.get_serializer(data=request.data, instance=self.get_object())
    serializer.is_valid(raise_exception=True)

    query = Refund.objects.filter(orderid=id)
    if len(query) == 0:
        refund = Refund.objects.create(
            orderid=id,
            refunddeliveryprice=serializer.validated_data.get("refund_delivery_price"),
            refundprice=serializer.validated_data.get("refund_price"),
            refundamount=serializer.validated_data.get("refund_amount"),
            created=datetime.now(),
            updated=datetime.now(),
        )
    else:
        refund = query.first()  # type: Refund
        refund.refunddeliveryprice = serializer.validated_data.get(
            "refund_delivery_price"
        )
        refund.refundprice = serializer.validated_data.get("refund_price")
        refund.refundamount = serializer.validated_data.get("refund_amount")
        refund.updated = datetime.now()
        refund.save()

    return Response(RefundSerializer(refund).data, status=status.HTTP_200_OK)
