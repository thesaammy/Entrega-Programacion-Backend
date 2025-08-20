from flask import Blueprint, request, render_template, redirect, url_for,flash
from models.usuarios_model import Usuarios
import hashlib

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth', methods=['POST'])
def auth():
    username = request.form['username']
    password = request.form['password']

    if " " in username:
        flash("No se permiten los espacios en Usuario", "danger")
        return redirect(url_for('inventario'))

    # Crear hash de password
    password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    # Aquí deberías verificar el usuario y la contraseña con la base de datos
    usuario = Usuarios.query.filter_by(username=username, password=password).first()

    if usuario:
        flash("Inicio de sesión exitoso", "success")
        return redirect(url_for('productos.inventario'))
    else:
        flash("Usuario o contraseña incorrectos", "danger")
        return redirect(url_for('login'))

@auth_bp.route('/logout')
def logout():
    flash("Sesión cerrada exitosamente", "success")
    return redirect(url_for('login'))
