import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
button = 6
GPIO.setup(button, GPIO.IN)

while True:
    GPIO.output(led, not GPIO.input(button))