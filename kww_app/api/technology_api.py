from kww_app.api_serializers.technology_serial import TechnologySerializer
from kww_app.models import Technology
from rest_framework import viewsets, permissions


class TechnologyViewSet(viewsets.ModelViewSet):
    queryset = Technology.objects.all()

    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = TechnologySerializer


