from django_grpc_framework import proto_serializers
from drf_spectacular.utils import extend_schema_field
from gen.pyalloff import product_inquiry_pb2, product_inquiry_reply_pb2
from gen.pyalloff.product_pb2 import GetProductRequest
from office.serializers.pagination import PaginationSerializer
from office.serializers.user_recorded_model import WithUserSerializer
from product.serializers.product import ProductSerializer
from product.services.product import ProductService
from rest_framework import fields


class ProductInquiryReplySerializer(WithUserSerializer):
    id = fields.IntegerField()
    body = fields.CharField(allow_null=False)
    created_at = fields.DateTimeField()
    deleted_at = fields.DateTimeField(allow_null=True)

    class Meta:
        proto_class = product_inquiry_reply_pb2.ProductInquiryReply


class ProductInquirySerializer(proto_serializers.ProtoSerializer):
    id = fields.IntegerField()

    # 현재는 DB에 저장하지 않고, 서버에서 고정값 내려줌
    title = fields.SerializerMethodField()

    def get_title(self, obj):
        return "상품 문의"

    product_id = fields.CharField(allow_null=False)
    brand_keyname = fields.CharField(allow_null=False)
    company_keyname = fields.CharField(allow_null=False)

    user_id = fields.CharField(allow_null=False)
    user_name = fields.CharField(allow_null=False)
    body = fields.CharField(allow_null=False)

    is_pending = fields.BooleanField(allow_null=False)

    created_at = fields.DateTimeField()
    deleted_at = fields.DateTimeField(allow_null=True)

    replies = ProductInquiryReplySerializer(many=True)

    product = fields.SerializerMethodField()

    @extend_schema_field(ProductSerializer)
    def get_product(self, obj):
        req = GetProductRequest(alloff_product_id=obj.product_id)
        pd = ProductService.get(req)
        serializer = ProductSerializer(pd)
        return serializer.data

    class Meta:
        proto_class = product_inquiry_pb2.ProductInquiry


class PaginatedProductInquirySerializer(PaginationSerializer):
    results = ProductInquirySerializer(many=True)
