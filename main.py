#!/usr/bin/python
# -*- coding: utf-8 -*-

from foto import maakfoto
from ftp import ftpfoto
import time,os,socket
import configparser
import dbacties
import versturen
    
#-------------------------------------------------------------------------------------------------------------
def contacttodatabase(
    contact,
    onderneming,
    naam,
    voornaam,
    email,
    nieuwsbrief,
    fotonaam
    ):

    ctodatabase(onderneming,naam,voornaam,email,contact,nieuwsbrief,fotonaam)

#-------------------------------------------------------------------------------------------------------------
def suggestiontodatabase(
    contact,
    onderneming,
    naam,
    voornaam,
    email,
    nieuwsbrief,
    fotonaam
    ):
    
    stodatabase(sql)

#-------------------------------------------------------------------------------------------------------------
def main():
	# data afkomstig van config file	
	config = configparser.ConfigParser()
	config.read('config')
	hostname = config.get("DEFAULT","c_host")
	dbbeheerder = config.get("DEFAULT","c_dbbeheerder")

	# data afkomstig van input formulier
	receiver = 'kevin.vandenbrande@voka.be'
	contact = 'Kevin Van den Brande'
	onderneming = 'ABC'
	naam = 'Vermeulen'
	voornaam = 'Joske'
	email = 'fons@fopmail.com'
	nieuwsbrief ='0'
	#hostname = socket.gethostname()
	fotonaam = hostname +  "-" + time.strftime("%Y%m%d-%H%M%S.jpg")
    
	# functie om foto te nemen
	maakfoto(fotonaam)
	
	# functie om bezoek weg te schrijven in database
	contacttodatabase(contact,onderneming,naam,voornaam,email,nieuwsbrief,fotonaam)
	
	# functie indien nieuwsbrief is aangevink om dbbeheerder en contact en anders enkel contact te verwittigen
	if nieuwsbrief == '1':
		mailtodbbeheerder(dbbeheerder,onderneming,naam,voornaam,email)
		mailcontact(receiver,contact,onderneming,naam,voornaam,email,fotonaam)
	else:
		mailcontact(receiver,contact,onderneming,naam,voornaam,email,fotonaam)

	# functie om foto op te slaan op nas
	ftpfoto(fotonaam)

	# verwijder genomen foto
	os.remove(fotonaam)



#-------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	main()
    #MyApp().run()


			
