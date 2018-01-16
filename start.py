import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(21)
    if input_state == False:
        print('Button Pressed')
        os.system("python led-candle.py")
        os.system("aplay claps.wav")
        time.sleep(0.2)
