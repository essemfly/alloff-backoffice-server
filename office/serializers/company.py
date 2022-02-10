from office.models.company import Company
from office.models.company_brand import CompanyBrand
from rest_framework import serializers


class CompanyBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyBrand
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    company_brands = CompanyBrandSerializer(many=True)

    class Meta:
        model = Company
        fields = "__all__"
