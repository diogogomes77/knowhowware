from django.contrib.auth.models import User
from django.db import models


class ProjectParticipation(models.Model):
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE)
    participant = models.ForeignKey(
        'Participant',
        on_delete=models.CASCADE
    )
    company = models.ForeignKey(
        'Company',
        null=True,
        on_delete=models.SET_NULL
    )
    tecnologies = models.ManyToManyField(
        'Technology',
        through='TechnologyUse',
        through_fields=['projectparticipationn', 'technology']
    )
    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)
    role = models.ForeignKey(
        'Role',
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


class ProjectParticipationIssue(models.Model):
    participation = models.ForeignKey(
        'ProjectParticipation',
        null=False,
        related_name="issues",
        on_delete=models.CASCADE
    )
    issue = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

