from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=64, blank=False)
    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)
    participants = models.ManyToManyField(
        'Participant',
        through='ProjectParticipation',
        related_name='participations',
        through_fields=["project", "participant"]
    )
    technologies = models.ManyToManyField(
        'Technology',
        through='TechnologyUse',
        related_name='projects',
        through_fields=["project", "technology"]
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name