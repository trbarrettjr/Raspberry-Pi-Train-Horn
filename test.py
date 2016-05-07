from time import sleep
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)

while True:
  if ( GPIO.input(21) == False ):
    os.system('mpg321 train-horn.mp3 &')
  sleep(1);
