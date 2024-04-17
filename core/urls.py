"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken import views

urlpatterns = [
    # Backoffice for managing API data
    path('backoffice/', admin.site.urls),
    # Django REST Framework urls
    path('auth/', include('rest_framework.urls')),
    path('token/', views.obtain_auth_token),
    # Apps
    path('api/v1/geoconnector/', include('geoconnector.urls')),
    # Django Debug Toolbar
    path('__debug__/', include('debug_toolbar.urls')),
]
