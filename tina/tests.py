from django.test import TestCase
from django.urls import reverse
from tina.models import Location, Temperature
import json

def create_location():
    return Location.objects.create(code='code')

class TemperatureViewTests(TestCase):
    def test_create_weather_reading(self):
        location = create_location()
        response = self.client.post(
            reverse('create_reading'),
            json.dumps({'location_code': 'code', 'reading': 32.11}),
            content_type="application/json")
        temp = Temperature.objects.get(location_id=location.id)
        self.assertTrue(temp)
        self.assertEqual(response.status_code, 200)

