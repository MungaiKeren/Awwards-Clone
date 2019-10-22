from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

router = routers.DefaultRouter()
router.register('projects', views.ProjectView)

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.Registration, name='register'),
    path('profile/', views.Profile, name='profile'),
    path('new_site/', views.post_project, name='new_site'),
    path('project/<int:project_id>', views.get_project, name='project'),
    path('search/', views.search_results, name='search'),
    path('api/', include(router.urls))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
