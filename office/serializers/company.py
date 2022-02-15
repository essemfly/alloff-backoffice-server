from office.models.company import Company
from office.models.company_brand import CompanyBrand
from rest_framework import serializers


class CompanyBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyBrand
        fields = [
            "name",
            "keyname",
        ]


class CompanySerializer(serializers.ModelSerializer):
    company_brands = CompanyBrandSerializer(many=True)

    class Meta:
        model = Company
        fields = ["company_brands", "keyname", "name"]
