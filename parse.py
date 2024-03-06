import json
import requests
from datetime import datetime

from config import API_KEY


def parse_weather(city: str) -> list[dict]:
      URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
      response = json.loads(requests.get(URL).text)

      try:
            temp_c = int(response["current"]["temp_c"])
            wind_speed = response["current"]["wind_kph"]
            wind_dir = response["current"]["wind_dir"]

            match wind_dir[1:]:
                  case "N":
                        wind_dir = "Cеверный"
                  case "NE":
                        wind_dir = "Cеверо-Восточный"
                  case "E":
                        wind_dir = "Восточный"
                  case "SE":
                        wind_dir = "Юго-востоный"
                  case "S":
                        wind_dir = "Южный"
                  case "SW":
                        wind_dir = "Юго-западный"
                  case "W":
                        wind_dir = "Западный"
                  case "NW":
                        wind_dir = "Северо-западный"

            pressure = int(response["current"]["pressure_mb"])
            humidity = response["current"]["humidity"]
            local_time = datetime.now().strftime("%H:%M, %d %B %Y")

      except KeyError:
            return "Некорректное название города"

      return f"""
⛅ Погода в твоём городе: {city} | {local_time}

Температура воздуха: {temp_c}°С
Скорость ветра: {wind_speed} км/ч
Направление ветра: {wind_dir}
Давление: {pressure} мбар
Влажность: {humidity}%
"""