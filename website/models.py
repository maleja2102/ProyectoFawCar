from . import db
from flask_login import UserMixin

class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key = True)

class Usuarios(Base, UserMixin):
    nombre = db.Column(db.String(150))
    apellido = db.Column(db.String(150))
    usuario = db.Column(db.String(150), unique = True)
    clave = db.Column(db.String(150))
    cedula = db.Column(db.Integer, unique = True)
    correo = db.Column(db.String(150), unique = True)
    cargo = db.Column(db.String(150))

class Inventario(Base):
    marca = db.Column(db.String(150))
    modelo = db.Column(db.String(150))
    cantidad = db.Column(db.Integer)
    fecha_salida = db.Column(db.String(150))
    proveedor_id = db.Column(db.Integer, db.ForeignKey("proveedores.id"))

class Proveedores(Base):
    empresa = db.Column(db.String(150), unique = True)
    contacto = db.Column(db.String(150))
    telefono = db.Column(db.String(150), unique = True)
    direccion = db.Column(db.String(150))
    correo = db.Column(db.String(150), unique = True)
    vehiculos = db.relationship("Inventario")