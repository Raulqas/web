from datetime import datetime
from django.urls import path, re_path, include
from django.contrib import admin
from app import forms, views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('links/', views.links, name='links'),
    path('feedback/', views.feedback_view, name='pool'),
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('registration', views.registration, name='registration'),
    path('login/', auth_views.LoginView.as_view(next_page='home'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('blog/', views.blog, name='blog'),
    path('newpost/', views.newpost, name='newpost'),
    re_path(r'^(?P<parametr>\d+)/$', views.blogpost, name='blogpost'),
    path('video/', views.videopost, name='videopost'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])