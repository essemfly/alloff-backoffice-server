from rest_framework import serializers

from tagger.models.order_memo import OrderMemo
from tagger.serializers.admin import AdminSerializer


class OrderMemoSerializer(serializers.ModelSerializer):
    admin = AdminSerializer()

    class Meta:
        model = OrderMemo
        fields = "__all__"
