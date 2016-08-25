#!/usr/bin/python
# _*_ coding: utf-8 _*_
#say cheese :-) 

import picamera
from time import sleep
import os

def maakfoto(fotonaam):
    #camera = picamera.PiCamera()
    #camera.capture(fotonaam)
    command='raspistill -o '+fotonaam+' -t 5 -w 800 -h 480 -n'
    os.system(command)
