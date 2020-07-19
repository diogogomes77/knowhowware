from rest_framework.decorators import action

from kww_app.api_serializers.project_serial import ProjectSerializer
from kww_app.models import Project
from rest_framework import viewsets, permissions


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()

    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = ProjectSerializer

    @action(detail=True, methods=['get'])
    def download(self, request, *args, **kwargs):
        project = self.get_object()
        return project.download(self.request.user)

