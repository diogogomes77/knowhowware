from django.contrib.auth.models import User
from django.db import models


class CompanyType(models.Model):
    name = models.CharField(max_length=32, blank=False)


class Company(models.Model):
    name = models.CharField(max_length=64, blank=False)
    companytype = models.ForeignKey(
        CompanyType,
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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name