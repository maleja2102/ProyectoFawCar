from enum import unique
from flask import Flask, render_template, jsonify, redirect, request,session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import format_string
from werkzeug.security import *
from werkzeug.utils import redirect
import os

from wtforms.fields.simple import PasswordField
from wtforms.validators import Email
from login import formIngreso
from register import formRegistro

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db=SQLAlchemy(app)

#modelado base de datos
class core(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key = True)

class Users(core):
    __tableName__ = "Users"
    username= db.Column(db.String, unique=True, nullable=False)
    password= db.Column(db.String, nullable=False)
    role= db.Column(db.String, nullable=False)
    email= db.Column(db.String, unique=True, nullable=False)
    name= db.Column(db.String)
    surname= db.Column(db.String)
    personalId=db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return '<Users %r>' % self.username

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Cars(core):
    __tableName__ = "Cars"
    brand= db.Column(db.String, nullable=False)
    model= db.Column(db.String, nullable=False)
    description= db.Column(db.String)
    year= db.Column(db.String,  nullable=False)
    stock= db.Column(db.String)
    type= db.Column(db.String)

    def __repr__(self):
        return '<Cars %r>' % self.description

class Supplier(core):
    __tableName__ = "Suppliers"
    name= db.Column(db.String, unique=True, nullable=False)
    description= db.Column(db.String)
    contact= db.Column(db.String, nullable=False)
    phone= db.Column(db.String)
    email= db.Column(db.String,unique=True, nullable=False)
    address= db.Column(db.String)
    TributaryId=db.Column(db.String, unique=True, nullable=False)
    def __repr__(self):
        return '<Suppliers %r>' % self.name


# Rutas principales
@app.route('/', methods=['GET','POST'])
def ingreso():
    form=formIngreso()
    flash("buenas buenas")
    return render_template('ingreso.html', form=form)

#Ruta inicio (todos los roles)
@app.route('/inicio',methods=['GET','POST'])
def iniciar():
   #Por definir, deberia redirigir al inicio, ya que no debe ser accesible sin un usuario y su rol 
    if request.method=='POST':
        #Si la solicitud es POST
        #Traer usuario y contraseña del formulario
            formu=formIngreso()
            user = formu.usuario.data
            password = formu.contrasena.data
            #Recorremos la lista en busca del usuario y la contraseña introducidos
            login=Users.query.filter_by(username=user).first()
            # if login:
            #     if login.password == password:
            #         session["user"]=login.username
            #         session["rol"]=login.role
            #         return redirect("inicio")
            # else:
            #     return jsonify({"mensaje": "usuario no encontrado"})
            if login:
                if login.check_password(password):
                    session["user"]=login.username
                    session["rol"]=login.role
                    return redirect("inicio")
            else:
                return jsonify({"mensaje": "usuario no encontrado"})

    else:
        return render_template('inicio.html')

@app.route('/usuarios')
def usuario():
    rol_usuario= session['rol']
    return render_template('usuarios.html', rol_usuario = rol_usuario)

@app.route('/proveedores')
def proveedor():
    rol_usuario= session['rol']
    return render_template('proveedores.html', rol_usuario = rol_usuario)

@app.route('/inventario')
def inventario():
    rol_usuario= session['rol']
    return render_template('inventario.html', rol_usuario = rol_usuario)

@app.route('/prueba',methods=['GET','POST'])
def prueba():
    rol_usuario= session['rol']
    return render_template('inventario.html',rol_usuario=rol_usuario)

@app.route('/registro', methods=['GET','POST'])
def registro():
    form=formRegistro()
    if request.method=='POST':
        username= form.username.data
        password=form.password.data
        confirm=form.confirm.data
        email=form.email.data
        name=form.name.data
        surname=form.surname.data
        personalId=form.personalId.data

        if password==confirm:
            user=Users(username=username,email=email,name=name,surname=surname,personalId=personalId,role='registred')
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            # return render_template('inicio.html')
    return render_template('registro.html',form=form)

@app.route('/logout', methods=['GET','POST'])
def logout():
    session.clear()
    flash("ha cerrado sesion correctamente")
    return redirect("/")

if __name__ == '__main__':
    db.create_all()
    app.run(host='127.0.0.1', port=8000, debug=True)
