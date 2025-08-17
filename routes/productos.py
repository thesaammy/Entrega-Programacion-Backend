from flask import Blueprint, request, jsonify,render_template
from models.productos_model import Productos
from models.inventario_model import Inventario
from utils.db import db

productos_bp = Blueprint('productos', __name__)

@productos_bp.route("/productos")
def productos():
    return render_template('registroProducto.html')

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

    return f"producto {nombre} creado con {cantidadProducto} unidades "


@productos_bp.route("/productos/eliminar", methods=["DELETE"])
def eliminar_producto():
    # Lógica para eliminar un producto
    return "Producto eliminado"

@productos_bp.route("/productos/actualizar", methods=["PUT"])
def actualizar_producto():
    # Lógica para actualizar un producto
    return "Producto actualizado"

@productos_bp.route("/productos/obtener", methods=["GET"])
def obtener_producto():
    # Lógica para obtener un producto
    return "Producto obtenido"
