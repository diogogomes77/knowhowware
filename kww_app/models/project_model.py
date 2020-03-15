from django.contrib.auth.models import User
from django.db import models


class ProjectType(models.Model):
    name = models.CharField(max_length=32, blank=False)


class Project(models.Model):
    name = models.CharField(max_length=64, blank=False)
    projecttype = models.ForeignKey(
        ProjectType,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)
    participants = models.ManyToManyField(
        'Participant',
        through='ProjectParticipation',
        through_fields=["project", "participant"]
    )
    companies = models.ManyToManyField(
        'Company',
        through='ProjectParticipation',
        related_name='projects',
        through_fields=["project", "company"]
    )
    parent = models.ForeignKey(
        'Project',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

