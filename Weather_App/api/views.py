# from django.shortcuts import render

# for create api with function base
from rest_framework.decorators import api_view
from rest_framework.response import Response
# -----------------------

# clase base
from rest_framework.views import APIView
# -----------------------

# OTHER
# TODO: find way for use generics instead class base
# from rest_framework.generics import ListAPIView
# -----------------------

# for get data from url
import requests
from Weather_App.local_settings import Api_Key
# -----------------------


# Create your views here.


# for now i use this class base apis
class ClassApi(APIView):
    '''
    this is a classBase api for get data from 
    app
    '''

    def get(self, request, cityname=''):
        '''
        get json request from app
        '''
        query = cityname
        url = f"http://api.openweathermap.org/data/2.5/weather?q={query}&appid={Api_Key}"
        r = requests.get(url)
        return Response(r)


@api_view(['GET'])
def sendAsk(request, cityname=''):
    # i don't use this function base
    '''
        return json response from app 
        function base
    '''
    if request.method == 'GET':
        query = cityname
        url = f"http://api.openweathermap.org/data/2.5/weather?q={query}&appid={Api_Key}"
        r = requests.get(url)
        return Response(r)
