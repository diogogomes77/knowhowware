from django.shortcuts import render
from django.utils import timezone
from django.views import generic

from kww_app.models import Project, ProjectParticipation, Participant


def get_lateral_menu_options():
    pages = []
    projects = {
        'name': "Projects",
        'href': "/projects"
    }
    pages.append(projects)
    return pages


class HomeView(generic.TemplateView):
    template_name = 'kww_app/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['pages'] = get_lateral_menu_options()
        return context


class ProjectListView(generic.ListView):
    model = Project
    template_name = 'kww_app/project_list.html'
    context_object_name = 'project_list'
    queryset = Project.objects.all()# [:5]
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = get_lateral_menu_options()
        return context


class ProjectDetailView(generic.DetailView):
    model = Project
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = get_lateral_menu_options()
        context['now'] = timezone.now()
        return context


class ParticipationListView(generic.ListView):
    model = ProjectParticipation
    template_name = 'kww_app/project-participation_list.html'
    context_object_name = 'participation_list'
    queryset = ProjectParticipation.objects.all()# [:5]
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = get_lateral_menu_options()
        return context


class ParticipationDetailView(generic.DetailView):
    model = ProjectParticipation
    context_object_name = 'project-participation'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = get_lateral_menu_options()
        context['now'] = timezone.now()
        return context


class ParticipantListView(generic.ListView):
    model = Participant
    template_name = 'kww_app/participant_list.html'
    context_object_name = 'participant_list'
    queryset = Participant.objects.all()# [:5]
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = get_lateral_menu_options()
        return context


class ParticipantDetailView(generic.DetailView):
    model = Participant
    context_object_name = 'participant'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = get_lateral_menu_options()
        context['now'] = timezone.now()
        return context


