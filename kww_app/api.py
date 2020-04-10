from rest_framework.decorators import action

from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer


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

