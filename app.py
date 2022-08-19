import mysql.connector
import os

mydb = mysql.connector.connect(
  host= os.environ['MYSQL_HOST'],
  user= os.environ['MYSQL_USERNAME'],
  password= os.environ['MYSQL_PASSWORD']
)

print(mydb)
