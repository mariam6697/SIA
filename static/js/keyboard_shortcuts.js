// Atajos de teclado
// N = ingresar venta nueva
// En la venta de nueva venta, 1-2-3 para las opciones de pago
// Presionar ENTER para aceptar y pasar a añadir productos

// dominio
var dom = "http://127.0.0.1:8000/";

$(window).keydown(
    function(k){
        var notTheseOnes = ['textarea','input'];
        var target = k.target.tagName.toLowerCase();
        if (k.which == 78 && $.inArray(target,notTheseOnes) < 0){
            window.location.href = dom+"ventas/venta/new";
        }
    });

$(window).keydown(
    function(k){
        var notTheseOnes = ['textarea','input'];
        var target = k.target.tagName.toLowerCase();
        if (k.which == 80 && $.inArray(target,notTheseOnes) < 0){
            var id = idventa;
            var url = dom+"ventas/venta/"+id+"/pago-realizado";
            window.location.href = url;
        }
    });

$(window, '#venta').keypress(function(e){
    if(e.which == 49){
        document.getElementById('id_TipoPago').value = 1;
    }
    if(e.which == 50){
        document.getElementById('id_TipoPago').value = 2;
    }
    if(e.which == 51){
        document.getElementById('id_TipoPago').value = 3;
    }
    if(e.which == 13){
        $('form').submit();
    }
});

$(window, '#detalle').keypress(function(e){
    if(e.which == 13){
        $(this).closest('form').submit();
    }
});