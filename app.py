from flask import Flask, render_template, jsonify, redirect, request

from listas import usuarios1, productos1, proveedores1
app = Flask(__name__)

lista_usuarios = ["usuario", "admin", "superadmin"]
lista_inventario = ["mazda 3", "chevrolet onix", "mazda ñao"]
lista_proveedores = ["Kia", "General Motors", "Volkswagen"]

# Rutas principales
@app.route('/', methods=['GET','POST'])
def ingreso():
    return "render_template('ingreso.html')"
#rol_usuario="admin"

@app.route('/registro', methods=['GET','POST'])
def regisro():
    return "render_template('registro.html')"
#ejemplo
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
