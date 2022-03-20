#!/bin/python3

import RPi.GPIO as GPIO
import time

ledPin = 11 # Fiziksel GPIO Pin tanimi
btnPin = 12 # Fiziksel GPIO Button Pin Tanimi
ledDurum = False    # Led Yanmiyor durumu

def kurulum():
    GPIO.setmode(GPIO.BOARD)             # GPIO Fiziksel modunda calistirir
    GPIO.setup(ledPin, GPIO.OUT)         # GPIO Pin kurulumu
    GPIO.setup(btnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # GPIO Pinini bas kaldir moduna sokacak
    print('Kurulum basladi.')
    
def butonIslem(channel): # Buttona basildiginda bu fonksiyon calisacaktir
    global ledDurum
    print('Buton Islem GPIO Durumu:%d' %channel)
    ledDurum = not ledDurum   # Her tiklamada durumu tersine cevirecek (AC/KAPA = TRUE/FALSE)
    
    if ledDurum:
        print("Led Acik")
    else:
        print("Led Kapali")
    
    GPIO.output(ledPin, ledDurum)
    
def dongu():
    GPIO.add_event_detect(btnPin, GPIO.RISING, callback=butonIslem, bouncetime=200) # Buttona basiliyor mu islemi icin kontrol döngüsü (GPIO.FALLING)
    while True:
        pass # Programin acik kalmasini saglayan sonsuz pass döngüsü
    
    
def bitis():
    GPIO.cleanup()                       # GPIO Cikislarini sifirlar
    

if __name__ == '__main__':                # Programi baslatan Parametre
    print("PROGRAM BASLIYOR!")
    kurulum()
    try:
        dongu()
    except KeyboardInterrupt:            # Klavye ile CTRL+C müdahalesi sirasinda
        bitis()
