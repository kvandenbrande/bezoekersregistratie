#!/usr/bin/python
# -*- coding: utf-8 -*-
#takes care of the database part

import pymysql.cursors

def ctodatabase(onderneming,naam,voornaam,email,contact,nieuwsbrief,fotonaam):
    
    # Connect to the database
    connection = pymysql.connect(host='127.0.0.1',user='root',passwd='reset',db='kvkaw')

    curr= connection.cursor()
    # Create a new record
    
    sql = '''INSERT INTO gastenboek(Onderneming,Naam,Voornaam,Email,Contact,Nieuwsbrief,Foto) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s)'''
    curr.execute(sql, (onderneming,naam,voornaam,email,contact,nieuwsbrief,fotonaam))

    # connection is not autocommit by default. So you must commit to save your changes.
    connection.commit()
    curr.close()
    connection.close()
