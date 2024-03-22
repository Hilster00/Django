from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "CienciaDados/home.html")
def Centralidade(request):
    return render(request, "CienciaDados/Centralidade.html")

def DistribuicaoStarrDrops(request):
    return render(request, "CienciaDados/DistribuicaoStarrDrops.html")

def SepararAmostra(request):
    return render(request, "CienciaDados/SepararAmostra.html")

def Stratify(request):
    return render(request, "CienciaDados/Stratify.html")
