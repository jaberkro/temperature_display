# temperature_display
Creating a weather display using Raspberry Pi, Arduino, Serial, MQTT and a LiquidCrystal display

Inspired by the Observer Pattern described in the book "Head First Design Patterns - Eric Freeman and Kathy Sierra" we decided to make an Arduino display the current feel temperature.

To practice with publishers and subscribers ourselves we used MQTT to communicate between different pieces of code on multiple devices.

In this project we have a Raspberry Pi that reads the current weather information through the OpenWeatherMap API. The temperature information will be sent to another Raspberry Pi through MQTT. This Raspberry Pi sends information to the Arduino through Serial communication. The Arduino displays the information on a LiquidCrystal display.

# OpenWeatherMap
For this project we created a free account on OpenWeatherMap. Make sure to do so as well and save your API key, we will use it later.

# Arduino:
You can follow this [tutorial](https://create.arduino.cc/projecthub/najad/interfacing-lcd1602-with-arduino-764ec4) to get the Arduino wired up to the display.

Upload this code from the Arduino IDE on your computer to the Arduino:
File->Examples->LiquidCrystal->SerialDisplay

Connect the Arduino now to the Raspberry Pi through USB

# Install MQTT and Paho
You can make this project as well on one or 2 Raspberry Pi's (or other Linux devices). Install MQTT and Paho on all devices you will use:

Install MQTT:
```
sudo apt install -y mosquitto mosquitto-clients
```
After this you should enable Mosquitto and start it: 
```
sudo systemctl enable mosquitto.service
mosquitto -v
mosquitto -d
```
Note: when mosquitto -v gives an error, you can just continue with the next steps anyways.

Install Paho:
```
sudo pip3 install paho-mqtt
```

# Raspberry Pi (subscriber):
Save the weather_subscriber.py code on this Raspberry Pi. Make sure to change the MQTT_SERVER to "your_ip_addres_of_the_raspberry_pi_server" (either localhost or the ip address of the publisher Raspberry Pi)

Turn it on with this command in your terminal on the Raspberry Pi:
```
python3 weather_subscriber.py
```

# Raspberry Pi (publisher):
Save the weather_subscriber.py code on this Raspberry Pi. Make sure to replace {your_city} with the city that is closest to you from OpenWeatherMap. Replace {your_api_key} with your API key from OpenWeatherMap.

Run the code with this command:
```
python3 weather_publisher.py
```

If everything works, your Arduino displays the current feel temperature!

