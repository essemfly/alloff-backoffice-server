from datetime import datetime

from django.core.files.storage import default_storage
from django.http import request
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view
from office.serializers.shipping_candidate import (
    ShippingCandidateProtoSerializer,
    ShippingCandidateSubmitItemProtoSerializer,
)
from office.serializers.shipping_notice import (
    PaginatedShippingNoticeSerializer,
    ShippingNoticeListSerializer,
    ShippingNoticeRetrieveSerializer,
    ShippingNoticeStatus,
)
from office.serializers.shipping_notice_item import ShippingNoticeItemRemovalType
from office.services.shipping_notice import ShippingNoticeService
from office.utils.openapi import PROTO_PAGINATION_QUERY_PARAMS
from office.viewsets.pagination import PaginationListMixin
from office.viewsets.shipping_notice.make_upload_template import make_cj_workbook
from office.viewsets.shipping_notice.print_package_labels import print_package_labels
from rest_framework import fields, serializers, status, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response


class ShippingNoticeRemoveItemSerializer(serializers.Serializer):
    item_id = fields.IntegerField()
    removal_type = fields.ChoiceField(ShippingNoticeItemRemovalType.choices)


class ShippingNoticeMoveItemSerializer(serializers.Serializer):
    item_id = fields.IntegerField()
    source_id = fields.IntegerField()
    target_id = fields.IntegerField()


@extend_schema_view(
    list=extend_schema(
        parameters=PROTO_PAGINATION_QUERY_PARAMS
        + [
            OpenApiParameter(
                "statuses",
                {
                    "type": "array",
                    "items": {"type": "string", "enum": ShippingNoticeStatus.values},
                },
                OpenApiParameter.QUERY,
                explode=True,
            ),
            OpenApiParameter("code", OpenApiTypes.STR, OpenApiParameter.QUERY),
        ],
    ),
    retrieve=extend_schema(
        parameters=[OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)],
        responses=ShippingNoticeRetrieveSerializer,
    ),
)
class ShippingNoticeViewSet(PaginationListMixin, viewsets.ViewSet):
    def get_serializer_class(self):
        if self.action == "list":
            return PaginatedShippingNoticeSerializer
        elif self.action == "retrieve":
            return ShippingNoticeRetrieveSerializer
        elif self.action == "get_candidates":
            return ShippingCandidateProtoSerializer(many=True)
        return ShippingNoticeListSerializer

    def retrieve(self, request: Request, pk=None):
        response = ShippingNoticeService.retrieve(int(pk))
        serializer = ShippingNoticeRetrieveSerializer(response)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def list(self, request: Request, *args, **kwargs):
        list_response = ShippingNoticeService.list(
            **self.get_pagination_params(request),
            statuses=request.query_params.getlist("statuses"),
        )
        serializer = PaginatedShippingNoticeSerializer(list_response)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        responses=ShippingCandidateProtoSerializer(many=True),
        request=None,
    )
    @action(detail=False, methods=["get"])
    def get_candidates(self, request: Request):
        service = ShippingNoticeService()
        candidates = service.get_candidates()
        return Response(
            ShippingCandidateProtoSerializer(candidates, many=True).data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        responses=ShippingNoticeListSerializer,
        request=ShippingCandidateSubmitItemProtoSerializer(many=True),
    )
    @action(detail=False, methods=["post"])
    def make_shipping_notice_with_candidates(self, request: Request):
        serializer = ShippingCandidateSubmitItemProtoSerializer(
            data=request.data, many=True
        )
        serializer.is_valid(raise_exception=True)
        service = ShippingNoticeService()
        return Response(
            ShippingNoticeListSerializer(
                service.submit_candidates(serializer.validated_data), many=True
            ).data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        responses=ShippingNoticeRetrieveSerializer,
        request=ShippingNoticeRemoveItemSerializer,
        parameters=[OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)],
    )
    @action(detail=True, methods=["POST"])
    def remove_item(self, request: Request, pk=None):
        serializer = ShippingNoticeRemoveItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = ShippingNoticeService()
        notice = service.remove_item(
            int(pk),
            serializer.validated_data.get("item_id"),
            serializer.validated_data.get("removal_type"),
        )
        return Response(
            ShippingNoticeRetrieveSerializer(notice).data, status=status.HTTP_200_OK
        )

    @extend_schema(
        responses=ShippingNoticeRetrieveSerializer,
        request=ShippingNoticeMoveItemSerializer,
        parameters=[OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)],
    )
    def move_item(self, request: Request, pk=None):
        service = ShippingNoticeService()
        serializer = ShippingNoticeMoveItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        notice = service.move_item(
            int(pk),
            serializer.validated_data.get("item_id"),
            serializer.validated_data.get("source_id"),
            serializer.validated_data.get("target_id"),
        )
        return Response(
            ShippingNoticeRetrieveSerializer(notice).data, status=status.HTTP_200_OK
        )

    @extend_schema(
        request=None,
        responses=ShippingNoticeRetrieveSerializer,
        parameters=[OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)],
    )
    @action(detail=True, methods=["POST"])
    def lock_and_package(self, request: Request, pk=None):
        service = ShippingNoticeService()
        notice = service.lock_and_package(int(pk))
        for package in notice.packages:
            print_package_labels(package)
        return Response(
            ShippingNoticeRetrieveSerializer(notice).data, status=status.HTTP_200_OK
        )

    # def list(self, request: Request):
    #     received_items = ShippingNoticeService.list(
    #         **self.get_pagination_params(request),
    #         statuses=request.query_params.getlist("statuses"),
    #     )
    #     serializer = PaginatedShippingNoticeSerializer(received_items)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=None,
        responses=ShippingNoticeRetrieveSerializer,
        parameters=[OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)],
    )
    @action(detail=True, methods=["POST"])
    def make_upload_template(self, request: Request, pk=None):
        notice = ShippingNoticeService.retrieve(int(pk))
        wb = make_cj_workbook(notice)

        filename = f"CJ_TEMPLATE_{notice.code}_{int(datetime.now().timestamp())}.xls"
        s3_path = f"cj-templates/{filename}"

        with default_storage.open(s3_path, "wb") as f:
            wb.save(f)

        template_url = f"https://alloff.s3.ap-northeast-2.amazonaws.com/{s3_path}"

        service = ShippingNoticeService()

        return Response(
            ShippingNoticeRetrieveSerializer(
                service.record_shipping_template(int(pk), template_url)
            ).data,
            status=status.HTTP_200_OK,
        )

    # @action(detail=True, url_path="seal", methods=["POST"])
    # def seal(self, request: Request, pk=None):
    #     return Response({"message": "ok"}, status=status.HTTP_200_OK)
