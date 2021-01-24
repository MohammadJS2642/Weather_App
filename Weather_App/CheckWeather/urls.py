from django.urls import path
from . import views

urlpatterns = [
    path('showweather/<cityname>/', views.ShowWeather, name="showweather"),
    path('showweather/', views.ShowWeather, name="showweather"),
]
