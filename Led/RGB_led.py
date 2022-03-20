#!/bin/python3

import RPi.GPIO as GPIO
import time
import random

ledPin = [11, 12, 13] # Fiziksel GPIO Pin tanimi 

def kurulum():
    global pwmK, pwmY, pwmM
    GPIO.setmode(GPIO.BOARD)             # GPIO Fiziksel modunda calistirir
    GPIO.setup(ledPin, GPIO.OUT)         # GPIO Pin kurulumu
    GPIO.output(ledPin, GPIO.HIGH)        # Pin Düsük Frekansta baslasin
    pwmK = GPIO.PWM(ledPin[0], 2000)
    pwmY = GPIO.PWM(ledPin[1], 2000)
    pwmM = GPIO.PWM(ledPin[2], 2000)
    pwmK.start(0)
    pwmY.start(0)
    pwmM.start(0)
    
def renk_ayar(k_deg, y_deg, m_deg):        # Renk Ayarlamasini RGB degerinin Frekansini ayarlayan fonksiyon
    pwmK.ChangeDutyCycle(k_deg)
    pwmY.ChangeDutyCycle(y_deg)
    pwmM.ChangeDutyCycle(m_deg)
    
def dongu():
    while True:
        k = random.randint(0,100)
        y = random.randint(0,100)
        m = random.randint(0,100)
        renk_ayar(k, y, m)
        print('k=%d, y=%d, m=%d' %(k, y, m))
        time.sleep(2)
    
    
def bitis():
    pwmK.stop()
    pwmY.stop()
    pwmM.stop()
    GPIO.cleanup()                       # GPIO Cikislarini sifirlar
    

if __name__ == '__main__':                # Programi baslatan Parametre
    print("PROGRAM BASLIYOR!")
    kurulum()
    try:
        dongu()
    except KeyboardInterrupt:            # Klavye ile CTRL+C müdahalesi sirasinda
        bitis()
