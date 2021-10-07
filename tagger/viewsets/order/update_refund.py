from datetime import datetime

from rest_framework import serializers, status
from rest_framework.request import Request
from rest_framework.response import Response
from tagger.core.mongo.models.order import Order, Refund
from tagger.models.order_action_log import (
    OrderActionLog,
    OrderActionType,
    OrderRefundUpdateLog,
)
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

    refund_delivery_price = serializer.validated_data.get("refund_delivery_price")
    refund_price = serializer.validated_data.get("refund_price")
    refund_amount = serializer.validated_data.get("refund_amount")

    if len(query) == 0:
        refund = Refund.objects.create(
            orderid=id,
            refunddeliveryprice=refund_delivery_price,
            refundprice=refund_price,
            refundamount=refund_amount,
            created=datetime.now(),
            updated=datetime.now(),
        )
    else:
        refund = query.first()  # type: Refund
        refund.refunddeliveryprice = refund_delivery_price
        refund.refundprice = refund_price
        refund.refundamount = refund_amount
        refund.updated = datetime.now()
        refund.save()

    # Log
    log = OrderActionLog.objects.create(
        order_id=id,
        admin=request.user,
        action_type=OrderActionType.REFUND_UPDATE,
        detail=str(refund.refundamount),
    )

    OrderRefundUpdateLog.objects.create(
        order_id=id,
        action_log=log,
        refund_delivery_price=refund_delivery_price,
        refund_price=refund_price,
        refund_amount=refund_amount,
    )

    return Response(RefundSerializer(refund).data, status=status.HTTP_200_OK)
