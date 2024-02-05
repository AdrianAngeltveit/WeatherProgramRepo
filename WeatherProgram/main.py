import requests
import json

class WeatherClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.weatherstack.com"

    def get_current_weather(self, location):
        url = f"{self.base_url}/current?access_key={self.api_key}&query={location}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    
    def format_format_weather(self, weather_data):
        try:

            location = weather_data['location']['name']
            local_time = weather_data['location']['localtime']
            temp = weather_data['current']['temperature']
            weather_description = weather_data['current']['weather_descriptions'][0]
            wind_speed = weather_data['current']['wind_speed']
            return f"\nLocation: {location}\nLocal time: {local_time}\nTemperature: {temp}°C\nWeather description: {weather_description} \nWind speed: {wind_speed} km/h"
        
        except KeyError:
            return "Weather data is not available or invalid"
        


if __name__ == "__main__":
    client = WeatherClient("3461687bed134e51636ac4125deeae25")
    weather = client.get_current_weather("Kolltveit")
    format_weather = client.format_format_weather(weather)
    print(json.dumps(weather, indent=4), format_weather)