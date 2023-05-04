import RPi.GPIO as GPIO
import time

# GPIO-Pins für die Motoren
IN1 = 18
IN2 = 22
IN3 = 32
IN4 = 38

# GPIO-Initialisierung
GPIO.setmode(GPIO.BOARD)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

direction = int(input("Bitte geben sie die Richtung an. forward/backward: "))

if direction == forward:
    try:
        # Hauptschleife des Programms
        while True:
            GPIO.output(IN1, GPIO.HIGH)
            GPIO.output(IN2, GPIO.LOW)
            GPIO.output(IN3, GPIO.HIGH)
            GPIO.output(IN4, GPIO.LOW)

    except KeyboardInterrupt:
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.LOW)
        GPIO.cleanup()

elif direction == backward:
    try:
        # Hauptschleife des Programms
        while True:
            GPIO.output(IN1, GPIO.LOW)
            GPIO.output(IN2, GPIO.HIGH)
            GPIO.output(IN3, GPIO.LOW)
            GPIO.output(IN4, GPIO.HIGH)

    except KeyboardInterrupt:
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.LOW)
        GPIO.cleanup()

