from flask import Flask, render_template, request, redirect, url_for
import requests
import json
from config import token

app = Flask(__name__, template_folder='templates')

API_BASE = "http://127.0.0.1:8000/api"

def get_headers():
    return {'Authorization': f'Token {token}'}

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/edificios")
def lista_edificios():
    """
        Listar edificios usando la API de Django (GET)
    """
    r = requests.get(f"{API_BASE}/edificios/", headers=get_headers())
    edificios = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    return render_template("edificios.html", edificios=edificios, numero=numero)


@app.route("/departamentos")
def lista_departamentos():
    """
        Listar departamentos usando la API de Django (GET)
    """
    r = requests.get(f"{API_BASE}/departamentos/", headers=get_headers())
    departamentos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    
    # obtener nombre del edificio para cada departamento
    datos = []
    for d in departamentos:
        datos.append({
            'nombre_propietario': d['nombre_propietario'],
            'costo': d['costo'],
            'num_cuartos': d['num_cuartos'],
            'edificio': obtener_edificio(d['edificio'])
        })
    return render_template("departamentos.html", departamentos=datos, numero=numero)


@app.route("/crear/edificio", methods=['GET', 'POST'])
def crear_edificio():
    """
        Crear edificio usando la API de Django (POST)
    """
    if request.method == 'POST':
        data = {
            'nombre': request.form['nombre'],
            'direccion': request.form['direccion'],
            'ciudad': request.form['ciudad'],
            'tipo': request.form['tipo'],
        }
        r = requests.post(f"{API_BASE}/edificios/", json=data, headers=get_headers())
        if r.status_code == 201:
            return redirect(url_for('lista_edificios'))
        else:
            print("Error al crear:", r.text)
    return render_template("crear_edificio.html")


@app.route("/crear/departamento", methods=['GET', 'POST'])
def crear_departamento():
    """
        Crear departamento usando la API de Django (POST)
    """
    # obtener lista de edificios para el select
    r = requests.get(f"{API_BASE}/edificios/", headers=get_headers())
    edificios = json.loads(r.content)['results']

    if request.method == 'POST':
        # Reemplazamos coma por punto por si el navegador envía el formato español
        costo_str = request.form['costo'].replace(',', '.')
        
        data = {
            'nombre_propietario': request.form['nombre_propietario'],
            'costo': float(costo_str),
            'num_cuartos': int(request.form['num_cuartos']),
            'edificio': request.form['edificio'],
        }
        r = requests.post(f"{API_BASE}/departamentos/", json=data, headers=get_headers())
        if r.status_code == 201:
            return redirect(url_for('lista_departamentos'))
        else:
            print("Error al crear:", r.text) # Para depuración
    return render_template("crear_departamento.html", edificios=edificios)


# funciones ayuda

def obtener_edificio(url):
    """
        Obtener el nombre de un edificio a partir de su URL
    """
    r = requests.get(url, headers=get_headers())
    nombre_edificio = json.loads(r.content)['nombre']
    return nombre_edificio

if __name__ == '__main__':
    app.run(debug=True, port=5000)
