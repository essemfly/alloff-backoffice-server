from datetime import datetime

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets

from tagger.core.drf.search_filter import CustomSearchFilter
from tagger.core.mongo.models.alloff_product import AlloffProductTemplate
from tagger.serializers.timedeal_product import TimedealProductTemplateSerializer


class TimedealProductTemplateViewSet(viewsets.ModelViewSet):
    queryset = AlloffProductTemplate.objects().order_by("-id")
    filter_backends = [CustomSearchFilter]
    search_fields = [
        "brand__korname",
        "name"
    ]
    permission_classes = [IsAuthenticated]
    serializer_class = TimedealProductTemplateSerializer

    def destroy(self, request: Request, id=None):
        template = self.get_object()  # type: AlloffProductTemplate
        template.removed = True
        template.updated = datetime.utcnow()
        template.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
