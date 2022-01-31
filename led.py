import RPi.GPIO as GPIO
import sys ,time

r = 13 #red

GPIO.setmode(GPIO.BOARD)

GPIO.setup(r, GPIO.OUT)

while True :
    
    GPIO.output(r, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(r, GPIO.LOW)
    time.sleep(0.5)

