#!/usr/bin/python
# -*- coding: utf-8 -*-
#takes care of saving the photo to NAS02

import ftplib
import configparser

def ftpfoto(fotonaam):
	config = configparser.ConfigParser()
	config.read('config')
	
	ftp=ftplib.FTP(config.get("FTP","c_host"))
	ftp.login(config.get("FTP","c_user"),config.get("FTP","c_passwd"))
	ftp.cwd(config.get("FTP","c_dir"))
	ftp.storbinary("STOR " + fotonaam, open(fotonaam,'rb'), 1024)
	ftp.quit()
