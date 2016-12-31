from django.shortcuts import render
from django.http import HttpResponse
from tina.models import Temperature, Location
import json
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse('Index')

@csrf_exempt
def create_weather_reading(request):
    json_response = json.loads(request.body)
    location = Location.objects.get(code=json_response['location_code'])
    Temperature.objects.create(location = location, reading=float(json_response['reading']))
    return HttpResponse(200)

def get_temperature_reading(request):
    location = Location.objects.get(code=request.GET['location_code'])
    temp = Temperature.objects.filter(location = location).order_by('date')[0]
    response = {'reading': str(temp.reading), 'date': str(temp.date)}
    return HttpResponse(json.dumps(response), content_type='application/json')
