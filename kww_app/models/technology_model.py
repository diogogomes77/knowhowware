from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from taggit_autosuggest.managers import TaggableManager


class Technology(models.Model):
    name = models.CharField(max_length=64)
    parent = models.ForeignKey('Technology', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    tags = TaggableManager()

    def __str__(self):
        return self.name


class TechnologyUse(models.Model):
    technology = models.ForeignKey('Technology', on_delete=models.CASCADE, null=True)
    projectparticipation = models.ForeignKey(
        'ProjectParticipation',
        on_delete=models.SET_NULL,
        null=True
    )
    description = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
