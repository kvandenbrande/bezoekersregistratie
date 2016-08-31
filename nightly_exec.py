#!/usr/bin/python
# -*- coding: utf-8 -*-
#night proces to exit all remaining inhouse visitors

import pymysql.cursors
import configparser

def visitor_night_exit():
    
	# Connect to the database
	config = configparser.ConfigParser()
	config.read('config')

	connection = pymysql.connect(host=config.get("DB","c_host"),user=config.get("DB","c_user"),passwd=config.get("DB","c_passwd"),db=config.get("DB","c_db"))
	
	curr= connection.cursor()

	curr.execute("UPDATE `gastenboek` SET `Buiten`= current_timestamp WHERE Buiten = '0000-00-00 00:00:00'")

	curr.close()
	connection.close()
	

visitor_night_exit()
