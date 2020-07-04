from urllib.parse import urlparse

from django.contrib.auth.models import User
from django.db import models
from django.http import HttpResponse
from django.urls import reverse
from minio_storage.storage import MinioMediaStorage

storage = MinioMediaStorage()


class Participant(User):
    onboard = models.DateField(null=True, blank=True)
    offboard = models.DateField(null=True, blank=True)

    projects = models.ManyToManyField(
        'Project',
        through='ProjectParticipation',
        related_name='participations',
        through_fields=["participant", "project"]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    photo = models.ImageField(
        null=True,
        blank=True,
        storage=storage
    )

    @property
    def slug(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('participant-detail', args=[str(self.slug)])



class Role(models.Model):
    name = models.CharField(max_length=32, blank=False)

    def __str__(self):
        return self.name


