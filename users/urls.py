"""define users' urls"""

from django.urls import path, re_path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

from . import views

app_name = 'users'
urlpatterns = [
    # login page
    re_path(r'^login/$', LoginView.as_view(template_name='users/login.html'), name = 'login'),
    re_path(r'^logout/$', LogoutView.as_view(), name = 'logout'),
    re_path(r'^register/$', PasswordChangeView.as_view(template_name='users/register.html'), name = 'register'),
]
