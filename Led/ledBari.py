#!/bin/python3

import RPi.GPIO as GPIO
import time

ledPin = [3, 5, 11, 12, 13, 35, 16, 18, 22, 24] # Fiziksel GPIO Pin tanimi

def kurulum():
    GPIO.setmode(GPIO.BOARD)             # GPIO Fiziksel modunda calistirir
    GPIO.setup(ledPin, GPIO.OUT)         # GPIO Pin kurulumu
    GPIO.output(ledPin, GPIO.HIGH)       # Tüm ledleri söndürmek icin Yüksek Frekans
    print('Kurulum basladi.')
    
def dongu():
    while True:
        for pin in ledPin:
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.1)
        for pin in ledPin:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.1)
    
def bitis():
    GPIO.cleanup()                       # GPIO Cikislarini sifirlar
    

if __name__ == '__main__':                # Programi baslatan Parametre
    print("PROGRAM BASLIYOR!")
    kurulum()
    try:
        dongu()
    except KeyboardInterrupt:            # Klavye ile CTRL+C müdahalesi sirasinda
        bitis()
