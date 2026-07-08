import requests
import os
from dotenv import load_dotenv
from typing import Final


load_dotenv()
api_weather_key : Final = os.getenv('weather_token')
def get_weather(city):
            api_key = os.getenv('weather_token')
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_weather_key}&units=metric"
            try : 
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                data = response.json()
                # print(data)
                if data["cod"] == 200 :
                    weather = (
                        f"🌍 Weather in {data['name']}\n"
                        f"🌡 Temperature: {data['main']['temp']}°C\n"
                        f"☁️ Condition: {data['weather'][0]['description']}"
                        )

                    return weather
                    
            except requests.exceptions.HTTPError : 
                match response.status_code :
                    case 400 :
                        return "❌ City not found"
                        
            except requests.exceptions.RequestException as e:
                return f"❌ Connection error: {e}"