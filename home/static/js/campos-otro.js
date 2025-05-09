// OTRO DE TIPO DE TIENDA

function mostrarPreguntaCobroSelect(selectElement) {
  const contenedor = document.getElementById('pregunta_cobro_bano');
  if (selectElement.value === 'si') {
    contenedor.style.display = 'block';
  } else {
    contenedor.style.display = 'none';
  }
}

function mostrarCampoOtro() {
  const seleccion = document.getElementById("adquirente").value;
  const campoOtro = document.getElementById("campoOtro");
  campoOtro.style.display = (seleccion === "otro") ? "block" : "none";
}

// Ejecutar al cargar por si ya hay algo seleccionado
window.addEventListener('DOMContentLoaded', mostrarCampoOtro);