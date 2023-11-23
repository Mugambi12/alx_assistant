# models/weather.py

import requests
import re
from bs4 import BeautifulSoup

def get_weather(city_input, temp_format):
    CITY_URL = f"https://www.google.com/search?q=weather+{city_input}"
    response = requests.get(CITY_URL)
    soup = BeautifulSoup(response.content, "html.parser")
    temperature_element = soup.find("div", class_="BNeawe iBp4i AP7Wnd")
    City_Input = city_input.title()

    if temperature_element is None:
        return f"There is no data for {City_Input}"
    else:
        temperature_text = temperature_element.get_text()
        temperature_numeric_part = re.search(r"\d+", temperature_text).group()
        temperature_celsius = int(temperature_numeric_part)

        if temp_format == "F":
            temperature_fahrenheit = (temperature_celsius * 9/5) + 32
            degrees_format = "°F"
        else:
            temperature_fahrenheit = None
            degrees_format = "°C"

        is_hot = temperature_celsius > 32
        is_semi_hot = 28 <= temperature_celsius <= 32
        is_avg = 20 <= temperature_celsius < 28
        is_semi_cold = 15 <= temperature_celsius < 20
        is_cold = temperature_celsius < 15

        if is_hot:
            if temperature_fahrenheit is not None:
                return f"The weather in {City_Input} is quite hot at {temperature_fahrenheit:.1f} °F. Be sure to stay hydrated and protect yourself from the sun. Wearing lightweight clothing and using sunscreen is recommended."
            else:
                return f"The weather in {City_Input} is quite hot at {temperature_celsius} {degrees_format}. Be sure to stay hydrated and protect yourself from the sun. Wearing lightweight clothing and using sunscreen is recommended."
        elif is_semi_hot:
            if temperature_fahrenheit is not None:
                return f"It's warm in {City_Input} with a temperature of {temperature_fahrenheit:.1f} °F. Make sure to stay hydrated and protect yourself from the sun. Lightweight clothing and sunscreen are advised."
            else:
                return f"It's warm in {City_Input} with a temperature of {temperature_celsius} {degrees_format}. Make sure to stay hydrated and protect yourself from the sun. Lightweight clothing and sunscreen are advised."
        elif is_avg:
            if temperature_fahrenheit is not None:
                return f"{City_Input} is experiencing pleasant weather with a temperature of {temperature_fahrenheit:.1f} °F. Stay comfortable and enjoy the day!"
            else:
                return f"{City_Input} is experiencing pleasant weather with a temperature of {temperature_celsius} {degrees_format}. Stay comfortable and enjoy the day!"
        elif is_semi_cold:
            if temperature_fahrenheit is not None:
                return f"It's a bit cool in {City_Input} with a temperature of {temperature_fahrenheit:.1f} °F. Consider wearing a light jacket and staying comfortable."
            else:
                return f"It's a bit cool in {City_Input} with a temperature of {temperature_celsius} {degrees_format}. Consider wearing a light jacket and staying comfortable."
        elif is_cold:
            if temperature_fahrenheit is not None:
                return f"It's cold in {City_Input}, with temperatures around {temperature_fahrenheit:.1f} °F. Dress warmly with layered clothing to stay comfortable. Don't forget to wear a hat and gloves to keep yourself warm."
            else:
                return f"It's cold in {City_Input}, with temperatures around {temperature_celsius} {degrees_format}. Dress warmly with layered clothing to stay comfortable. Don't forget to wear a hat and gloves to keep yourself warm."
        else:
            if temperature_fahrenheit is not None:
                return f"The temperature in {City_Input} is around {temperature_fahrenheit:.1f} °F. Enjoy the pleasant weather today!"
            else:
                return f"The temperature in {City_Input} is around {temperature_celsius} {degrees_format}. Enjoy the pleasant weather today!"
