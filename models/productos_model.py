from utils.db import db


class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    precio = db.Column(db.Integer, nullable=False)

    #Crear Relacion producto-inventario
    inventario_rel = db.relationship('Inventario', back_populates='producto_rel', uselist=False, cascade="all, delete-orphan")

    def __init__(self, nombre, descripcion, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio


