#!/bin/python3

import RPi.GPIO as GPIO
import time

ledPin = 12 # Fiziksel GPIO Pin tanimi

def kurulum():
    global p
    GPIO.setmode(GPIO.BOARD)             # GPIO Fiziksel modunda calistirir
    GPIO.setup(ledPin, GPIO.OUT)         # GPIO Pin kurulumu
    GPIO.output(ledPin, GPIO.LOW)        # Pin Düsük Frekansta baslasin
    
    #PWM
    p = GPIO.PWM(ledPin, 500)            # PWM Frekansini 500Hz
    p.start(0)                           # Baslangic Frekansini 0a tanimlar.
    
    print('Kurulum basladi. Kurulan pin: %d' %ledPin)
    
def dongu():
    global p
    while True:
        for dc in range(0,101,1):         # LED Aydinligini yukselt
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)
        time.sleep(1)
        for dc in range(100,-1,-1):       # LED Aydinligini alcalt
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)
        time.sleep(1)
    
def bitis():
    p.stop()                              # PWM Baslangicini durdur
    GPIO.cleanup()                       # GPIO Cikislarini sifirlar
    

if __name__ == '__main__':                # Programi baslatan Parametre
    print("PROGRAM BASLIYOR!")
    kurulum()
    try:
        dongu()
    except KeyboardInterrupt:            # Klavye ile CTRL+C müdahalesi sirasinda
        bitis()
