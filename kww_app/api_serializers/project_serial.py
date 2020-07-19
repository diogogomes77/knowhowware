from rest_framework import serializers
from kww_app.models.project_model import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

