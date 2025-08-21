from flask import Blueprint, request,render_template, redirect, url_for, flash
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from models.usuarios_model import Usuarios
from utils.db import db
import hashlib 


usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/usuarios')
@jwt_required()
def listar_usuarios():
    claims = get_jwt()                
    if claims.get("rol") != "admin":
        flash("No tienes permiso para acceder a esta página", "danger")
        return redirect(url_for('productos.inventario'))

    usuarios_list = Usuarios.query.all()
    return render_template('usuarios.html', usuarios_list=usuarios_list)

#Crear y Borrar
@usuarios_bp.route('/usuarios/crear', methods=['POST'])
@jwt_required()
def crear_usuario():
    claims = get_jwt()                
    if claims.get("rol") != "admin":
        flash("No tienes permiso para acceder a esta página", "danger")
        return redirect(url_for('productos.inventario'))

    username = request.form['username']
    password = request.form['password']
    rol = request.form['rol']

    if " " in username:
        flash("No se permiten los espacios en Usuario", "danger")
        return redirect(url_for('usuarios.listar_usuarios'))

    #Crear hash de password
    password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    
    #crear el objeto para guardar
    nuevo_usuario = Usuarios(username,password,rol)

    flash(f"Usuario {username} creado correctamente", "success")
    db.session.add(nuevo_usuario)
    db.session.commit()
    return redirect(url_for('usuarios.listar_usuarios'))


@usuarios_bp.route('/usuarios/eliminar/<id>')
@jwt_required()
def eliminar_usuario(id):
    claims = get_jwt()                
    if claims.get("rol") != "admin":
        flash("No tienes permiso para acceder a esta página", "danger")
        return redirect(url_for('productos.inventario'))
    
    usuario = Usuarios.query.get(id)
    db.session.delete(usuario)
    db.session.commit()    
    flash(f"Usuario {usuario.username} eliminado correctamente", "success")
    return redirect(url_for('usuarios.listar_usuarios'))