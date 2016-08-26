#!/usr/bin/python
# -*- coding: utf-8 -*-

from versturen import sending
from opslaan import ctodatabase
from foto import maakfoto
from ftp import ftpfoto
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import time,os,socket
import configparser


#-------------------------------------------------------------------------------------------------------------
def mailtodbbeheerder(dbbeheerder,onderneming,naam,voornaam,email):
    
    # Create message container - the correct MIME type is multipart/alternative.
    subject = 'Een bezoeker wenst onze nieuwsbrief te ontvangen'  
    sender = 'Onthaal'
      
    msgRoot = MIMEMultipart('related')  
    msgRoot['Subject'] = subject
    msgRoot['From'] = sender

    html = \
            """\
            <html>
              <head></head>
              <body>
                <p>Beste,<br><br>
                   Bezoeker met onderstaande gegevens wenst onze nieuwsbrief te ontvangen.<br><br>
                   Onderneming: {onderneming} <br> Naam: {naam} <br>Voornaam: {voornaam} <br>Email: {email} <br><br><img src="cid:image1">
                </p>
               </body>
            </html>
            """.format(**locals())  

    msgText = MIMEText(html,'html')

      
    msgRoot.attach(msgText)  
      
    msg = msgRoot.as_string().encode('utf-8')

    # Send the message via SMTP server.
    sending(dbbeheerder,msg)

#-------------------------------------------------------------------------------------------------------------
def mailcontact(
    # Create the body of the message
    receiver,
    contact,
    onderneming,
    naam,
    voornaam,
    email,
    fotonaam
    ):
    
    # Create message container - the correct MIME type is multipart/alternative.
    subject = 'Uw bezoeker is toegekomen'  
    sender = 'Onthaal'
    attachement  = fotonaam
      
    msgRoot = MIMEMultipart('related')  
    msgRoot['Subject'] = subject
    msgRoot['From'] = sender

    html = \
            """\
            <html>
              <head></head>
              <body>
                <p>Beste {contact},<br><br>
                   Uw bezoeker met onderstaande gegevens is toegekomen.<br><br>
                   Onderneming: {onderneming} <br> Naam: {naam} <br>Voornaam: {voornaam} <br>Email: {email} <br><br><img src="cid:image1">
                </p>
               </body>
            </html>
            """.format(**locals())  

    msgText = MIMEText(html,'html')

      
    msgRoot.attach(msgText)  
      
    fp = open(attachement, 'rb')  
    msgImage = MIMEImage(fp.read())  
    fp.close()  
      
    msgImage.add_header('Content-ID', '<image1>')  
    msgRoot.attach(msgImage)  


    msg = msgRoot.as_string().encode('utf-8')

    # Send the message via SMTP server.
    sending(receiver,msg)

    
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


			
