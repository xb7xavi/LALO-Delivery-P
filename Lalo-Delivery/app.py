import os
import flask
from flask import request, render_template
from flask_api import FlaskAPI

DEBUG = True

# Se configura FlaskAPI
app = FlaskAPI(__name__)


# DASHBOARD (Front-End de la Aplicacion)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/seccioncomida')
def seccioncomida():
    return render_template('seccion-comida.html')

@app.route('/seccionfarmacia')
def seccionfarmacia():
    return render_template('seccion-farmacia.html')

@app.route('/seccionlicores')
def seccionlicores():
    return render_template('seccion-licores.html')

@app.route('/seccionexpress')
def seccionexpress():
    return render_template('seccion-express.html')

@app.route('/secciongeneral')
def secciongeneral():
    return render_template('seccion-general.html')

@app.route('/empresa')
def empresa():
    return render_template('empresa.html')

@app.route('/registrate')
def registrate():
    return render_template('registrate.html')

@app.route('/ingresa')
def ingresa():
    return render_template('ingresa.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')