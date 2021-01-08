from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
import requests
from django.template.loader import render_to_string

# Create your views here.


def ShowWeather(request):
    api = '35017b640b12e562215df7ca0500d361'
    city = 'tehran'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"

    response = requests.get(url)

    check = response.json()
    weather = check[0]

    # context = {'check': check}

    # return HttpResponse()
    return render_to_string(weather)
    # return redirect(check)
