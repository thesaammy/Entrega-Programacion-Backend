from flask import Blueprint, request,render_template, redirect, url_for, flash
from models.usuarios_model import Usuarios
from utils.db import db
import hashlib 


usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/usuarios')
def listar_usuarios():
    usuarios_list = Usuarios.query.all()
    return render_template('usuarios.html', usuarios_list=usuarios_list)

#Crear y Borrar
@usuarios_bp.route('/usuarios/crear', methods=['POST'])
def crear_usuario():
    username = request.form['username']
    password = request.form['password']
    rol = request.form['rol']
    
    print(username)
    #Validar espacio
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
def eliminar_usuario(id):
    usuario = Usuarios.query.get(id)
    db.session.delete(usuario)
    db.session.commit()    
    flash(f"Usuario {usuario.username} eliminado correctamente", "success")
    return redirect(url_for('usuarios.listar_usuarios'))