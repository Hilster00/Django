from django.shortcuts import render
from django.http import HttpResponse

def Portfolio(requests):
    return render(requests, "Portfolio/Portfolio.html")

