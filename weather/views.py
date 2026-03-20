from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    city=""
    data=None
    if request.method =="POST":
        city=request.POST["city"].strip().title()
        res=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=5f242f3e9eae63bf407a34af3c4856a3').read()
        json_data = json.loads(res)

        temp_kelvin = json_data['main']['temp']
        temp_celsius = round(temp_kelvin - 273.15, 2)
        wind_m_s = json_data['wind']['speed']
        wind_km_h = (wind_m_s*3600)/1000

        data={
            "country_code" : str(json_data['sys']['country']),
            "coordinate" : str(json_data['coord']['lon']) + str(json_data['coord']['lat']),
            "temp" : temp_celsius ,
            "pressure" : str(json_data['main']['pressure']),
            "humidity" : str(json_data['main']['humidity']) ,    
            "wind" : wind_km_h    
            }
    
    return render(request,'index.html',{'city':city , 'data':data})
