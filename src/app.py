from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/historia")
def historia():
    return render_template("historia.html")

@app.route("/plantas")
def plantas():
    return render_template("plantas.html")
    
@app.route("/escenarios")
def escenarios():
    return render_template("escenarios.html")

@app.route("/inicio")
def inicio():
    return render_template("inicio.html")

@app.route("/registro")
def registro():
    return render_template("registro.html")

@app.route("/actividades")
def actividades():
    return render_template("actividades.html")


if __name__ == "__main__":
    app.run(debug=True, port=7055)
