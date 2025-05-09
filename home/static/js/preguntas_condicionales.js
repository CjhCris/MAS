function mostrarPreguntaCobroSelect(selectElement) {
    const contenedor = document.getElementById('pregunta_cobro_bano');
    if (selectElement.value === 'si') {
        contenedor.style.display = 'block';  // Muestra la pregunta de cobro por baño
    } else {
        contenedor.style.display = 'none';   // Oculta la pregunta de cobro por baño
        // También ocultamos los campos adicionales cuando no se cobra por el baño
        document.getElementById('monto_cobro_bano').style.display = 'none';
        document.getElementById('metodo_pago_bano').style.display = 'none';
        document.getElementById('metodo_apertura_bano').style.display = 'none';
        document.getElementById('metodo_apertura_otro').style.display = 'none';
    }
}

// Función para mostrar el campo de monto a cobrar por el baño
function mostrarMontoCobroBano(selectElement) {
    const contenedorMonto = document.getElementById('monto_cobro_bano');
    const contenedorMetodoPago = document.getElementById('metodo_pago_bano');
    const contenedorMetodoApertura = document.getElementById('metodo_apertura_bano');
    if (selectElement.value === 'si') {
        contenedorMonto.style.display = 'block';  // Muestra el campo para ingresar el monto
        contenedorMetodoPago.style.display = 'block';  // Muestra el campo de método de pago
        contenedorMetodoApertura.style.display = 'block';  // Muestra el campo de método de apertura
    } else {
        contenedorMonto.style.display = 'none';   // Oculta el campo de monto
        contenedorMetodoPago.style.display = 'none';  // Oculta el campo de método de pago
        contenedorMetodoApertura.style.display = 'none';  // Oculta el campo de método de apertura
        document.getElementById('metodo_apertura_otro').style.display = 'none'; // Oculta el campo "Otro"
    }
}

// Función para mostrar el campo de especificar el método de apertura si se selecciona "Otro"
function mostrarCampoOtroApertura(selectElement) {
    const contenedorOtroApertura = document.getElementById('metodo_apertura_otro');
    if (selectElement.value === 'otro') {
        contenedorOtroApertura.style.display = 'block';  // Muestra el campo de especificar el método de apertura
    } else {
        contenedorOtroApertura.style.display = 'none';  // Oculta el campo de especificar el método de apertura
    }
}

function togglePuertaSeguridad() {
    var tienda24hrs = document.getElementById("tienda_24hrs").value;
    var puertaSeguridadDiv = document.getElementById("puerta_seguridad");

    if (tienda24hrs === "si") {
      puertaSeguridadDiv.style.display = "block";
    } else {
      puertaSeguridadDiv.style.display = "none";
    }
  }
  function togglePreguntasAdicionales() {
    var puertaSeguridad = document.getElementById("puerta_seguridad_cerrada").value;
    var distanciaCajaDiv = document.getElementById("distancia_caja");
    var pagosNocheDiv = document.getElementById("pagos_noche");

    if (puertaSeguridad === "si") {
      distanciaCajaDiv.style.display = "block";
      pagosNocheDiv.style.display = "block";
    } else {
      distanciaCajaDiv.style.display = "none";
      pagosNocheDiv.style.display = "none";
    }
  }


  function toggleSelect(idSelect, habilitar) {
    const select = document.getElementById(idSelect);
    if (select) {
      select.disabled = !habilitar;
      if (!habilitar) {
        select.selectedIndex = 0; // reinicia a la primera opción (usualmente "0")
      }
    }
  }

 function toggleFields() {
        var tienda24hrs = document.getElementById('tienda_24hrs').value;
        var puertaSeguridad = document.getElementById('puerta_seguridad');
        var distanciaCaja = document.getElementById('distancia_caja');
        var pagosNoche = document.getElementById('pagos_noche');
        
        if (tienda24hrs === 'NO') {
            // Deshabilitar campos
            puertaSeguridad.style.display = 'none';
            distanciaCaja.style.display = 'none';
            pagosNoche.style.display = 'none';
            
            // También deshabilitar el contenido de los campos
            document.getElementById('puerta_seguridad_cerrada').disabled = true;
            document.getElementById('distancia_caja_puerta').disabled = true;
            document.getElementById('pagos_noche').disabled = true;
        } else {
            // Mostrar y habilitar campos
            puertaSeguridad.style.display = 'block';
            distanciaCaja.style.display = 'block';
            pagosNoche.style.display = 'block';
            
            // Habilitar los campos
            document.getElementById('puerta_seguridad_cerrada').disabled = false;
            document.getElementById('distancia_caja_puerta').disabled = false;
            document.getElementById('pagos_noche').disabled = false;
        }
    }

    // Ejecutar toggleFields al cargar la página en caso de que ya haya un valor seleccionado
    window.onload = function() {
        toggleFields();
    };
  