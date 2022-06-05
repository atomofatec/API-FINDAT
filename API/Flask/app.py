from flask import Flask, render_template 

app = Flask(__name__) 

@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template("home.html")

@app.route("/cursos")
def cursos():
    return render_template("cursos.html")

@app.route("/localizacao")
def localizacao():
    return render_template("localizacao.html")

@app.route("/metricas")
def metricas():
    return render_template("metricas.html")

@app.route("/vagas")
def vagas():
    return render_template("vagas.html")
