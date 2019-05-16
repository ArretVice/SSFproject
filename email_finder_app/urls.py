from django.urls import path
from . import views

app_name = 'email_finder'

urlpatterns = [
    path('', views.email_finder_view, name='home'),
]
