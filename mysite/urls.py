from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.Registration, name='register'),
    path('profile/', views.Profile, name='profile'),
    path('new_site/', views.post_project, name='new_site'),
    path('images/(\d+)', views.single_page, name='single_page')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
