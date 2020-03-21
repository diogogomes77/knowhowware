from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from kww_app.models import Project


class HomeView(TemplateView):
    template_name = 'kww_app/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        pages = []
        projects = {
            'name': "Projects",
            'href': "/projects"
        }
        pages.append(projects)
        context['pages'] = pages
        return context


class ProjectsView(HomeView):
    template_name = 'kww_app/project_list.html'




