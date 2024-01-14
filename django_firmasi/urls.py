"""
URL configuration for django_firmasi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from page.views import (
    home_view, 
    about_us_view, 
    contact_us_view,
    vision_view
    )

urlpatterns = [
    path("", home_view, name='home'),
    path("haqqimizda/", about_us_view, name='about_us'),
    path("elaqe/", contact_us_view, name='contact_us'),
    path("vizyonumuz/", vision_view, name='vision'),
    path("admin/", admin.site.urls),
]

