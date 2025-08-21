from flask import Blueprint, request, render_template, redirect, url_for,flash, make_response
from flask_jwt_extended import set_access_cookies, create_access_token, unset_jwt_cookies
from models.usuarios_model import Usuarios
import hashlib
from datetime import timedelta

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

    #Verificación de que existe un registro del usuario
    usuario = Usuarios.query.filter_by(username=username, password=password).first()

    if usuario:
        flash("Inicio de sesión exitoso", "success")
        #Generar token e incluir en cookie
        access_token = create_access_token(identity=usuario.id, additional_claims={"rol": usuario.rol}, expires_delta=timedelta(hours=2))
        resp = make_response(redirect(url_for('productos.inventario')))
        set_access_cookies(resp, access_token)
        return resp
    else:
        flash("Usuario o contraseña incorrectos", "danger")
        return redirect(url_for('login'))

@auth_bp.route('/logout')
def logout():
    resp = make_response(redirect(url_for('login')))
    unset_jwt_cookies(resp)
    flash("Sesión cerrada exitosamente", "success")
    return resp
