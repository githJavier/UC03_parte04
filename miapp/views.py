from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, 'inicio.html')

def uc3(request):
    return render(request, 'uc3.html')

def noticia(request):
    return render(request, 'noticia.html')
