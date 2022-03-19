#!/bin/python3

import RPi.GPIO as GPIO
import time

ledPin = 11 # Fiziksel GPIO Pin tanimi

def kurulum():
    GPIO.setmode(GPIO.BOARD)             # GPIO Fiziksel modunda calistirir
    GPIO.setup(ledPin, GPIO.OUT)         # GPIO Pin kurulumu
    GPIO.output(ledPin, GPIO.LOW)        # Pin Düsük Frekansta baslasin
    print('Kurulum basladi. Kurulan pin: %d' %ledPin)
    
def dongu():
    while True:
        GPIO.output(ledPin, GPIO.HIGH)       # Led Pin Frekansini yukselt
        print(">>> LED Acilmistir!")
        time.sleep(1)
        GPIO.output(ledPin, GPIO.LOW)        # Led Pin Frekansini düsür
        print(">>> LED Kapanmistir!")
        time.sleep(1)
    
    
def bitis():
    GPIO.cleanup()                       # GPIO Cikislarini sifirlar
    

if __name__ == '__main__':                # Programi baslatan Parametre
    print("PROGRAM BASLIYOR!")
    kurulum()
    try:
        dongu()
    except KeyboardInterrupt:            # Klavye ile CTRL+C müdahalesi sirasinda
        bitis()