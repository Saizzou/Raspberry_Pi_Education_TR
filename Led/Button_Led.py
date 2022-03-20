#!/bin/python3

import RPi.GPIO as GPIO
import time

ledPin = 11 # Fiziksel GPIO Pin tanimi
btnPin = 12 # Fiziksel GPIO Button Pin Tanimi

def kurulum():
    GPIO.setmode(GPIO.BOARD)             # GPIO Fiziksel modunda calistirir
    GPIO.setup(ledPin, GPIO.OUT)         # GPIO Pin kurulumu
    GPIO.setup(btnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # GPIO Pinini bas kaldir moduna sokacak
    print('Kurulum basladi.')
    
def dongu():
    while True:
        if GPIO.input(btnPin) == GPIO.LOW:
            GPIO.output(ledPin, GPIO.HIGH) # Ledi yak
            print(">>> LED yaniyor")
        else: # Diger button durumu
            GPIO.output(ledPin, GPIO.LOW)
            print(">>> LED Yanmiyor")
    
    
def bitis():
    GPIO.cleanup()                       # GPIO Cikislarini sifirlar
    

if __name__ == '__main__':                # Programi baslatan Parametre
    print("PROGRAM BASLIYOR!")
    kurulum()
    try:
        dongu()
    except KeyboardInterrupt:            # Klavye ile CTRL+C müdahalesi sirasinda
        bitis()