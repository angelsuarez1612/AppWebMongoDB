from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    usuario=request.form.get("usuario")
    contrasena=request.form.get("contraseña")
    client = MongoClient('localhost', 27017, username=usuario, password=contrasena)
    db = client.pruebaBD
    revista = db.Revista
    all_revista = revista.find()
    return render_template('login.html',all_revista=all_revista)
