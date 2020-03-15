from django.db import models


class ProjectType(models.Model):
    name = models.CharField(max_length=32, blank=False)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=64, blank=False)
    projecttype = models.ForeignKey(
        'ProjectType',
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
        through='ProjectCompany',
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

    def add_participant(self, participant):
        from kww_app.models import Participant
        if not isinstance(participant, Participant):
            return False
        from kww_app.models import ProjectParticipation
        prj_participation, created = ProjectParticipation.objects.get_or_create(
            project=self,
            participant=participant,
        )
        if created:
            return True
        return False

    def add_company(self, company):
        from kww_app.models import Company
        if not isinstance(company, Company):
            return False
        from kww_app.models import ProjectCompany
        prj_company, created = ProjectCompany.objects.get_or_create(
            project=self,
            company=company,
        )
        if created:
            return True
        return False

