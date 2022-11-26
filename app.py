from flask import Flask, render_template,request,jsonify
from bd import *
from flask_cors import CORS,cross_origin
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
CORS(app)
app.secret_key = 'daniel123'

@app.route('/comidas',methods=['GET'])
def get_user():
    payload = []
    content = {}
    connect = conexion()
    cursor = connect.cursor()
    sql=("SELECT * FROM menu")
    cursor.execute(sql)
    for result in cursor:
        content = {'id': result[0], 'nombre': result[1]}
        payload.append(content)
        content = {}
    return jsonify(payload)

@app.route('/contacto',methods=['GET'])
def contacto():
    payload = []
    content = {}
    connect = conexion()
    cursor = connect.cursor()
    sql=("SELECT * FROM contacto")
    cursor.execute(sql)
    for result in cursor:
        content = {'id': result[0], 'nombre': result[1], 'apellido':result[2],'correo':result[3],'telefono':result[4],'mensaje':result[5]}
        payload.append(content)
        content = {}
    return jsonify(payload)

@app.route('/bebidas',methods=['GET'])
def bebidas():
    payload = []
    content = {}
    connect = conexion()
    cursor = connect.cursor()
    sql=("SELECT * FROM bebidas")
    cursor.execute(sql)
    for result in cursor:
        content = {'id': result[0], 'nombre': result[1]}
        payload.append(content)
        content = {}
    return jsonify(payload)


@app.route("/user/<id>",methods=["GET"])
def user(id):
    payload = []
    content = {}
    connect = conexion()
    cursor = connect.cursor()
    sql=("SELECT  * FROM clientes WHERE id= %s ")
    datos=(id,)
    cursor.execute(sql,datos)
    for result in cursor:
        content = {'id': result[0], 'nombre': result[1], 'apellido': result[2]}
        payload.append(content)
        content = {}
    return jsonify(payload)

@cross_origin()
@app.route("/insert_user",methods=["POST"])
def insert_user():
    try:
        data = request.get_json(force=True)
        if verificar_registro(data["correo"])!=True:
            connect  =conexion()
            cursor = connect.cursor()
            print(data)
            sql="INSERT INTO clientes (nombre,apellido,cedula, correo, contraseña,telefono)  VALUES (%s,%s,%s,%s,%s,%s)"
            datos=(data["nombre"],data["apellido"], data["cedula"], data["correo"], data["contraseña"], data["telefono"])
            cursor.execute(sql,datos)
            connect.commit()
            return jsonify({"Mensaje":"Registro exitoso"})
        else:
            return jsonify({"error":"Ya esta registrado"})
    except Exception as ex:
        print(ex)

@cross_origin()
@app.route("/enviar-mensaje",methods=["POST"])
def sent_message():
 
    data = request.get_json(force=True)
    connect  =conexion()
    cursor = connect.cursor()
    print(data)
    sql="INSERT INTO contacto (nombre,apellido, correo, telefono,mensaje)  VALUES (%s,%s,%s,%s,%s)"
    datos=(data["nombre"],data["apellido"], data["correo"], data["telefono"],  data["mensaje"])
    cursor.execute(sql,datos)
    connect.commit()
    return jsonify({"Mensaje":"Mensaje recibido exitoso, pronto recibira un correo·"})

@app.route("/update/<id>",methods=["PUT"])
def update_user(id):
    data = request.get_json(force=True)
    connect  =conexion()
    cursor = connect.cursor()
    sql="UPDATE  personas SET nombre =%s, apellido =%s, identificacion=%s WHERE id =%s"
    datos=(data["nombre"],data["apellido"],data["identificacion"],id)
    cursor.execute(sql,datos)
    connect.commit()
    return jsonify({"Mensaje":"Registro actualizado correctamente"})


@app.route("/verificar_user",methods=["POST"])
def verificar_user():
    payload = []
    content = {}
    data = request.get_json(force=True)
    connect  =conexion()
    cursor = connect.cursor()
    sql="SELECT  correo,contraseña,rol,id FROM clientes  WHERE correo =%s "
    datos=(data["correo"],)
    cursor.execute(sql,datos)
    for datos in cursor:
       if datos[0]==data['correo'] and datos[1]==data['contraseña']:
         content =  {'correo':datos[0], 'contraseña':datos[1], 'rol':datos[2],'id':datos[3]}
         payload.append(content)
         return (payload)
    return jsonify({"error":"contraseña invalida"})

@app.route('/delete_user/<id>',methods=["DELETE"])
def delete_user(id):
    connect  =conexion()
    cursor = connect.cursor()
    sql = ("DELETE from personas WHERE id=%s")
    datos=(id,)
    cursor.execute(sql,datos)
    connect.commit()
    return jsonify({"Mensaje":"Usuario eliminado correctamente"})

if __name__ == "__main__":
    app.run(debug=True,port=7000)