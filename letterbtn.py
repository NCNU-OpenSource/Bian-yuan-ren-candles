import RPi.GPIO as GPIO
import time
import os 
import signal 

class letterbnt_object(object):
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.buttonPin = 21
        GPIO.setup(self.buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        self.click = 0

    def demo(self):
        while True:
            input_state = GPIO.input(self.buttonPin)
            if input_state == False:
                self.click = self.click + 1
                if self.click == 1:
    	            os.system("python led-cleanup.py")
    	            os.system("python letter-C.py")
                if self.click == 2:
                    os.system("python led-cleanup.py")
    	            os.system("python letter-E.py")
                if self.click == 3:
    	            os.system("python led-cleanup.py")
    	            os.system("python letter-J.py")
                if self.click == 4:
    	            os.system("python led-cleanup.py")
                    os.system("python letter-K.py")
                    self.click = 0
            time.sleep(0.2)

def main():
    ledobj=letterbnt_object()
    ledobj.demo()

if __name__ == "__main__":
    main()
