#!/usr/bin/python3
# -*- coding: utf-8 -*-

#installeer deze plugins eerst
#sudo pip3 install pymysql

from versturen import sending
#from opslaan import todatabase
from foto import maakfoto
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


#-------------------------------------------------------------------------------------------------------------
def mailcontact(
    # Create the body of the message
    receiver,
    contact,
    onderneming,
    naam,
    voornaam,
    email,
    ):
    
    # Create message container - the correct MIME type is multipart/alternative.
    subject = 'Uw bezoeker is toegekomen'  
    sender = 'Onthaal'
    attachement  = 'onthaal.jpg'
      
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
    receiver,
    contact,
    onderneming,
    naam,
    voornaam,
    email,
    nieuwsbrief
    ):

    # Prepare SQL query to INSERT a record into the database.
    sql = "INSERT INTO gastenboek(Datum, Onderneming, Naam, Voornaam, Email, Contact, nieuwsbrief)\
           VALUES (datetime.now(),onderneming, naam, voornaam, email, contact, nieuwsbrief)"
    todatabase(sql)
    print ('opgeslagen')

#-------------------------------------------------------------------------------------------------------------
def suggestiontodatabase(
    receiver,
    contact,
    onderneming,
    naam,
    voornaam,
    email,
    nieuwsbrief
    ):
    # which data is needed?
    # Prepare SQL query to INSERT a record into the database.
    sql = "INSERT INTO suggesties(Datum, Suggestie)\
           VALUES (datetime.now(),suggestie)"
    todatabase(sql)


#-------------------------------------------------------------------------------------------------------------
def main():

    # data afkomstig van input formulier
    receiver = 'kevin.vandenbrande@voka.be'
    contact = 'Kevin Van den Brande'
    onderneming = 'ABC'
    naam = 'Vermeulen'
    voornaam = 'Joske'
    email = 'fons@fopmail.com'

    # functie om foto te nemen

#maakfoto()

    # functie om bezoek weg te schrijven in database

'''contacttodatabase(
    'kevin.vandenbrande@voka.be',
    'Kevin Van den Brande',
    'ABC',
    'Vermeulen',
    'Joske',
    'fons@fopmail.com',
    '0',
    )
'''
    # functie indien nieuwsbrief is aangevink om database beheerder te contacteren

    # functie om contactpersoon te verwittigen via mail dat bezoeker is toegekomen

    
mailcontact(
    'kevin.vandenbrande@voka.be',
    'Kevin Van den Brande',
    'ABC',
    'Vermeulen',
    'Joske',
    'fons@fopmail.com',
    )
exit(0)
#-------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()


			
