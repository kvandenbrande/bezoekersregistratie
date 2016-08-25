#!/usr/bin/python
# -*- coding: utf-8 -*-
#takes care of the database part

import pymysql.cursors
import configparser

def ctodatabase(onderneming,naam,voornaam,email,contact,nieuwsbrief,fotonaam):
    
   # Connect to the database
   config = configparser.ConfigParser()
	config.read('config')

	connection = pymysql.connect(host=config.get("DB","c_host"),user=config.get("DB","c_user"),passwd=config.get("DB","c_passwd"),db=config.get("DB","c_db"))
	
	curr= connection.cursor()
	# Create a new record
	 
	sql = '''INSERT INTO gastenboek(Onderneming,Naam,Voornaam,Email,Contact,Nieuwsbrief,Foto) \
	                 VALUES (%s, %s, %s, %s, %s, %s, %s)'''
	curr.execute(sql, (onderneming,naam,voornaam,email,contact,nieuwsbrief,fotonaam))
	
	# connection is not autocommit by default. So you must commit to save your changes.
	connection.commit()
	curr.close()
	connection.close()
