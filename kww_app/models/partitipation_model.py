from django.db import models


class ProjectParticipation(models.Model):
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE)
    participant = models.ForeignKey(
        'Participant',
        on_delete=models.CASCADE
    )
    role = models.ForeignKey(
        'Role',
        null=True,
        on_delete=models.SET_NULL
    )
    company = models.ForeignKey(
        'Company',
        null=True,
        on_delete=models.SET_NULL
    )
    tecnologies = models.ManyToManyField(
        'Technology',
        through='TechnologyUse',
        through_fields=['projectparticipation', 'technology']
    )

    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def add_technology(self, tech):
        from kww_app.models import Technology
        if not isinstance(tech, Technology):
            return False
        from kww_app.models import TechnologyUse
        tech_use, created = TechnologyUse.objects.get_or_create(
            technology=tech,
            projectparticipation=self
        )
        if created:
            return True
        return False

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

