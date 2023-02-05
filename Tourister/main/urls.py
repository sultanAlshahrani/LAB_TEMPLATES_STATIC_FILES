from django.urls import path
from.import views

nameApp="main"

urlpatterns=[
    path("", views.base_page, name="base_page"),
    path("home/",views.home_page,name="home_page"),
    path("city/Riyadh/",views.city_riyadh,name="city_abha"),
    path("city/Abha/",views.city_abha,name="city_riyadh"),
    path("city/Mekkah/",views.city_makkah,name="city_makkah"),
    path("city/AlUla/",views.city_AlUla,name="city_AlUla"),
    path("consent/tos/", views.consent_to_TOS, name="consent_to_tos"),
    path("mode/dark/", views.set_dark_mode, name="mode_dark"),
    path("mode/light/", views.set_light_mode, name="mode_light"),


]