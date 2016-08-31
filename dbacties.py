#!/usr/bin/python
# -*- coding: utf-8 -*-
#takes care of the database part

import pymysql.cursors
import configparser

#visitor initial registration
def visitor_registration(onderneming,naam,voornaam,email,contact,nieuwsbrief,fotonaam):
    
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

#pass all active contacts
def return_contacts():
    
	# Connect to the database
	config = configparser.ConfigParser()
	config.read('config')

	connection = pymysql.connect(host=config.get("DB","c_host"),user=config.get("DB","c_user"),passwd=config.get("DB","c_passwd"),db=config.get("DB","c_db"))
	
	curr= connection.cursor()
	sql = "SELECT * FROM `contacten` WHERE Actief = 1"
	curr.execute(sql)

	for row in curr:
		print(row)

	curr.close()
	connection.close()

#visitor exit registration	
def visitor_exit(id):
    
	# Connect to the database
	config = configparser.ConfigParser()
	config.read('config')

	connection = pymysql.connect(host=config.get("DB","c_host"),user=config.get("DB","c_user"),passwd=config.get("DB","c_passwd"),db=config.get("DB","c_db"))
	
	curr= connection.cursor()

	curr.execute("UPDATE `gastenboek` SET `Buiten`= current_timestamp WHERE id = '%d' " % (id))

	curr.close()
	connection.close()
	
	
#visitors in house
def return_visitor_active():
    
	# Connect to the database
	config = configparser.ConfigParser()
	config.read('config')

	connection = pymysql.connect(host=config.get("DB","c_host"),user=config.get("DB","c_user"),passwd=config.get("DB","c_passwd"),db=config.get("DB","c_db"))
	
	curr= connection.cursor()
	sql = "SELECT * FROM `gastenboek` WHERE Buiten = '0000-00-00 00:00:00'"
	curr.execute(sql)

	for row in curr:
		print(row)

	curr.close()
	connection.close()
	

