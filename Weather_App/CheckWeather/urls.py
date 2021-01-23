from django.urls import path
from . import views

urlpatterns = [
    path('showweather/<cityname>/', views.ShowWeather, name="ShowWeather"),
    path('showweather/', views.ShowWeather, name="ShowWeather"),
]
