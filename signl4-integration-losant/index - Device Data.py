
# Based on this article: https://docs.losant.com/getting-started/boards/getting-started-with-raspberry-pi

import json
from gpiozero import LED, Button # Import GPIO library: https://gpiozero.readthedocs.io/en/stable/
from time import sleep
from losantmqtt import Device # Import Losant library: https://github.com/Losant/losant-mqtt-python

led_gpio = 23
button_gpio = 4

led = LED(led_gpio)
button = Button(button_gpio, pull_up=False)

# Construct Losant device
# device = Device("my-device-id", "my-app-access-key", "my-app-access-secret")
device = Device("5bcda0385b2d0a0007732966", "057e62f0-b547-42ee-8cfe-2150907ffada", "8a5e9b37f2be9d91df377cc2d526be35867d9dd97da517b674e0e93fb0e90c5a")

def on_command(device, command):
    print(command["name"] + " command received.")

    # Listen for the gpioControl. This name configured in Losant
    if command["name"] == "toggle":
        # toggle the LED
        led.toggle()
    if command["name"] == "switch_on":
        # toggle the LED
        led.on()
    if command["name"] == "switch_off":
        # toggle the LED
        led.off()

def sendDeviceState():
    print("Sending Device State")
    device.send_state({"button": True})

# Listen for commands.
device.add_event_observer("command", on_command)

print("Listening for device commands")

button.when_pressed = sendDeviceState # Send device state when button is pressed

# Connect to Losant and leave the connection open
device.connect(blocking=True)
