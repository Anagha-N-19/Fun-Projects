import requests

# latitude = 8.524139
# longitude = 76.936638
my_api = '********'
place = 'Delhi'
lat = float(input("Enter latitude "))
lon = float(input("Enter longitude "))
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={my_api}")
data = response.json()
print(data)
weather_descr = data['weather'][0]['description']
current_temp = data['main']['temp']
humidity = data['main']['humidity']
print("Weather description:", weather_descr)
print("Current temperature in Celsius:", round(-273.15 + current_temp, 1))
print("Humidity:", humidity)
