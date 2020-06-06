import json
import requests

def get_weather():
    payload ={'q': "Columbia", 'units': 'imperial', 'APPID': '30cdffc331ee3350cc4a2a433f4f195d'}
    weather =requests.get('https://api.openweathermap.org/data/2.5/forecast?',params=payload).json()

    return weather



    '''

    playing with APIS - news API

    '''

def get_news():

    url = ('https://newsapi.org/v2/top-headlines?country=us&apiKey=8127eaf0360c418bbca2fc125a5171a0')
    response = requests.get(url).json()
    return response

