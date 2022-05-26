# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 21:21:20 2022

@author: Dewo
"""

import mysql.connector as sql_db
mydb = sql_db.connect(
    user = 'root',
    passwd = 'Buatapaan',
    host = '127.0.0.1',
    database = 'sakila'
    )

cursor = mydb.cursor()
mysql = "SELECT * FROM country"



cursor.execute(mysql)
result = cursor.fetchall()
for row in result:
    print(row)