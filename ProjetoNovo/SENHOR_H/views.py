from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def SENHOR_H(request):
    print("teste simples")
    return HttpResponse("AGORA SENHOR_H <br><a href='..'>voltar</a><br><a href='teste/'>Próxima Página</a>")

def srh(request):
    print("teste simples 2")
    return HttpResponse("AGORA Sr.H", )
def teste(request):
    print("Teste")
    return render(request,"SENHOR_H/HTML.html")
