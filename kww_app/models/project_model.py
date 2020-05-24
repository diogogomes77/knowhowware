from ckeditor.fields import RichTextField
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.conf import settings
from django.utils.text import slugify
from taggit_autosuggest.managers import TaggableManager


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

    image = models.ImageField(
        upload_to=settings.PROJECT_IMAGES,
        null=True,
        blank=True
    )
    file = models.FileField(
        upload_to=settings.PROJECT_FILES,
        null=True,
        blank=True
    )

    tags = TaggableManager(blank=True)
    #slug = models.SlugField(max_length=31, unique=True, null=True)

    content = RichTextField(config_name='example', null=True, blank=True)

    def _save(self, *args, **kwargs):
        #self.slug = slugify(self.name, allow_unicode=True)
        return super(Project, self).save(*args, **kwargs)

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.image))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.name

    def download(self):
        pass

    @property
    def slug(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('project-detail', args=[str(self.slug)])

    def add_participant(self, participant, role=None, company=None):
        from kww_app.models import Participant
        if not isinstance(participant, Participant):
            return False
        from kww_app.models import ProjectParticipation
        prj_participation, created = ProjectParticipation.objects.get_or_create(
            project=self,
            participant=participant,
            role=role,
            company=company,
        )
        return prj_participation

    def add_company(self, company):
        from kww_app.models import Company
        if not isinstance(company, Company):
            return False
        from kww_app.models import ProjectCompany
        prj_company, created = ProjectCompany.objects.get_or_create(
            project=self,
            company=company,
        )
        return prj_company



