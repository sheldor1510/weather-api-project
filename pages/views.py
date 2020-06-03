from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail
import pyowm
from django.contrib import messages



def home(request):
    import pyowm
    owm = pyowm.OWM('54c046a7b9b579e951527fc1dd8c7d1f')
    res = owm.weather_manager()
    place = "London"
    country = "GB"
    observation = owm.weather_at_place(f'{place}, {country}')
    weather = observation.weather
    temperature = weather.temperature('fahrenheit')['temp']
    temperature_in_celcius = int((temperature-32)*5/9)
    humidity = weather.humidity
    status = weather.status
    wind = ((int(weather.wind()['speed']))*3.6)
    wind_dir = int(weather.wind()['deg'])
    if wind_dir < 45:
        wind_dir = "North"
    elif 90 > wind_dir > 45:
        wind_dir = "North-East"
    elif 135 > wind_dir > 90:
        wind_dir = "East"
    elif 180 > wind_dir > 135:
        wind_dir = "South-East"
    elif 225 > wind_dir > 180:
        wind_dir = "South"
    elif 270 > wind_dir > 225:
        wind_dir = "South-West"
    elif 315 > wind_dir > 270:
        wind_dir = "West"
    elif wind_dir > 315:
        wind_dir = "North-West"
    elif wind_dir == 90:
        wind_dir = "East"
    elif wind_dir == 180:
        wind_dir = "South"
    elif wind_dir == 270:
        wind_dir = "West"
    import datetime
    now = datetime.datetime.now()
    from datetime import datetime, date
    today = date.today()
    today = str(today)
    lame =today.split('-')[2]
    date = int(lame)
    date2 = str(date)
    lame1 =today.split('-')[1]
    lame1 = int(lame1)
    months = {
        1:'Jan',
        2:'Feb',
        3:'Mar',
        4:'April',
        5:'May',
        6:'June',
        7:'July',
        8:'Aug',
        9:'Sep',
        10:'Oct',
        11:'Nov',
        12:'Dec'
    }

    month = str(months[lame1])
    day = (now.strftime("%A"))
    date = (date2 +' '+ month)
    context = {
        'day': day,
        'date':date,
        'temperature_in_celcius':temperature_in_celcius,
        'humidity':humidity,
        'wind':wind,
        'wind_dir':wind_dir,
        'place':place
    }

    return render(request, 'pages/index.html', context)

def contact(request):
    return render(request, 'pages/contact.html')

def contactme(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message'] 

        contact = Contact(name=name, email=email, message=message)

        contact.save()

        send_mail(
            'Contact Inquiry',
            'You just got a contact inquiry from' + name + 'Please check the admin panel for the detailed message',
            'fauk514@gmail.com',
            ['anshulsaha15@gmail.com'],
            fail_silently=False 
        )

        send_mail(
            'Contact Inquiry',
            'Your contact inquiry has been recieved. I will get back to you soon',
            'fauk514@gmail.com',
            [email],
            fail_silently=False 
        )

        return redirect('index')


def searchresults(request):
    if request.method == "POST":
        search = request.POST['search']
        search = str(search)
        try:
            if "," in search:
                res = search.split(',')
                city = (res[0].upper())
                country = (res[1].upper())
                location = f'{city},{country}'
                place = city
            else:
                search = search.upper()
                location = f'{search}'
                place = location
        except:
            pass
        

        #This should be on top of the code
        try:
            import pyowm
            owm = pyowm.OWM('54c046a7b9b579e951527fc1dd8c7d1f')
            res = owm.weather_manager()
            observation = res.weather_at_place(location)
            weather = observation.weather
            temperature = weather.temperature('fahrenheit')['temp']
            temperature_in_celcius = int((temperature-32)*5/9)
            humidity = weather.humidity
            status = weather.status
            wind = ((int(weather.wind()['speed']))*3.6)
            wind_dir = int(weather.wind()['deg'])
            if wind_dir < 45:
                wind_dir = "North"
            elif 90 > wind_dir > 45:
                wind_dir = "North-East"
            elif 135 > wind_dir > 90:
                wind_dir = "East"
            elif 180 > wind_dir > 135:
                wind_dir = "South-East"
            elif 225 > wind_dir > 180:
                wind_dir = "South"
            elif 270 > wind_dir > 225:
                wind_dir = "South-West"
            elif 315 > wind_dir > 270:
                wind_dir = "West"
            elif wind_dir > 315:
                wind_dir = "North-West"
            elif wind_dir == 90:
                wind_dir = "East"
            elif wind_dir == 180:
                wind_dir = "South"
            elif wind_dir == 270:
                wind_dir = "West"
            import datetime
            now = datetime.datetime.now()
            from datetime import datetime, date
            today = date.today()
            today = str(today)
            lame =today.split('-')[2]
            date = int(lame)
            date2 = str(date)
            lame1 =today.split('-')[1]
            lame1 = int(lame1)
            months = {
                1:'Jan',
                2:'Feb',
                3:'Mar',
                4:'April',
                5:'May',
                6:'June',
                7:'July',
                8:'Aug',
                9:'Sep',
                10:'Oct',
                11:'Nov',
                12:'Dec'
            }

            month = str(months[lame1])
            day = (now.strftime("%A"))
            date = (date2 +' '+ month)
            context = {
                'day': day,
                'date':date,
                'temperature_in_celcius':temperature_in_celcius,
                'humidity':humidity,
                'wind':wind,
                'wind_dir':wind_dir,
                'place':place
            }
        except:
            messageforuser = "Invalid City Or Country !"
            context = {
                'messageforuser': messageforuser
            }
            return render(request, 'pages/index.html', context)
            
        

        return render(request, 'pages/index.html', context)
