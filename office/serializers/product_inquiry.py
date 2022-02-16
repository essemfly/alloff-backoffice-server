from django_grpc_framework import proto_serializers
from office.serializers.pagination import PaginationSerializer
from office.serializers.user_recorded_model import WithUserSerializer
from protos.order.product_inquiry import product_inquiry_pb2
from protos.order.product_inquiry_reply import product_inquiry_reply_pb2
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
    class Meta:
        proto_class = product_inquiry_pb2.ProductInquiry

class PaginatedProductInquirySerializer(PaginationSerializer):
    results = ProductInquirySerializer(many=True)
