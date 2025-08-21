from flask import Blueprint, request,render_template, redirect, url_for, flash
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from models.productos_model import Productos
from models.inventario_model import Inventario
from sqlalchemy.exc import IntegrityError
from utils.db import db

productos_bp = Blueprint('productos', __name__)

@productos_bp.route("/inventario")
@jwt_required()
def inventario():
    id_usuario = get_jwt_identity()
    claims = get_jwt()
    productos_list = Productos.query.all()
    return render_template('app.html', productos_list=productos_list )


#Crear, Actualizar y Borrar
@productos_bp.route("/productos/crear", methods=["POST"])
@jwt_required()
def crear_producto():
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    precio = request.form['precio']
    cantidadProducto = request.form['cantidad']

    #Crear el objeto para guardar
    nuevoProducto = Productos(nombre,descripcion,precio)

    #Asociar inventario a producto
    nuevoProducto.inventario_rel = Inventario(cantidad=cantidadProducto)

    #Guardar el objeto en db
    try:
        db.session.add(nuevoProducto)
        db.session.commit()
        flash("Producto creado exitosamente", "success")
    except IntegrityError:
        db.session.rollback()
        flash(f"El producto '{nombre}' ya existe", "danger")

    return redirect("/inventario")

@productos_bp.route("/productos/eliminar/<id>")
@jwt_required()
def eliminar_producto(id):
    producto = Productos.query.get(id)
    db.session.delete(producto)
    db.session.commit()
    flash("Producto eliminado exitosamente", "success")

    return redirect(url_for('productos.inventario'))

@productos_bp.route("/productos/actualizar/<id>", methods=["GET", "POST"])
@jwt_required()
def actualizar_producto(id):
    producto = Productos.query.get(id)
    if request.method == "POST":
        producto.nombre = request.form['nombre']
        producto.descripcion = request.form['descripcion']
        producto.precio = request.form['precio']
        producto.inventario_rel.cantidad = request.form['cantidad']

        db.session.commit()
        flash(f"Producto '{producto.nombre}' actualizado exitosamente", "success")
        return redirect("/inventario")
    else:
        return render_template('actualizarProducto.html', producto=producto)