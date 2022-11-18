import mysql.connector

def conexion():
    return mysql.connector.connect(host='localhost',user='root',password='',db='personajes')