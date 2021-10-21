// Cambiar rutas para el formulario de Usuarios
function usuarios_update() {
    document.getElementById("form_usuarios").action = "/usuarios/update";
}

function usuarios_delete() {
    document.getElementById("form_usuarios").action = "/usuarios/delete";
}


// Cambiar rutas para el formulario de Inventario
function inventario_update() {
    document.getElementById("form_inventario").action = "/inventario/update";
}

function inventario_delete() {
    document.getElementById("form_inventario").action = "/inventario/delete";
}


// Cambiar rutas para el formulario de Proveedores
function proveedores_update() {
    document.getElementById("form_proveedores").action = "/proveedores/update";
}

function proveedores_delete() {
    document.getElementById("form_proveedores").action = "/proveedores/delete";
}