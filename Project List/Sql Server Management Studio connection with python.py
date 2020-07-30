# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 06:27:31 2020

@author: suryaam
"""

# Basic code for connecting to SSMS- SQL SERVER MANAGEMENT STUDIO
import pyodbc

## Pass the connection strings as desired. Please read the documentation for further details.
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=<Server name >;'
                      'Database=<Your specific database name which you want to connect >;'
                      'Trusted_Connection=yes;'
                      'username = <your userid>;' 
                      'password = <your password>;')

### Alternatively , if you want to connect to ssms by prompting the username and pwd at run-time, that
#can be done as follows


username=input(" Please enter your username")
password=input(" Please enter your password")

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=<Server name >;'
                      'Database=<Your specific database name which you want to connect >;'
                      'Trusted_Connection=yes;'
                      'username = username;' 
                      'password = password;')

cursor = conn.cursor()

cursor.execute('SELECT top(10) * FROM "database name"."tablename')
cursor.execute('select * FROM database.table_name)

for row in cursor:
    print(row)