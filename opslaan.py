#!/usr/bin/python3
# -*- coding: utf-8 -*-
#takes care of the database part

import pymysql


def todatabase(sql):
    # Connect to the database
    connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             passwd='reset',
                             db='kvkaw')

try:
    with connection.cursor() as cursor:
        # Create a new record
        #cursor.execute(sql)
        cursor.execute("select Onderneming from gastenboek")
        row = cursor.fetchall()
        print (row [13])
    # connection is not autocommit by default. So you must commit to save
    # your changes.
    #connection.commit()
finally:
    connection.close()

