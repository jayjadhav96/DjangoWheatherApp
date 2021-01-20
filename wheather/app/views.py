from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
import urllib.request

# Create your views here.

def home(request):

    if request.method == 'POST':
        city = request.POST['city']
        
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=a6ccf7a5461256d99adaa1a07f4dfa53').read()

        list_of_data = json.loads(source)  

        data = { 
            "city": city,
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": (float(list_of_data['main']['temp']) - 273),
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
        }

        print(data) 
    else:
        data ={}             
    
    return render(request, 'app/home.html', data)