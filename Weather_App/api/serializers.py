from rest_framework import serializers
from Weather_App.local_settings import Api_Key

import requests


class SendAskSerializer(serializers.ModelSerializer):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={query}&appid={Api_Key}"

    class Meta:
        model =
