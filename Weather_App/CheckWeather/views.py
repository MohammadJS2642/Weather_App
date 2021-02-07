from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import json
from Weather_App.local_settings import Api_Key


# Create your views here.
def ShowWeather(request, cityname=''):
    try:
        # for check what method is called
        if request.method == "GET":
            query = request.GET.get('cityname')
            # this is api url for request to that
            # city = cityname

            url = f"http://api.openweathermap.org/data/2.5/weather?q={query}&appid={Api_Key}"

            # get string (json) from url
            response = requests.get(url)

            # convert that string to json
            check = response.json()

            if check['cod'] == '400':
                context = {
                    'not': 'Please set city!!',
                }
                return render(request, 'CheckWeather/index.html', context)

            elif check['cod'] == '404':
                context = {
                    'not': 'City Not Found!!',
                }
                return render(request, 'CheckWeather/index.html', context)

            else:
                # **************************
                # search inside weather arrey
                weather_list = check['weather'][0]

                # searching inside main dictionary
                main = check['main']

                # wind
                wind = check['wind']
                # **************************

                # find main in weather status
                status = weather_list['main']

                # find weather description
                description = weather_list['description']

                # Weather Icon
                weather_icon = weather_list['icon']

                # temp in main
                temp_kelvin = main['temp']
                temp = round((temp_kelvin-273.15), 1)

                # speed wind
                speed_wind = wind['speed']

                # degree wind
                degree_wind = wind['deg']

                # city name
                name = check['name']

                context = {
                    'name': name,
                    'status': status,
                    'description': description,
                    'weather_icon': weather_icon,
                    'temp': temp,
                    'speed_wind': speed_wind,
                    'degree_wind': degree_wind,
                }

                return render(request, 'CheckWeather/index.html', context)

    except Exception as e:
        return render(request, 'checkweather/index.html', e)


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

    # search inside weather arrey
    # weather_list = check['weather'][0]

    # searching inside main dictionary
    # main = check['main']

    # find main in weather status
    # status = weather_list['main']

    # find weather description
    # description = weather_list['description']

    # Weather Icon
    # weather_icon = weather_list['icon']

    # temp in main
    # temp = main['temp']

    # wind
    # wind = check['wind']

    # speed wind
    # speed_wind = wind['speed']

    # degree wind
    # degree_wind = wind['deg']

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
    return render(request, 'checkweather/index.html')
