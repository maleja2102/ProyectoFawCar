// Cambiar rutas para el formulario de Usuarios
function usuarios_update() {
    document.getElementById("form_usuarios").action = "/usuarios/update";
}

function usuarios_delete() {
    document.getElementById("form_usuarios").action = "/usuarios/delete";
}

function usuarios_search() {
    document.getElementById("form_usuarios").action = "/usuarios";
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


$(document).ready( function () {
    var table = $('#usertable').DataTable({
        paging: false,
        searching: false,
        info:false,
        "columnDefs": [
            {
                "targets": [ 3 ],
                "visible": false,
            },
            {
                "targets": [ 4 ],
                "visible": false,
            }
        ]

    });
    
    $("#usertable tbody tr").on('click',function(event) {
        $("#usertable tbody tr").removeClass('bg-primary');
        // $("#usertable tbody tr").removeClass('odd');   
        $("#usertable tbody tr").css({"color":"",})      
        $(this).addClass('bg-primary');
        $(this).css({"color":"white"})
        // table.rows(this).select();
        
        // var nombre=table.rows(this).data
        $('#usertable tbody').on( 'click', 'tr', function () {
            fila=table.row(this).data()
            document.getElementById("inputNombre").value= fila[0]
            document.getElementById("inputApellido").value= fila[1]
            document.getElementById("inputUsuario").value= fila[2]
            document.getElementById("inputPassword").value= fila[3]
            document.getElementById("inputRol").value= fila[4]
            document.getElementById("inputCedula").value= fila[5]
            document.getElementById("inputEmail").value= fila[6]
            document.getElementById("inputCargo").value= fila[7]
            document.getElementById("userImage").src=fila[8]
        } );
        
    });
    $("#usertable tbody tr:eq(0)").click();
} )

