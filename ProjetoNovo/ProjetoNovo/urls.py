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
from django.conf.urls import handler404

def home(request):
    print("HOME localhost")
    return HttpResponse("HOME")

def home2(request):
    
    return render(request,'Mahouno.html')
def home_final(request):
    return render(request,'home.html')

def ainda_fazer(request):
    return HttpResponse("Ainda não fiz")
def not_found(request):
    return render(request,"404.html")
urlpatterns = [
    path('', home_final),
    path('adminH/', admin.site.urls),
    path('SENHOR_H/', include('SENHOR_H.urls')),
    path("portfolio/", include('Portfolio.urls')),
    path("Portfolio/", include('Portfolio.urls')),
]


