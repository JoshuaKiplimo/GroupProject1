from django.shortcuts import render
import requests
import json
from pages.getdata import get_news, get_weather

def index(request):   
    context = {}
    weather = get_weather()
    news = get_news()

    context['news'] = news
    context['weather'] = weather
    #print(context)
    
    return render(request, 'pages/index.html', context)
