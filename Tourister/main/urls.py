from django.urls import path
from.import views

nameApp="main"

urlpatterns=[
    path("",views.home_page,name="home_page"),
    path("city/Riyadh/",views.city_riyadh,name="city_abha"),
    path("city/Abha/",views.city_abha,name="city_riyadh"),
    path("city/Mekkah/",views.city_makkah,name="city_makkah"),
    path("city/AlUla/",views.city_AlUla,name="city_AlUla"),
]