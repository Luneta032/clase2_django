from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def holaManuel(request):
     return HttpResponse("<h1> HOLA MANUEL </h1>")