# Creating a script that gets your day going via email.
# Sends Weather and Calendar Meetings

import json
import requests

weather_api_key = "7abc9a643ec0a91b1e604ce98f51501c"
weather_url = "http://api.openweathermap.org/data/2.5/weather?"
my_city = "Providence"
full_url = weather_url + "appid=" + weather_api_key + "&q=" + my_city

# Create: Function - get weather
def get_weather():
    response = requests.get(full_url)
    x = response.json()
    temperature = x["main"]["temp"]
    converted_temp = 1.8 * (temperature - 273) + 32
    converted_temp = round(converted_temp,2)
    print("Current Temperature: " + str(converted_temp))
# Create: Function - get schedule


# Create Function - send email

get_weather()