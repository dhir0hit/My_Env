from PyQt6.QtWidgets import QMainWindow
from bs4 import BeautifulSoup as bs
import requests

from ui.Weather.ui_weather import Ui_Weather

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/58.0.3029.110 Safari/537.3'}

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
# US english
LANGUAGE = "en-US,en;q=0.5"

class MainWindow(QMainWindow):
    def __init__(self, window):
        super(MainWindow, self).__init__()
        print("[+] Opened Password Manager Create")

        self.Window = window.Window



    def run(self):
        """
        Run the app
        add elements in app
        """
        URL = "https://www.google.com/search?lr=lang_en&ie=UTF-8&q=weather"
        import argparse

        parser = argparse.ArgumentParser(description="Quick Script for Extracting Weather data using Google Weather")
        parser.add_argument("region", nargs="?", help="""Region to get weather for, must be available region.
                                                      Default is your current location determined by your IP Address""",
                            default="")
        # parse arguments
        args = parser.parse_args()
        region = args.region
        if region:
            region = region.replace(" ", "+")
            URL += f"+{region}"
        # get data
        data = get_weather_data(URL)
        # print data
        print("Weather for:", data["region"])
        print("Now:", data["dayhour"])
        print(f"Temperature now: {data['temp_now']}°C")
        print("Description:", data['weather_now'])
        print("Precipitation:", data["precipitation"])
        print("Humidity:", data["humidity"])
        print("Wind:", data["wind"])

        self.weatherapp = Ui_Weather()
        self.weatherapp.setupUi(self.Window.current_app_container)
        self.Window.verticalLayout_7.addWidget(self.weatherapp.weather_container)

        self.weatherapp.label.setText("Wind speed is :")
        self.weatherapp.label_2.setText(data["wind"])

        self.weatherapp.label_3.setText("Humidity percentage is :")
        self.weatherapp.label_8.setText(data["humidity"])

        self.weatherapp.label_9.setText("Precipitation percentage is :")
        self.weatherapp.label_10.setText(data["precipitation"])

        self.weatherapp.label_5.setText("Today's Day and Time is :"+ data["dayhour"])
        self.weatherapp.label_4.setText("The Weather is : "+data["weather_now"])

        self.weatherapp.label_7.setText( data["temp_now"])
        self.weatherapp.label_6.setText(data["region"])







def get_weather_data(url):
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html = session.get(url)
    # create a new soup
    soup = bs(html.text, "html.parser")
    # store all results on this dictionary
    result = {}
    # extract region
    result['region'] = soup.find("div", attrs={"id": "wob_loc"}).text
    # extract temperature now
    result['temp_now'] = soup.find("span", attrs={"id": "wob_tm"}).text
    # get the day and hour now
    result['dayhour'] = soup.find("div", attrs={"id": "wob_dts"}).text
    # get the actual weather
    result['weather_now'] = soup.find("span", attrs={"id": "wob_dc"}).text
    # get the precipitation
    result['precipitation'] = soup.find("span", attrs={"id": "wob_pp"}).text
    # get the % of humidity
    result['humidity'] = soup.find("span", attrs={"id": "wob_hm"}).text
    # extract the wind
    result['wind'] = soup.find("span", attrs={"id": "wob_ws"}).text


    return result





