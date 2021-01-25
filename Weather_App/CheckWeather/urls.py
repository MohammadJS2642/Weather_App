from django.urls import path
from . import views

urlpatterns = [
    path('showweather/<cityname>/', views.ShowWeather, name="showweather"),
    path('showweather/', views.ShowWeather, name="showweather"),
    path('showweather2/<cityname>/', views.ShowWeather2, name="ShowWeather2"),
    path('showweather2/', views.ShowWeather2, name="ShowWeather2"),
    path('ShowMe/', views.ShowMe, name="ShowMe"),
]
