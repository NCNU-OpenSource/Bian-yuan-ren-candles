#include GPIO and Timer Library 
import RPi.GPIO as GPIO
import time

class led87_object(object):
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
    for i in range(1,10000):
      self.clear()
      GPIO.output(self.ROW1, GPIO.HIGH)
      GPIO.output(self.COL1, GPIO.HIGH)
      GPIO.output(self.COL2, GPIO.HIGH)
      GPIO.output(self.COL3, GPIO.HIGH)
      GPIO.output(self.COL4, GPIO.LOW)
      GPIO.output(self.COL5, GPIO.HIGH)
      GPIO.output(self.COL6, GPIO.HIGH)
      GPIO.output(self.COL7, GPIO.HIGH)
      GPIO.output(self.COL8, GPIO.HIGH)
      time.sleep(self.sleeptime)

      self.clear()
      GPIO.output(self.ROW2, GPIO.HIGH)
      GPIO.output(self.COL1, GPIO.HIGH)
      GPIO.output(self.COL2, GPIO.HIGH)
      GPIO.output(self.COL3, GPIO.HIGH)
      GPIO.output(self.COL4, GPIO.LOW)
      GPIO.output(self.COL5, GPIO.LOW)
      GPIO.output(self.COL6, GPIO.HIGH)
      GPIO.output(self.COL7, GPIO.HIGH)
      GPIO.output(self.COL8, GPIO.HIGH)
      time.sleep(self.sleeptime)

      self.clear()
      GPIO.output(self.ROW3, GPIO.HIGH)
      GPIO.output(self.COL1, GPIO.HIGH)
      GPIO.output(self.COL2, GPIO.HIGH)
      GPIO.output(self.COL3, GPIO.LOW)
      GPIO.output(self.COL4, GPIO.LOW)
      GPIO.output(self.COL5, GPIO.LOW)
      GPIO.output(self.COL6, GPIO.LOW)
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
      GPIO.output(self.COL1, GPIO.LOW)
      GPIO.output(self.COL2, GPIO.LOW)
      GPIO.output(self.COL3, GPIO.LOW)
      GPIO.output(self.COL4, GPIO.LOW)
      GPIO.output(self.COL5, GPIO.LOW)
      GPIO.output(self.COL6, GPIO.LOW)
      GPIO.output(self.COL7, GPIO.LOW)
      GPIO.output(self.COL8, GPIO.LOW)
      time.sleep(self.sleeptime)

      self.clear()
      GPIO.output(self.ROW6, GPIO.HIGH)
      GPIO.output(self.COL1, GPIO.LOW)
      GPIO.output(self.COL2, GPIO.LOW)
      GPIO.output(self.COL3, GPIO.LOW)
      GPIO.output(self.COL4, GPIO.LOW)
      GPIO.output(self.COL5, GPIO.LOW)
      GPIO.output(self.COL6, GPIO.LOW)
      GPIO.output(self.COL7, GPIO.LOW)
      GPIO.output(self.COL8, GPIO.LOW)
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
    ledobj=led87_object()
    ledobj.demo()

if __name__ == "__main__":
    main()

