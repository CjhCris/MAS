function toggleSeccion(seccion) {
    const secciones = ['comercial', 'tecnico', 'critico'];
    secciones.forEach(s => {
      const div = document.getElementById(`seccion-${s}`);
      div.style.display = (s === seccion) ? (div.style.display === 'block' ? 'none' : 'block') : 'none';
    });
    ocultarFormulariosInternos();
  }

  function toggleFormulario(idFormulario) {
    const formularios = ['form-admin', 'form-tienda', 'form-infraestructura', 'form-pago', 'form-otros-servicios', 'form-avances-caja', 'form-datos-finales'];
  
    // Oculta todos los formularios
    formularios.forEach(id => {
      const form = document.getElementById(id);
      if (form) {
        form.style.display = (id === idFormulario && (form.style.display === 'none' || form.style.display === '')) ? 'block' : 'none';
      }
    });
  
    // Quitar clase activa de todos los botones
    const botones = document.querySelectorAll('.btn-outline-secondary');
    botones.forEach(b => b.classList.remove('btn-activo'));
  
    // Verifica si el formulario seleccionado está visible y añade clase activa al botón
    const formActivo = document.getElementById(idFormulario);
    if (formActivo && formActivo.style.display === 'block') {
      const botonesFormulario = document.querySelectorAll('button');
      botonesFormulario.forEach(boton => {
        if (boton.getAttribute('onclick')?.includes(`'${idFormulario}'`)) {
          boton.classList.add('btn-activo');
        }
      });
    }
  }
  


  function ocultarFormulariosInternos() {
    document.querySelectorAll('.formulario-interno').forEach(form => {
      form.style.display = 'none';
    });
  }