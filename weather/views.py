import requests
from django.shortcuts import render
from django.contrib import messages
import json

def index(request):
    if request.method == 'POST':
        city = request.POST['city'].strip()
        
        # Using wttr.in - no API key required
        url = f'http://wttr.in/{city}?format=j1'
        
        try:
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                current = data['current_condition'][0]
                
                weather_data = {
                    'city': city.title(),
                    'temperature': current['temp_C'],
                    'description': current['weatherDesc'][0]['value'],
                    'humidity': current['humidity'],
                    'wind_speed': current['windspeedKmph'],
                    'feels_like': current['FeelsLikeC'],
                }
                return render(request, 'weather/index.html', {'weather_data': weather_data})
            else:
                messages.error(request, 'City not found!')
        except Exception as e:
            messages.error(request, f'Error fetching weather data: {str(e)}')
    
    return render(request, 'weather/index.html')