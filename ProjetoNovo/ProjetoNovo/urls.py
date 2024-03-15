"""
URL configuration for ProjetoNovo project.

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
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    print("HOME localhost")
    return HttpResponse("HOME")

def home2(request):
    
    return render(request,'Mahouno.html')

def ainda_fazer(request):
    return HttpResponse("Ainda não fiz")
urlpatterns = [
    path('', home2),
    path('adminH/', admin.site.urls),
    path('SENHOR_H/', include('SENHOR_H.urls')),
    path("portifolio/", ainda_fazer),
    
]
