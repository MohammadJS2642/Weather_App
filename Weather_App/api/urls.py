from django.urls import path
from .views import sendAsk, ClassApi

app_name = "api"
urlpatterns = [
    # path('<cityname>/', sendAsk, name='send_ask'),
    path('v1/<cityname>/', ClassApi.as_view(), name='ClassApi'),
]
