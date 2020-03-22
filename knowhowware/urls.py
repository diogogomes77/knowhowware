from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from kww_app import views
from kww_app.views import download

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
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)