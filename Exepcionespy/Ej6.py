import mysql.connector
from mysql.connector import Error

cnx = mysql.connector.connect(user='bdi', password='pepe1234', host='127.0.0.1', database='Cantantes')
cursor = cnx.cursor()
try:
    add_cantante = ("INSERT INTO cantante " "(dni, nombre)""VALUES (%s, %s)")

    data_cantante = (33457892, 'Ricardo Moroni')

    cursor.execute(add_cantante, data_cantante)
    cnx.commit()
    
except mysql.connector.errors.IntegrityError:
    print("Hay un problema en insertar un cantante")
cursor.close()
cnx.close()
