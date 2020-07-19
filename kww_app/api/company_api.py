from kww_app.api_serializers.company_serial import CompanySerializer
from kww_app.models import Project, Company
from rest_framework import viewsets, permissions


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()

    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = CompanySerializer


