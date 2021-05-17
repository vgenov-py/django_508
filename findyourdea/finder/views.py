from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Se encuentra en la página Index")

def contact(request):
    return HttpResponse("Se encuentra en la página de contactos")