
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^temperature/create_reading$', views.create_weather_reading, name='create_reading'),
    url(r'^temperature/get_current_reading$', views.get_temperature_reading, name='get_current_reading'),
]
