from ckeditor.fields import RichTextField
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class ProjectParticipation(models.Model):
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE)
    participant = models.ForeignKey(
        'Participant',
        on_delete=models.CASCADE
    )
    role = models.ForeignKey(
        'Role',
        null=True,
        on_delete=models.SET_NULL
    )
    company = models.ForeignKey(
        'Company',
        null=True,
        on_delete=models.SET_NULL
    )
    technologies = models.ManyToManyField(
        'Technology',
        through='TechnologyUse',
        through_fields=['projectparticipation', 'technology']
    )

    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def slug(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('participation-detail', args=[str(self.slug)])

    def add_technology(self, tech):
        from kww_app.models import Technology
        if not isinstance(tech, Technology):
            return False
        from kww_app.models import TechnologyUse
        tech_use, created = TechnologyUse.objects.get_or_create(
            technology=tech,
            projectparticipation=self
        )
        if created:
            return True
        return False

    def __str__(self):
        try:
            participant = self.participant.username
        except:
            participant = ""
        try:
            project = self.project.name
        except:
            project = ""
        try:
            role = self.role.name
        except:
            role = ""
        return participant + " on " + project + " as " + role


class ProjectParticipationIssue(models.Model):
    participation = models.ForeignKey(
        'ProjectParticipation',
        null=False,
        related_name="issues",
        on_delete=models.CASCADE
    )
    issue = RichTextField(config_name='awesome_ckeditor', null=True, blank=True)
    technology = models.ForeignKey(
        'Technology',
        null=True, blank=True,
        related_name="issues",
        on_delete=models.CASCADE
    )
    # technologies = models.ManyToManyField(
    #     'Technology',
    #     through='TechnologieIssue',
    #     through_fields=['issue', 'technology']
    # )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TechnologieIssue(models.Model):
    technology = models.ForeignKey('Technology', on_delete=models.CASCADE, null=True)
    issue = models.ForeignKey(
        ProjectParticipationIssue,
        on_delete=models.SET_NULL,
        null=True
    )
    description = RichTextField(config_name='awesome_ckeditor', null=True, blank=True)


@receiver(post_save, sender=ProjectParticipation)
def participation_company_add(sender, instance, created, **kwargs):
    participation = instance
    project = participation.project
    company = participation.company
    if company and not (company in project.companies.all()):
        project.add_company(company)