from django.shortcuts import render
import json
import requests


def index(request):

    if request.method=="GET":
            city=request.GET.get('city')


            url='http://api.openweathermap.org/data/2.5/weather?q={}&appid=6af01b33fed0b78cdf6c455503eb8f30'
            r=requests.get(url.format(city)).json()
            print (r)
            t= r['main']['temp']

            temp= float(t)-273.15
            t1=round(temp,2)
            print(t1)
            weather={

                'city':city,
                'temp':t1,
                'description': r['weather'][0]['description'],
                'icon':r['weather'][0]['icon'],
                    }
            print(weather)
    return render (request, 'weather.html',weather)
