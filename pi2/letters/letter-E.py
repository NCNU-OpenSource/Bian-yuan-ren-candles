#include GPIO and Timer Library 
import RPi.GPIO as GPIO
import time
import sys
import os, threading, signal

class ledE_object(object):
  def __init__(self):
    #define Raspberry Pi GPIO number
    self.sleeptime=0.001
    self.ROW1=22
    self.ROW2=18
    self.ROW3=16
    self.ROW4=35
    self.ROW5=33
    self.ROW6=31
    self.ROW7=29
    self.COL1=38
    self.COL2=36
    self.COL3=32
    self.COL4=37
    self.COL5=15
    self.COL6=13
    self.COL7=11
    self.COL8=7
    self.buttonPin = 40
    self.buttonMusic = 12

    #Raspberry Pi GPIO initalization
    GPIO.setmode( GPIO.BOARD )
    GPIO.setup(self.COL1, GPIO.OUT)
    GPIO.setup(self.COL2, GPIO.OUT)
    GPIO.setup(self.COL3, GPIO.OUT)
    GPIO.setup(self.COL4, GPIO.OUT)
    GPIO.setup(self.COL5, GPIO.OUT)
    GPIO.setup(self.COL6, GPIO.OUT)
    GPIO.setup(self.COL7, GPIO.OUT)
    GPIO.setup(self.COL8, GPIO.OUT)
    GPIO.setup(self.ROW1, GPIO.OUT)
    GPIO.setup(self.ROW2, GPIO.OUT)
    GPIO.setup(self.ROW3, GPIO.OUT)
    GPIO.setup(self.ROW4, GPIO.OUT)
    GPIO.setup(self.ROW5, GPIO.OUT)
    GPIO.setup(self.ROW6, GPIO.OUT)
    GPIO.setup(self.ROW7, GPIO.OUT)
    
    GPIO.setup(self.buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(self.buttonMusic, GPIO.IN, pull_up_down=GPIO.PUD_UP)

  def clear(self):
    #set all GPIO output to LOW
    GPIO.output(self.COL1, GPIO.LOW)
    GPIO.output(self.COL2, GPIO.LOW)
    GPIO.output(self.COL3, GPIO.LOW)
    GPIO.output(self.COL4, GPIO.LOW)
    GPIO.output(self.COL5, GPIO.LOW)
    GPIO.output(self.COL6, GPIO.LOW)
    GPIO.output(self.COL7, GPIO.LOW)
    GPIO.output(self.COL8, GPIO.LOW)
    GPIO.output(self.ROW1, GPIO.LOW)
    GPIO.output(self.ROW2, GPIO.LOW)
    GPIO.output(self.ROW3, GPIO.LOW)
    GPIO.output(self.ROW4, GPIO.LOW)
    GPIO.output(self.ROW5, GPIO.LOW)
    GPIO.output(self.ROW6, GPIO.LOW)
    GPIO.output(self.ROW7, GPIO.LOW)

  def demo(self):
    def close(channel):
        os.system("python ~/Bian-yuan-ren-candles/led-cleanup.py")
        for line in os.popen("ps ax | grep wav | grep -v grep"):
            fields = line.split()
            pid = fields[0]
            os.kill(int(pid), signal.SIGKILL)
        sys.exit()

    def playmusic():
        print("play music")
        os.system("aplay ~/Bian-yuan-ren-candles/pi2/music/englishHB.wav")

    def callback(channel):
        thd.start()

    thd = threading.Thread(target=playmusic, name='thd1')

    GPIO.add_event_detect(self.buttonMusic, GPIO.RISING, callback=callback)
    GPIO.add_event_detect(self.buttonPin, GPIO.RISING, callback=close)

    while 1:
      self.clear()
      GPIO.output(self.ROW1, GPIO.HIGH)
      GPIO.output(self.COL1, GPIO.HIGH)
      GPIO.output(self.COL2, GPIO.LOW)
      GPIO.output(self.COL3, GPIO.LOW)
      GPIO.output(self.COL4, GPIO.LOW)
      GPIO.output(self.COL5, GPIO.LOW)
      GPIO.output(self.COL6, GPIO.LOW)
      GPIO.output(self.COL7, GPIO.LOW)
      GPIO.output(self.COL8, GPIO.HIGH)
      time.sleep(self.sleeptime)

      self.clear()
      GPIO.output(self.ROW2, GPIO.HIGH)
      GPIO.output(self.COL1, GPIO.HIGH)
      GPIO.output(self.COL2, GPIO.LOW)
      GPIO.output(self.COL3, GPIO.HIGH)
      GPIO.output(self.COL4, GPIO.HIGH)
      GPIO.output(self.COL5, GPIO.HIGH)
      GPIO.output(self.COL6, GPIO.HIGH)
      GPIO.output(self.COL7, GPIO.HIGH)
      GPIO.output(self.COL8, GPIO.HIGH)
      time.sleep(self.sleeptime)

      self.clear()
      GPIO.output(self.ROW3, GPIO.HIGH)
      GPIO.output(self.COL1, GPIO.HIGH)
      GPIO.output(self.COL2, GPIO.LOW)
      GPIO.output(self.COL3, GPIO.HIGH)
      GPIO.output(self.COL4, GPIO.HIGH)
      GPIO.output(self.COL5, GPIO.HIGH)
      GPIO.output(self.COL6, GPIO.HIGH)
      GPIO.output(self.COL7, GPIO.HIGH)
      GPIO.output(self.COL8, GPIO.HIGH)
      time.sleep(self.sleeptime)

      self.clear()
      GPIO.output(self.ROW4, GPIO.HIGH)
      GPIO.output(self.COL1, GPIO.HIGH)
      GPIO.output(self.COL2, GPIO.LOW)
      GPIO.output(self.COL3, GPIO.LOW)
      GPIO.output(self.COL4, GPIO.LOW)
      GPIO.output(self.COL5, GPIO.LOW)
      GPIO.output(self.COL6, GPIO.LOW)
      GPIO.output(self.COL7, GPIO.LOW)
      GPIO.output(self.COL8, GPIO.HIGH)
      time.sleep(self.sleeptime)

      self.clear()
      GPIO.output(self.ROW5, GPIO.HIGH)
      GPIO.output(self.COL1, GPIO.HIGH)
      GPIO.output(self.COL2, GPIO.LOW)
      GPIO.output(self.COL3, GPIO.HIGH)
      GPIO.output(self.COL4, GPIO.HIGH)
      GPIO.output(self.COL5, GPIO.HIGH)
      GPIO.output(self.COL6, GPIO.HIGH)
      GPIO.output(self.COL7, GPIO.HIGH)
      GPIO.output(self.COL8, GPIO.HIGH)
      time.sleep(self.sleeptime)

      self.clear()
      GPIO.output(self.ROW6, GPIO.HIGH)
      GPIO.output(self.COL1, GPIO.HIGH)
      GPIO.output(self.COL2, GPIO.LOW)
      GPIO.output(self.COL3, GPIO.HIGH)
      GPIO.output(self.COL4, GPIO.HIGH)
      GPIO.output(self.COL5, GPIO.HIGH)
      GPIO.output(self.COL6, GPIO.HIGH)
      GPIO.output(self.COL7, GPIO.HIGH)
      GPIO.output(self.COL8, GPIO.HIGH)
      time.sleep(self.sleeptime)

      self.clear()
      GPIO.output(self.ROW7, GPIO.HIGH)
      GPIO.output(self.COL1, GPIO.HIGH)
      GPIO.output(self.COL2, GPIO.LOW)
      GPIO.output(self.COL3, GPIO.LOW)
      GPIO.output(self.COL4, GPIO.LOW)
      GPIO.output(self.COL5, GPIO.LOW)
      GPIO.output(self.COL6, GPIO.LOW)
      GPIO.output(self.COL7, GPIO.LOW)
      GPIO.output(self.COL8, GPIO.HIGH)
      time.sleep(self.sleeptime)
      
    self.clear()    

def main():
    ledobj=ledE_object()
    ledobj.demo()

if __name__ == "__main__":
    main()

