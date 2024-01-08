import requests
from bs4 import BeautifulSoup
import json


def get_response(msg):
    """
    This function will return a response based on the message text.

    can be extended to use machine learning or other AI concepts to generate sophisticated responses
    this is the bare minimum.
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

        return "test"

    return "test"
