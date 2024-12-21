import requests

# city = input("")
api_key = '61c19192827181c777f83424e9b9c48b'
city_id = 524901

try:
    res = requests.get('http://api.openweathermap.org/data/2.5/weather',
                       params={'id': city_id, 'lang': 'ru', 'units': 'metric', 'APPID': api_key})
    data = res.json()

    print("Город:", data['name'])
    print("Погода:", data['weather'][0]['description'])
    print("Температура:", data['main']['temp'])

except Exception as e:
    print("Exception (weather):", e)
    pass

