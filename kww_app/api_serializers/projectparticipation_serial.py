from rest_framework import serializers
from kww_app.models import ProjectParticipation


class TProjectParticipationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectParticipation
        fields = '__all__'

