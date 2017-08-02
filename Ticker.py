import os
import random
import urllib
import threading
import Adafruit_CharLCD as LCD

# URL for the commit messages
link = "http://whatthecommit.com/index.txt"

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDPlate()
lcdLineLimit = 16


# Print out the Message To LCD
def display():
    threading.Timer(10.0, display).start()

    # Get information from URL
    f = urllib.urlopen(link)
    message = f.read()

    if len(message) > lcdLineLimit:
        message = message[:lcdLineLimit] + os.linesep + message[lcdLineLimit:]

    # Setup the LCD for Display
    red = random.randint(0, 1)
    green = random.randint(0, 1)
    blue = random.randint(0, 1)

    if red == 0 and green == 0 and blue == 0:
        red = 1
        green = 1
        blue = 1

    lcd.set_color(red, green, blue)
    lcd.clear()
    lcd.message(message)


display()
