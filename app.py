from flask import Flask, render_template, jsonify, redirect, request
from werkzeug.utils import format_string
import os

from listas import usuarios1, productos1, proveedores1
from login import formIngreso
app = Flask(__name__)
app.secret_key = os.urandom(24)

lista_usuarios = ["usuario", "admin", "superadmin"]
lista_inventario = ["mazda 3", "chevrolet onix", "mazda ñao"]
lista_proveedores = ["Kia", "General Motors", "Volkswagen"]
rol_usuario=""

# Rutas principales
@app.route('/', methods=['GET','POST'])
def ingreso():
    form=formIngreso()
    return render_template('ingreso.html', form=form)

#Ruta inicio (todos los roles)
@app.route('/inicio',methods=['GET','POST'])
def iniciar():
   #Por definir, deberia redirigir al inicio, ya que no debe ser accesible sin un usuario y su rol 
    if request.method=='GET':
        return render_template('inicio.html')
    else: #Si la solicitud es POST
        #Traer usuario y contraseña del formulario
            # user=request.form.get('user')
            # passw=request.form.get('pass')
            formu=formIngreso()
            user = formu.usuario.data
            password = formu.contrasena.data
            #Recorremos la lista en busca del usuario y la contraseña introducidos
            login = [usuario for usuario in usuarios1 if (usuario["nombre"] == user)and (usuario["contrasena"]==password)]
            #Si la lista resultante está vacia, enviamos error
            rol_usuario= login[0]["rol"]
            if (len(login) == 0):
                return jsonify({"mensaje": "usuario no encontrado"})
            else:
                #si la lista resultante contiene un elemento (siempre debe ser 1)
                #extraemos el rol del usuario de la lista
                # rol_usuario= login[0]["rol"]
                #mostramos la plantilla de inicio, pasandole como parametro el rol del usuario
                return render_template('inicio.html',rol_usuario= rol_usuario)

@app.route('/usuarios')
def usuario():
    return render_template('usuarios.html', rol_usuario = rol_usuario )

@app.route('/prueba')
def prueba():
    return render_template('prueba.html')

@app.route('/inventariosuperadmin')
def inventariosuperadmin():
    return render_template('inventario.html')

@app.route('/prueba_proveedores')
def prueba_proveedores():
    return render_template('proveedores.html')

#rol_usuario="admin"

#ejemplo
@app.route('/registro', methods=['GET','POST'])
def regisro():
    return "render_template('registro.html')"
# Rutas para el superadmin
@app.route('/inicio_superadmin', methods=['GET'])
def inicio():
    return "Inicia sesión"

@app.route('/perfil_superadmin', methods=['GET','POST'])
def perfil():
    return "Bienvenido, aquí podrás cambiar la información de tu cuenta"

@app.route('/usuarios_superadmin/<id_usuario>', methods=['GET','POST'])
def usuarios(id_usuario):
    if id_usuario in lista_usuarios:
        return f"Bienvenido, {id_usuario}"
    else:
        return f"El usuario {id_usuario} no está en la lista"

@app.route('/inventario_superadmin/<id_carro>', methods=['GET','POST'])
def inventario(id_carro):
    if id_carro in lista_inventario:
        return f"Aún tienes el vehiculo, {id_carro}"
    else:
        return f"No tienes el vehículo {id_carro}"

@app.route('/proveedores_superadmin/<id_proveedor>', methods=['GET','POST'])
def proveedores(id_proveedor):
    if id_proveedor in lista_proveedores:
        return f"El proveedor {id_proveedor} aún está activo"
    else:
        return f"El proveedor {id_proveedor} ya no está activo"


# Rutas para el admin
@app.route('/administrador/<string:dato>', methods=['GET','POST'])
def usuariosAdmin (dato):
    usua = [usuario for usuario in usuarios1 if (usuario["rol"] == dato)]
    if (len(usua) == 0):
        return jsonify({"mensaje": "usuario no encontrado"})
    else:
        return jsonify({"mensaje": "articulo encontrado", "articulo":usua})

@app.route('/proveedoradministrador/<string:info>', methods=['GET','POST'])
def proveedoresAdmin(info):
    provee = [proveedor for proveedor in proveedores1 if (proveedor["Contacto"] == info)]
    if (len(provee) == 0):
        return jsonify({"mensaje": "usuario no encontrado"})
    else:
        return jsonify({"mensaje": "articulo encontrado", "articulo":provee})

@app.route('/administradorproductos/<string:informacion>', methods=['GET','POST'])
def productosAdmin(informacion):
    produc = [producto for producto in productos1 if (producto["Marca"] == informacion)]
    if (len(produc) == 0):
        return jsonify({"mensaje": "usuario no encontrado"})
    else:
        return jsonify({"mensaje": "articulo encontrado", "articulo":produc})


# Rutas para el usuario final
@app.route('/usuarioProveedores/<string:info>', methods=['GET','POST'])
def proveedoresUsuario(info):
    provee = [proveedor for proveedor in proveedores1 if (proveedor["Contacto"] == info)]
    if (len(provee) == 0):
        return jsonify({"mensaje": "usuario no encontrado"})
    else:
        return jsonify({"mensaje": "articulo encontrado", "articulo":provee})

@app.route('/usuarioProductos/<string:informacion>', methods=['GET','POST'])
def productosUsuario(informacion):
    produc = [producto for producto in productos1 if (producto["Modelo"] == informacion)]
    if (len(produc) == 0):
        return jsonify({"mensaje": "usuario no encontrado"})
    else:
        return jsonify({"mensaje": "articulo encontrado", "articulo":produc})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
