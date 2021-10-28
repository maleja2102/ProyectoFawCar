// Cambiar rutas para el formulario de Usuarios
function usuarios_update() {
    document.getElementById("form_usuarios").action = "/usuarios/update";
}

function usuarios_delete() {
    document.getElementById("form_usuarios").action = "/usuarios/delete";
}

function usuarios_search() {
    document.getElementById("form_busqueda").action = "/usuarios";
}

function inventarios_search() {
    document.getElementById("form_busqueda").action = "/inventarios";
}

function proveedores_search() {
    document.getElementById("form_busqueda").action = "/proveedores";
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

// USUARIOS SELECT
$(document).ready( function () {
    var usertable = $('#usertable').DataTable({
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

    var provtable = $('#provtable').DataTable({
        paging: false,
        searching: false,
        info:false,
    });

    var inventariotable = $('#inventariotable').DataTable({
        paging: false,
        searching: false,
        info:false,
        // "columnDefs": [
        //     {
        //         "targets": [ 3 ],
        //         "visible": false,
        //     },
        //     {
        //         "targets": [ 4 ],
        //         "visible": false,
        //     }
        // ]

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
            fila=usertable.row(this).data()
            document.getElementById("inputNombre").value= fila[0]
            document.getElementById("inputApellido").value= fila[1]
            document.getElementById("inputUsuario").value= fila[2]
            document.getElementById("inputPassword").value= fila[3]
            document.getElementById("inputRol").value= fila[4]
            document.getElementById("inputCedula").value= fila[5]
            document.getElementById("inputEmail").value= fila[6]
            document.getElementById("inputCargo").value= fila[8]
            document.getElementById("userImage").src=fila[7]
        } );
        
    });
    $("#usertable tbody tr:eq(0)").click();

    $("#inventariotable tbody tr").on('click',function(event) {
        $("#inventariotable tbody tr").removeClass('bg-primary');
        // $("#usertable tbody tr").removeClass('odd');   
        $("#inventariotable tbody tr").css({"color":"",})      
        $(this).addClass('bg-primary');
        $(this).css({"color":"white"})
        // table.rows(this).select();
        
        // var nombre=table.rows(this).data
        $('#inventariotable tbody').on( 'click', 'tr', function () {
            fila=inventariotable.row(this).data()
            document.getElementById("id").value= fila[0]
            document.getElementById("marca").value= fila[1]
            document.getElementById("modelo").value= fila[2]
            document.getElementById("cantidad").value= fila[3]
            document.getElementById("anio").value= fila[4]
            document.getElementById("cantidadMin").value= fila[5]
            document.getElementById("inventario_imagen").src=fila[6]
            document.getElementById("Proveedor").value= fila[7]
        } );
        
    });
    $("#inventariotable tbody tr:eq(0)").click();

    $("#provtable tbody tr").on('click',function(event) {
        $("#provtable tbody tr").removeClass('bg-primary');
        // $("#usertable tbody tr").removeClass('odd');   
        $("#provtable tbody tr").css({"color":"",})      
        $(this).addClass('bg-primary');
        $(this).css({"color":"white"})
        // table.rows(this).select();
        
        // var nombre=table.rows(this).data
        $('#provtable tbody').on( 'click', 'tr', function () {
            fila=provtable.row(this).data()
            document.getElementById("proveedores_id").value= fila[0]
            document.getElementById("proveedores_empresa").value= fila[1]
            document.getElementById("proveedores_contacto").value= fila[2]
            document.getElementById("proveedores_telefono").value= fila[3]
            document.getElementById("proveedores_direccion").value= fila[4]
            document.getElementById("proveedores_correo").value= fila[5]
            document.getElementById("imagProveedor").src=fila[6]
            //document.getElementById("Proveedor").value= fila[7]
        } );
        
    });
    $("#provtable tbody tr:eq(0)").click();
} )