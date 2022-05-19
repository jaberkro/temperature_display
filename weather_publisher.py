import json
import sys
import paho.mqtt.publish as publish
import os

MQTT_SERVER = "localhost"
MQTT_PATH = "weather"
url = 'curl "https://api.openweathermap.org/data/2.5/weather?q={your_city}&appid={your_api_key}&units=metric"'

publish.single(MQTT_PATH, json.loads(os.popen(url).read())['main']['feels_like'], hostname=MQTT_SERVER)
