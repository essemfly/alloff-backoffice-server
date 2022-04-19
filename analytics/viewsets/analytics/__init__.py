from drf_spectacular.utils import extend_schema
from office.serializers.analytics import RefreshExhibitionGoogleSheetResponse
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from analytics.scripts.exhibition import update_google_sheet


class AnalyticsViewSet(viewsets.ViewSet):
    @extend_schema(responses={status.HTTP_200_OK: RefreshExhibitionGoogleSheetResponse})
    @action(detail=False, methods=["GET"])
    def refresh_exhibition_google_sheet(self, request):
        return Response(update_google_sheet(), status=status.HTTP_200_OK)
