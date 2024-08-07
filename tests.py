from unittest import mock
import unittest
import mock

import app
from app import GEOCODING_API_URL, WEATHER_API_URL

import requests_mock
#
class SomefileTestCase1(unittest.TestCase):

    def test_method_weather1(self):
        m = mock.MagicMock()
        m.values = "MyData"
        with mock.patch("app.request", m):
            app.weather()
    def test_method_weather_data(self):

        with requests_mock.Mocker() as m:
            m.get(WEATHER_API_URL, json={
            'latitude': 51.5073219,
            'longitude': -0.1276474,
            'current': {'temp': 28.61, 'wind_speed': 2.68, 'rain':{"1h": 0.25}},
            'precipitation': {"1h": 0.25},
            'location': f"Lat: 51.507321, Lon:-0.1276474"
        })
            app.get_weather_data({'lat': 51.5073219, 'lon': -0.1276474})

    def test_method_coordinates1(self):

        with requests_mock.Mocker() as m:
            m.get(GEOCODING_API_URL,  json=[{'lat': 51.5073219, 'lon': -0.1276474}])
            app.get_coordinates(33)

    def test_method_weather2(self):
        m = mock.MagicMock()
        m.values = "MyData"
        with mock.patch("app.request", m ):
            c = mock.MagicMock()
            c.values = None
            with mock.patch("app.get_coordinates", c):

                app.weather()



if __name__ == '__main__':
    unittest.main()
