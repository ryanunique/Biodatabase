import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='cherye88881'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE thingkingzombie")

print("All done!")