"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from . import views
from django.contrib import admin
from django.urls import path, include
from crudApp.views import index
# from .import views
# from crudApp.views import index
# app_name = 'crudApp'
from crudApp import views
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
        
    path('create/',include('crudApp.urls')),
]
