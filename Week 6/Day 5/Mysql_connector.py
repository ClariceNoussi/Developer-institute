import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="postgre",
  passwd="Noussi4889+"
)
mycursor=mydb.cursor()
mycursor.execute('CREATE DATABASE mydatabase')

