from flask import Flask, render_template

app = Flask(__name__)

@app.route('/consumir-api', methods=["GET"])
def consumir_api():
    return render_template("index.html")

@app.route("/Mostrar-personas",methods=["GET"])
def mostrar():
    return render_template("personas.html")
    
if __name__ == "__main__":
    app.run(debug=True,port=7000)