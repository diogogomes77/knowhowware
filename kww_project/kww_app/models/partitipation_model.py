from django.contrib.auth.models import User
from django.db import models


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

