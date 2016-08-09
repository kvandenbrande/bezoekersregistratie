#!/usr/bin/python3
# -*- coding: utf-8 -*-
#takes care of the mailing part

import smtplib

def sending(receiver,message):

    sender = 'info.aw@voka.be'

    s = smtplib.SMTP('195.85.246.107')
    s.sendmail(sender, receiver, message)
    s.quit()
    print ('Successfully sent email')

