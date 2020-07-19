from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from kww_app.models import Company


class CompanySerializer(serializers.ModelSerializer):
    companytype = SerializerMethodField()
    country = SerializerMethodField()

    class Meta:
        model = Company
        fields = (
            'name',
            'companytype',
            'country',
            'parent',
            'participants'
        )

    def get_companytype(self, company):
        return company.companytype.name

    def get_country(self, company):
        return company.country.country


