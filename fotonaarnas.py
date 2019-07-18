#!/usr/bin/python
# -*- coding: utf-8 -*-
#saves the photo to ftp

from ftplib import FTP

def fotoopslag(photo):

    ftp = FTP('192.168.0.123')
    ftp.login(user='', passwd ='')

    ftp.cwd('/folder/')

    ftp.storbinary('STOR' +photo, open(photo, 'rb'))
    ftp.quit()
