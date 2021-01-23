from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from Weather_App.local_settings import Api_Key

# Create your views here.


def ShowWeather(request):

    # for check what method is called
    if request.method == "GET":

        # using from GET
        cityName = request.method.get['cityname']

        if cityName == '':
            return HttpResponse("Not city")

        # this is api url for request to that
        city = cityName

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={Api_Key}"

        # get string (json) from url
        response = request.get(url)

        # convert that string to json
        check = response.json()

    # if city not found
    else:
        return HttpResponse("City is not true")

    # show json like string in html with httpresponse without template
    return HttpResponse(response)

    # display a pice of  from json
    # return HttpResponse(check['weather'])
