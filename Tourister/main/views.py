from django.shortcuts import render,resolve_url
from django.http import HttpRequest , HttpResponse

# Create your views here.

def home_page(request: HttpRequest):
  return render(request, "main/home.html")

def city_riyadh(request: HttpRequest):
  return render(request, "main/city_riyadh.html")
  
def city_abha(request: HttpRequest):
  return render(request, "main/city_abha.html")

def city_makkah(request: HttpRequest):
  return render(request, "main/city_makkah.html")

def city_AlUla(request: HttpRequest):
  return render(request, "main/city_Alula.html")
