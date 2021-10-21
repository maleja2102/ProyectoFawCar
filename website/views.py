from flask import Blueprint, render_template, request, redirect, flash
from .models import Usuarios, Inventario, Proveedores
from werkzeug.security import generate_password_hash, check_password_hash

views = Blueprint("views", __name__)

rol_usuario = ""

@views.route("/")
def ingreso():
    return render_template("ingreso.html")

@views.route("/login", methods=["POST"])
def login():
    username_login = request.form["user"]
    password = request.form["pass"]

    if len(username_login) == 0:
        flash("Escribe tu nombre de usuario", category="error")  
    elif len(password) == 0:
        flash("Escribe tu contraseña", category="error")  
    else:
        return redirect("inicio")

    return redirect("/")    

@views.route("/inicio")
def inicio():
    return render_template("inicio.html")

@views.route("/usuarios")
def usuarios():
    return render_template('usuarios.html')

@views.route("/inventario")
def inventario():

    return render_template('inventario.html')

@views.route("/proveedores")
def proveedor():
    return render_template('proveedores.html')


# CRUD ROUTES
# USUARIOS
@views.route("/usuarios/add", methods=['POST'])
def usuarios_add():
    pass

@views.route("/usuarios/update", methods=['POST'])
def usuarios_update():
    pass

@views.route("/usuarios/delete", methods=['POST'])
def usuarios_delete():
    return redirect("/usuarios")


# INVENTARIO
@views.route("/inventario/add", methods=['POST'])
def inventario_add():
    return redirect("/inventario")

@views.route("/inventario/update", methods=['POST'])
def inventario_update():
    pass

@views.route("/inventario/delete", methods=['POST'])
def inventario_delete():
    return redirect("/inventario")


# PROVEEDORES
@views.route("/proveedores/add", methods=['POST'])
def proveedores_add():
    pass

@views.route("/proveedores/update", methods=['POST'])
def proveedores_update():
    pass

@views.route("/proveedores/delete", methods=['POST'])
def proveedores_delete():
    return redirect("/proveedores")





@views.route("/prueba")
def prueba():
    return render_template('prueba.html')