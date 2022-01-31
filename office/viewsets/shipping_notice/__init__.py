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
from office.services.shipping_notice import ShippingNoticeService
from office.utils.openapi import PROTO_PAGINATION_QUERY_PARAMS
from office.viewsets.pagination import PaginationListMixin
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from protos.logistics.shipping_notice.shipping_notice_pb2 import ShippingNoticeRetrieveRequest


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
        responses=ShippingNoticeRetrieveSerializer
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

    # def list(self, request: Request):
    #     received_items = ShippingNoticeService.list(
    #         **self.get_pagination_params(request),
    #         statuses=request.query_params.getlist("statuses"),
    #     )
    #     serializer = PaginatedShippingNoticeSerializer(received_items)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)

    # @action(detail=True, url_path="make-upload-template", methods=["POST"])
    # def make_upload_template(self, request: Request, pk=None):
    #     return Response({"message": "ok"}, status=status.HTTP_200_OK)

    # @action(detail=True, url_path="seal", methods=["POST"])
    # def seal(self, request: Request, pk=None):
    #     return Response({"message": "ok"}, status=status.HTTP_200_OK)

    # @action(detail=True, url_path="package", methods=["POST"])
    # def package(self, request: Request, pk=None):
    #     return Response({"message": "ok"}, status=status.HTTP_200_OK)
