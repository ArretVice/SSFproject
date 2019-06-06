"""mainapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path(os.environ.get('DJANGO_SSF_PROJECT_ADMIN_URL'), admin.site.urls),
    path('', views.home_view, name='home'),
    path('email_finder/', include('email_finder_app.urls')),
    path('wishlist/', include('wishlist_app.urls')),
    path('users/', include('users_app.urls')),
    path('exchangerates/', include('exchangerates_app.urls')),
    path('blog/', include('blog_app.urls')),
    path('', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
