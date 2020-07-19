from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, reverse
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from frontend.views import index
from kww_app import views
from kww_app.api import ProjectViewSet
from kww_app.views import download
from rest_framework import routers

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from kww_celery.views import celery_view, CreateView, DetailView, IndexView


router = routers.DefaultRouter()
router.register('api/projects', ProjectViewSet, 'projects')


urlpatterns = [
    #path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('api/', include((router.urls, 'api'), namespace='api')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),
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
    path('ckeditor/', include('ckeditor_uploader.urls')),

]

urlpatterns += router.urls


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns