from utils.db import db
from datetime import datetime

class Inventario(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False, unique=True)
    cantidad = db.Column(db.Integer, nullable=False, default=0)
    actualizado_en = db.Column(db.DateTime, default=datetime.utcnow,onupdate=datetime.utcnow)

    #Crear Relacion inventario-producto
    producto_rel = db.relationship("Productos", back_populates="inventario_rel")
