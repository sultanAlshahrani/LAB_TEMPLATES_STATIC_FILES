from django.shortcuts import render,resolve_url,redirect
from django.http import HttpRequest , HttpResponse

# Create your views here.
def base_page(request: HttpRequest):
  cookies = request.COOKIES
  return render(request, "main/base.html")

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


def consent_to_TOS(request : HttpRequest):

    response = redirect("main:base_page")
    response.set_cookie("consent", "Yes", max_age=60*60*24*7)

    return response

def set_dark_mode(request : HttpRequest):

  response = redirect("main:base_page")
  response.set_cookie("mode", "dark", max_age=60*60*24*7)

  return response


def set_light_mode(request : HttpRequest):

    response = redirect("main:base_page")
    response.set_cookie("mode", "light", max_age=60*60*24*7)

    return response