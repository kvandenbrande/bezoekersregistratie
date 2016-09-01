#!/usr/bin/python3
# -*- coding: utf-8 -*-
#takes care of the mailing part

import smtplib,os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

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


def sending(receiver,message):

    sender = 'info.aw@voka.be'

    s = smtplib.SMTP('195.85.246.107')
    s.sendmail(sender, receiver, message)
    s.quit()


