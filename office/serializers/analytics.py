from rest_framework import fields, serializers


class RefreshExhibitionGoogleSheetResponse(serializers.Serializer):
    spreadsheetId = fields.CharField()
    updatedRange = fields.CharField()
    updatedRows = fields.IntegerField()
    updatedColumns = fields.IntegerField()
    updatedCells = fields.IntegerField()
