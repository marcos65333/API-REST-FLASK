import mysql.connector

def conexion():
    return mysql.connector.connect(host='localhost',user='root',password='',db='Restuarante')

def verificar_registro(correo):
    connect = conexion()
    cursor = connect.cursor()
    sql=("SELECT correo FROM clientes WHERE correo=%s")
    cursor.execute(sql,(correo,))
    for i in cursor:
        if i[0]==correo:
            return True


