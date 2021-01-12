from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from Weather_App.local_settings import Api_Key

# Create your views here.


def ShowWeather(request):

    # this is api url for request to that
    city = 'tehran'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={Api_Key}"

    # get string (json) from url
    response = requests.get(url)

    # convert that string to json
    check = response.json()

    # show json like string in html with httpresponse without template
    return HttpResponse(response)

    # display a pice of  from json
    # return HttpResponse(check['weather'])
