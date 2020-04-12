from django.contrib import admin
from django.urls import path, include, reverse
from django.conf import settings
from django.conf.urls.static import static

from frontend.views import index
from kww_app import views
from kww_app.api import ProjectViewSet
from kww_app.views import download
from rest_framework import routers

from kww_celery.views import celery_view, CreateView, DetailView, IndexView

router = routers.DefaultRouter()
router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('projects', views.ProjectListView.as_view(), name='project-list'),
    path('projects/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
    path('participations', views.ParticipationListView.as_view(), name='project-participation-list'),
    path('participations/<int:pk>', views.ParticipationDetailView.as_view(), name='project-participation-detail'),
    path('participants', views.ParticipantListView.as_view(), name='participant-list'),
    path('participants/<int:pk>', views.ParticipantDetailView.as_view(), name='participant-detail'),

    path('download/<int:id>/', download, name='download'),
    path('taggit_autosuggest/', include('taggit_autosuggest.urls')),

    path('frontend/', index),

    path('celerytask/', celery_view),
    path('person/add/', CreateView.as_view(),
         name='person-create'
         ),
    path('person/<int:pk>/', DetailView.as_view(), name='person-detail'),
    path('person/', IndexView.as_view(), name='person-list'),

]

urlpatterns += router.urls


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)