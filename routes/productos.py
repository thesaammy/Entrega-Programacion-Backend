from flask import Blueprint, request, jsonify,render_template, redirect, url_for
from models.productos_model import Productos
from models.inventario_model import Inventario
from utils.db import db

productos_bp = Blueprint('productos', __name__)

@productos_bp.route("/productos")
def productos():
    return render_template('registroProducto.html')

@productos_bp.route("/inventario")
def inventario():
    productos_list = Productos.query.all()
    return render_template('inventario.html', productos_list=productos_list )

@productos_bp.route("/productos/crear", methods=["POST"])
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
    db.session.add(nuevoProducto)
    db.session.commit()

    return redirect("/inventario")

@productos_bp.route("/productos/eliminar/<id>")
def eliminar_producto(id):
    producto = Productos.query.get(id)
    db.session.delete(producto)
    db.session.commit()

    return redirect(url_for('productos.inventario'))

@productos_bp.route("/productos/actualizar/<id>", methods=["GET", "POST"])
def actualizar_producto(id):
    producto = Productos.query.get(id)
    if request.method == "POST":
        producto.nombre = request.form['nombre']
        producto.descripcion = request.form['descripcion']
        producto.precio = request.form['precio']
        producto.inventario_rel.cantidad = request.form['cantidad']

        db.session.commit()
        return redirect("/inventario")
    else:
        return render_template('actualizarProducto.html', producto=producto)