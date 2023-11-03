import mysql
import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='cherye88881'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE biodata")

print("All done!")