from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Link(models.Model):
    url = models.URLField()
    description = models.CharField(max_length=128, null=True, blank=True)
    link_type = models.ForeignKey('LinkType', null=True, blank=True, on_delete=models.SET_NULL)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()


class LinkType(models.Model):
    link_type = models.CharField(max_length=32)

    def __str__(self):
        return self.link_type

