from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from kww_app.models import Project


def get_lateral_menu_options():
    pages = []
    projects = {
        'name': "Projects",
        'href': "/projects"
    }
    pages.append(projects)
    return pages


class HomeView(TemplateView):
    template_name = 'kww_app/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['pages'] = get_lateral_menu_options()
        return context


class ProjectsView(ListView):
    model = Project
    template_name = 'kww_app/project_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProjectsView, self).get_context_data(*args, **kwargs)
        context['pages'] = get_lateral_menu_options()
        return context





