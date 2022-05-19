# temperature_display
Creating a weather display using Raspberry Pi, Arduino, Serial, MQTT and a LiquidCrystal display

Inspired by the Observer Pattern described in the book "Head First Design Patterns - Eric Freeman and Kathy Sierra" we decided to make an Arduino display the current feel temperature.

To practice with servers and listeners ourselves we used MQTT to communicate between different pieces of code on multiple devices.

In this project we have a Raspberry Pi that reads the current weather information through the OpenWeatherMap API. The temperature information will be sent to another Raspberry Pi through MQTT. This Raspberry Pi sends information to the Arduino through Serial communication. The Arduino displays the information on a LiquidCrystal display.

# Arduino
We used this tutorial to get the Arduino wired up to the display:
[Follow this](https://create.arduino.cc/projecthub/najad/interfacing-lcd1602-with-arduino-764ec4)

Upload this code from the Arduino IDE to your Arduino:
File->Examples->LiquidCrystal->SerialDisplay
 


