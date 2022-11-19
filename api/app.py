from flask import Flask, render_template,request,jsonify
from bd import *
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/get_user',methods=['GET'])
def get_user():
    payload = []
    content = {}
    connect = conexion()
    cursor = connect.cursor()
    sql=("SELECT * FROM personas")
    cursor.execute(sql)
    for result in cursor:
        content = {'id': result[0], 'nombre': result[1], 'apellido': result[2], 'identificacion': result[3]}
        payload.append(content)
        content = {}
    return jsonify(payload)

@app.route("/user/<id>",methods=["GET"])
def user(id):
    payload = []
    content = {}
    connect = conexion()
    cursor = connect.cursor()
    sql=("SELECT  * FROM personas WHERE id=%s ")
    datos=(id,)
    cursor.execute(sql,datos)
    for result in cursor:
        content = {'id': result[0], 'nombre': result[1], 'apellido': result[2], 'identificacion': result[3]}
        payload.append(content)
        content = {}
    return jsonify(payload)


@app.route("/insert_user",methods=["POST"])
def insert_user():
    data = request.get_json(force=True)
    connect  =conexion()
    cursor = connect.cursor()
    sql="INSERT INTO personas (nombre,apellido,identificacion)  VALUES (%s,%s,%s)"
    datos=(data["nombre"],data["apellido"],data["identificacion"])
    cursor.execute(sql,datos)
    connect.commit()
    return jsonify({"Mensaje":"Registro exitoso"})

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
    app.run(debug=True)