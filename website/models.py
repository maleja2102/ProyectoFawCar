from . import db
from werkzeug.security import *

class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key = True)

class Usuarios(Base):
    nombre = db.Column(db.String(150))
    apellido = db.Column(db.String(150))
    usuario = db.Column(db.String(150), unique = True)
    clave = db.Column(db.String(150))
    rol = db.Column(db.String(30))
    cedula = db.Column(db.Integer, unique = True)
    correo = db.Column(db.String(150), unique = True)
    cargo = db.Column(db.String(150))
    imagen = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)

    def set_password(self, clave):
        self.clave = generate_password_hash(clave)

    def check_password(self, clave):
        return check_password_hash(self.clave, clave)

class Inventario(Base):
    marca = db.Column(db.String(150))
    modelo = db.Column(db.String(150))
    cantidad = db.Column(db.Integer)
    fecha_salida = db.Column(db.String(150))
    cantidad_minima =db.Column(db.Integer)
    imagen = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    proveedor_id = db.Column(db.Integer, db.ForeignKey("proveedores.id"))

class Proveedores(Base):
    empresa = db.Column(db.String(150), unique = True)
    contacto = db.Column(db.String(150))
    telefono = db.Column(db.String(150), unique = True)
    direccion = db.Column(db.String(150))
    correo = db.Column(db.String(150), unique = True)
    imagen = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    vehiculos = db.relationship("Inventario")