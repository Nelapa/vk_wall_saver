"""vk_wall_saver URL Configuration"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from posts_saver import views

urlpatterns = [
    url(r'^$', views.ten_posts),
    url(r'^login$', auth_views.LoginView.as_view(template_name='login.html')),
    url(r'^logout$', auth_views.LogoutView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'', include('social_django.urls')),
]
