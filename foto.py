#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#say cheese :-) 

import picamera
from time import sleep

def maakfoto():
    camera = picamera.PiCamera()
    camera.capture('onthaal.jpg')
