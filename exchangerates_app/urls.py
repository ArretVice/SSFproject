from django.urls import path

from . import views


app_name = 'exchangerates'

urlpatterns = [
    path('', views.rates_view, name='exchangerates'),
]
