import requests
from bs4 import BeautifulSoup
import json


def get_response(msg):
    """
    This function will return a response based on the message text.

    can be extended to use machine learning or other AI concepts to generate sophisticated responses.
    """

    if msg == "/start":
        return "Hello there, welcome to our bot, please send a message to get started"

    if msg == "/help":
        return "Hello there, I can help you getting information about the weather in your city, just send me /weather and I will reply with the weather information for Oxford, Zurich and Freiburg"

    if msg == "/weather":
        urls = [
            "https://www.wetter.com/wetter_aktuell/wettervorhersage/16_tagesvorhersage/vereinigtes-koenigreich/oxford/GB0KJ1109.html",
            "https://www.wetter.com/wetter_aktuell/wettervorhersage/16_tagesvorhersage/schweiz/zuerich/CH0CH4503.html",
            "https://www.wetter.com/wetter_aktuell/wettervorhersage/16_tagesvorhersage/deutschland/freiburg-im-breisgau/DE0003016.html",
        ]
        locations = ["Oxford, UK", "Zurich, Switzerland", "Freiburg, Germany"]

        assembled_weather_info = {
            "Oxford, UK": 0,
            "Zurich, Switzerland": 1,
            "Freiburg, Germany": 2,
        }

        for i, url in enumerate(urls):
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")

            if url.startswith("https://www.wetter.com/"):
                # print("wetter.com")
                # Extract the current weather information
                if response.status_code == 200:
                    # Parse the HTML content with BeautifulSoup
                    soup = BeautifulSoup(response.content, "html.parser")

                    ## Extract the current weather information

                    # Find the div with the class "info-weather"
                    info_weather_div = soup.select_one(".info-weather")

                    # Extract temperature
                    temperature = info_weather_div.select_one(".rtw_temp").text.strip()

                    # Extract weather description
                    weather_description = info_weather_div.select_one(
                        ".rtw_weather_txt"
                    ).text.strip()

                    # extract detailed weather description
                    weather_element = soup.find(
                        "div",
                        class_="[ layout__item desk-one-third portable-one-whole ] [ portable-mb ]",
                    )

                    # Extract the text content
                    weather_text = weather_element.get_text(strip=True)

                    # set location
                    location = locations[i]

                    ## Extract the forecast

                    # Find all anchor tags inside the forecast-navigation-grid div
                    forecast_days = soup.find(
                        "div",
                        class_="[ forecast-navigation-grid ]",
                    )

                    if forecast_days:
                        days = forecast_days.find_all("a")

                    for day in days:
                        div_element = day.select_one("div")
                        if div_element:
                            date = div_element.text.strip()
                            max_temp = day.select_one(
                                ".forecast-navigation-temperature-max"
                            ).text.strip("°")
                            min_temp = day.select_one(
                                ".forecast-navigation-temperature-min"
                            ).text.strip("°")

                        # print(
                        #    f"Date: {date}, Max Temperature: {max_temp}°C, Min Temperature: {min_temp}°C"
                        # )
                    return tuple(
                        string.encode("latin1").decode("unicode_escape")
                        for string in (
                            "Current Weather in",
                            location,
                            "Temperature:",
                            temperature,
                            "Weather Description:",
                            weather_description,
                            weather_text,
                            f"Date: {date}, Max Temperature: {max_temp}°C, Min Temperature: {min_temp}°C",
                        )
                    )

                else:
                    return "Failed to retrieve content. Status code: {response.status_code}"
