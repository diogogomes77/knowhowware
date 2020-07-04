from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from taggit_autosuggest.managers import TaggableManager


class Technology(models.Model):
    name = models.CharField(max_length=64)
    parents = models.ManyToManyField(
        'self', blank=True,
        through='ParentTechnology',
        through_fields=["technology", "parent"],
        related_name="children",
        symmetrical=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.name


class ParentTechnology(models.Model):
    technology = models.ForeignKey(
        Technology,
        on_delete=models.CASCADE,
        related_name='parent_tech'
    )
    parent = models.ForeignKey(
        Technology,
        on_delete=models.CASCADE,
        related_name='tech_parent'
    )


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
