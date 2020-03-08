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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Participant(User):
    onboard = models.DateField(null=True, blank=True)
    offboard = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Role(models.Model):
    name = models.CharField(max_length=32, blank=False)

    def __str__(self):
        return self.name


class ProjectParticipation(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE)
    participant = models.ForeignKey(
        Participant,
        related_name="projects",
        on_delete=models.CASCADE)
    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)
    role = models.ForeignKey(Role, related_name="participations", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)