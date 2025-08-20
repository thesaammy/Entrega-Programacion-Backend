from flask import Blueprint, request, render_template, redirect, url_for,flash
import hashlib
from models.usuarios_model import Usuarios
from utils.db import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth', methods=['POST'])
def auth():
    username = request.form['username']
    password = request.form['password']

    if " " in username:
        flash("No se permiten los espacios en Usuario", "danger")
        return render_template('login.html')

    # Crear hash de password
    password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    # Aquí deberías verificar el usuario y la contraseña con la base de datos
    usuario = Usuarios.query.filter_by(username=username, password=password).first()

    if usuario:
        flash("Inicio de sesión exitoso", "success")
        return redirect(url_for('inventario'))
    else:
        flash("Usuario o contraseña incorrectos", "danger")
        return render_template('login.html')

    
