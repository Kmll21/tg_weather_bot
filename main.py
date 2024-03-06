import json
import requests
from datetime import datetime

from config import API_KEY


city = "Kazan"
URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"


response = json.loads(requests.get(URL).text)

temp_c = response["current"]["temp_c"]
local_time = datetime.now().strftime("%H:%M, %d %B")

print(f"""
      Город: {city}
      Время: {local_time}
      Температура: {temp_c}
      """)