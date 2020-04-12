from django import forms
from django.shortcuts import HttpResponse
from django.urls import reverse
from django.views import View, generic

from kww_celery.models import PersonAge
from .tasks import celery_task


def celery_view(request):
    for counter in range(2):
        celery_task.delay(counter)
    return HttpResponse("FINISH PAGE LOAD")


class IndexView(generic.ListView):
    template_name = 'kww_celery/index.html'
    context_object_name = 'persons'

    def get_queryset(self):
        """Return the last five published questions."""
        return PersonAge.objects.all()


class DetailView(generic.DetailView):
    model = PersonAge
    template_name = 'kww_celery/detail.html'
    context_object_name = 'person'


class CreateNewPerson(forms.ModelForm):
    class Meta:
        model = PersonAge
        fields = ['name', 'born']

        widgets = {
            'born': forms.DateInput(format=('%m/%d/%Y'),
                 attrs={'class': 'form-control', 'placeholder': 'Select a date',
                        'type': 'date'}),
        }


class CreateView(generic.CreateView):
    model = PersonAge
    form_class = CreateNewPerson
    template_name = 'kww_celery/create.html'
    success_url = '/person/'


