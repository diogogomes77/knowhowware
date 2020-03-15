from django.db import models


class CompanyType(models.Model):
    name = models.CharField(max_length=32, blank=False)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=64, blank=False)
    companytype = models.ForeignKey(
        'CompanyType',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    parent = models.ForeignKey(
        'Company',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    participants = models.ManyToManyField(
        'Participant',
        through='ProjectParticipation',
        through_fields=['company', 'participant']
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProjectCompany(models.Model):
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE)
    company = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE
    )

    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
