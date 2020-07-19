from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from taggit_autosuggest.managers import TaggableManager

from kww_app.models import Link


class Technology(models.Model):
    class Meta:
        verbose_name_plural = "technologies"

    name = models.CharField(max_length=64)
    content = RichTextField(config_name='example', null=True, blank=True)
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

    links = GenericRelation(Link)

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
    description = RichTextField(config_name='awesome_ckeditor', null=True, blank=True)
    links = GenericRelation(Link)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
