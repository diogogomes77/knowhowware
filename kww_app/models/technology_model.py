from django.contrib.auth.models import User
from django.db import models


class Technology(models.Model):
    name = models.CharField(max_length=64)
    parent = models.ForeignKey('Technology', null=True, blank=True, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TechnologyUse(models.Model):
    technology = models.ForeignKey('Technology', on_delete=models.CASCADE, null=True)
    projectparticipation = models.ForeignKey(
        'ProjectParticipation',
        on_delete=models.SET_NULL,
        null=True
    )
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
