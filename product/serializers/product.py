from rest_framework import serializers
from django_grpc_framework import proto_serializers
from protos.product.product_pb2 import ProductMessage


class ProductSerializer(proto_serializers.ProtoSerializer):
    alloff_name = serializers.CharField()
    product_id = serializers.CharField()
    brand_kor_name = serializers.CharField()
    category_name = serializers.CharField()
    alloff_category_name = serializers.CharField()
    is_foreign_delivery = serializers.BooleanField()
    is_refund_possible = serializers.BooleanField()
    is_removed = serializers.BooleanField()
    is_soldout = serializers.BooleanField()
    original_price = serializers.IntegerField()
    discounted_price = serializers.IntegerField()
    special_price = serializers.IntegerField()
    earliest_delivery_days = serializers.IntegerField()
    latest_delivery_days = serializers.IntegerField()
    refund_fee = serializers.IntegerField()
    total_score = serializers.IntegerField()

    class Meta:
        proto_class = ProductMessage
