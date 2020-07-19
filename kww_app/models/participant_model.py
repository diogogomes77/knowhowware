from urllib.parse import urlparse

from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.http import HttpResponse
from django.urls import reverse
from minio_storage.storage import MinioMediaStorage

from kww_app.models import Link

storage = MinioMediaStorage()


class Participant(User):


    projects = models.ManyToManyField(
        'Project',
        through='ProjectParticipation',
        related_name='participations',
        through_fields=["participant", "project"]
    )

    jobs = models.ManyToManyField(
        'Company',
        through='HasJob',
        related_name='colaborators',
        through_fields=["participant", "company"]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    photo = models.ImageField(
        null=True,
        blank=True,
        storage=storage
    )

    links = GenericRelation(Link)

    @property
    def slug(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('participant-detail', args=[str(self.slug)])


class Role(models.Model):
    name = models.CharField(max_length=32, blank=False)

    def __str__(self):
        return self.name


class HasJob(models.Model):
    participant = models.ForeignKey(
        'Participant',
        on_delete=models.CASCADE,
        null=False
    )
    company = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE,
        null=False
    )
    role = models.ForeignKey(
        'Role',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    onboard = models.DateField(null=True, blank=True)
    offboard = models.DateField(null=True, blank=True)


