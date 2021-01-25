from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from Weather_App.local_settings import Api_Key

# Create your views here.


def ShowWeather(request, cityname=''):

    # for check what method is called
    if request.method == "GET":

        # this is api url for request to that
        city = cityname

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={Api_Key}"

        # get string (json) from url
        response = requests.get(url)

        # convert that string to json
        check = response.json()

    elif check['cod'] == '404':
        return HttpResponse("City is not true")

    # if city not found
    else:
        return HttpResponse("City is not true")

    # show json like string in html with httpresponse without template
    # return HttpResponse(response)

    check2 = check['weather']
    context = {
        'check': check2,
    }

    return render(request, 'CheckWeather/index.html', context)

    # display a pice of  from json
    # return HttpResponse(check['weather'])


def ShowWeather2(request, cityname=''):

    # for check what method is called
    if request.method == "GET":

        # this is api url for request to that
        city = cityname

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={Api_Key}"

        # get string (json) from url
        response = requests.get(url)

        # convert that string to json
        check = response.json()

    elif check['cod'] == '404':
        return HttpResponse("City is not true")

    # if city not found
    else:
        return HttpResponse("City is not true")

    # show json like string in html with httpresponse without template
    return HttpResponse(response)

    # check2 = check['weather']
    # context = {
    #     'check': check2,
    # }

    # return render(request, 'CheckWeather/index.html', context)

    # display a pice of  from json
    # return HttpResponse(check['weather'])


def ShowMe(request):
    return render(request, 'checkweather/index2.html')
