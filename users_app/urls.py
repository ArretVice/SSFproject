from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


app_name = 'users'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.CustomLoginView.as_view(template_name='users_app/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout')
]
