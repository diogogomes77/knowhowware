from django.contrib.auth.models import User
from django.db import models


class Participant(User):
    onboard = models.DateField(null=True, blank=True)
    offboard = models.DateField(null=True, blank=True)
    technologies = models.ManyToManyField(
        'Technology',
        through='TechnologyUse',
        related_name='participants',
        through_fields=["participant", "technology"]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Role(models.Model):
    name = models.CharField(max_length=32, blank=False)

    def __str__(self):
        return self.name


class ProjectParticipation(models.Model):
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE)
    participant = models.ForeignKey(
        Participant,
        related_name="projects",
        null=True,
        on_delete=models.SET_NULL
    )
    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)
    role = models.ForeignKey(
        Role,
        related_name="participations",
        null=True,
        on_delete=models.SET_NULL
    )
    company = models.ForeignKey(
        'Company',
        null=True,
        on_delete=models.SET_NULL
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        try:
            participant = self.participant.username
        except:
            participant = ""
        try:
            project = self.project.name
        except:
            project = ""
        try:
            role = self.role.name
        except:
            role = ""

        return participant + " on " + project + " as " + role
