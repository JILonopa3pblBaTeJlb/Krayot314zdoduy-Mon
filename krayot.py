import asyncio
import re
import requests
from bs4 import BeautifulSoup
import telegram
import pytz
import datetime

def is_working_hours():
    tz = pytz.timezone("Asia/Jerusalem")
    now = datetime.datetime.now(tz)
    return now.hour >= 5 and now.hour < 20

async def send_weather_info():
    bot = telegram.Bot(token="YOUR_TOKEN")
    chat_id = "YOUR_CHAT_ID"
    url = "https://www.surfo.co.il/%D7%9E%D7%96%D7%92-%D7%90%D7%95%D7%95%D7%99%D7%A8"

    while True:
        if is_working_hours():
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            
            weather_element = soup.select_one(".w_line.firstline")
            if weather_element:
                weather_text = weather_element.get_text()
                numbers = re.findall(r'\d+', weather_text)
                if len(numbers) >= 5:
                    wind_direction = numbers[2][:3]
                    wind_speed = numbers[2][3:].lstrip("0")
                    max_wind_speed = numbers[3]
                    temperature = numbers[4]

                    if 22 <= int(wind_direction) <= 66:
                        wind_direction = "\U00002199"
                    elif 67 <= int(wind_direction) <= 110:
                        wind_direction = "\U00002B05"
                    elif 111 <= int(wind_direction) <= 154:
                        wind_direction = "\U00002196"
                    elif 155 <= int(wind_direction) <= 198:
                        wind_direction = "\U00002B06"
                    elif 199 <= int(wind_direction) <= 242:
                        wind_direction = "\U00002197"
                    elif 243 <= int(wind_direction) <= 286:
                        wind_direction = "\U000027A1"
                    elif 287 <= int(wind_direction) <= 335:
                        wind_direction = "\U00002B07"
                    else:
                        wind_direction = "\U00002B07"



                    weather_text = f"{wind_direction}{wind_speed}\u2212{max_wind_speed}\U0001F321{temperature}\U000000BA"
                    await bot.send_message(chat_id=chat_id, text=weather_text)
                else:
                    await bot.send_message(chat_id=chat_id, text="Not enough numbers found.")
            else:
                await bot.send_message(chat_id=chat_id, text="Element not found.")
        else:
            await asyncio.sleep(3600)
        
        await asyncio.sleep(300)  # wait 5 minutes

asyncio.run(send_weather_info())
