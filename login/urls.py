from django.urls import path

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.loginView, name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='base.html'), name='logout'),  
]