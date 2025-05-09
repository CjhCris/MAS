//Datos de Tienda

  document.getElementById('formulario-tienda').addEventListener('submit', function (e) {
      e.preventDefault();  // evita recarga de página
  
      const formData = new FormData(this);
      const jsonData = {};
  
      for (const [key, value] of formData.entries()) {
          jsonData[key] = value;
      }
  
      fetch(window.location.href, {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': getCookie('csrftoken')
          },
          body: JSON.stringify(jsonData)
      })
      .then(response => response.json())
      .then(data => {
          if (data.status === 'success') {
              alert('Datos enviados exitosamente');
          } else {
              alert('Error: ' + data.message);
          }
      })
      .catch(error => {
          alert('Error al enviar formulario');
          console.error(error);
      });
  });
  
  function getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
          const cookies = document.cookie.split(';');
          for (let i = 0; i < cookies.length; i++) {
              const cookie = cookies[i].trim();
              if (cookie.substring(0, name.length + 1) === (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
  }
 
  

  // Esperar a que el DOM esté completamente cargado
  document.addEventListener('DOMContentLoaded', function () {
      const currentUrl = window.location.href;


      const regex = /formulario_tienda\/([a-zA-Z0-9_-]+)\/?$/;
      const match = currentUrl.match(regex);

      if (match) {
          const sheetId = match[1];


          document.getElementById('sheet-id').value = sheetId;
      } else {
          console.error('No se pudo extraer el ID de la URL.');
      }
  });


  function enviarFormulario() {
      const form = document.getElementById('formulario-tienda');
      const formData = new FormData(form);
  
      // Convertir a JSON
      const data = {};
      formData.forEach((value, key) => {
          data[key] = value;
      });
  
      console.log('Datos enviados al servidor:', data);  // Para depuración
  
      fetch('/guardar_formulario_tienda/', {  // Cambia la URL por la de tu vista Django
          method: 'POST',
          headers: {
              'X-CSRFToken': getCSRFToken(),
              'Content-Type': 'application/json'
          },
          body: JSON.stringify(data)
      })
      .then(response => {
          if (response.ok) {
              alert('Datos guardados correctamente.');
          } else {
              alert('Error al guardar los datos.');
          }
      })
      .catch(error => {
          console.error('Error en la solicitud:', error);
      });
  }
  
  // Extraer token CSRF de cookies (Django)
  function getCSRFToken() {
      const name = 'csrftoken';
      const cookies = document.cookie.split(';');
      for (let cookie of cookies) {
          const trimmed = cookie.trim();
          if (trimmed.startsWith(name + '=')) {
              return trimmed.substring(name.length + 1);
          }
      }
      return '';
  }
  
  
// form Admin

document.getElementById('formulario-admin').addEventListener('submit', function (e) {
    e.preventDefault();

    const formData = new FormData(this);
    const jsonData = {};

    for (const [key, value] of formData.entries()) {
        jsonData[key] = value;
    }

    jsonData['sheet_id'] = SHEET_ID;  // Enviar el ID de la hoja a Django

    fetch('/guardar_formulario_admin/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
        },
        body: JSON.stringify(jsonData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert('Datos del administrador guardados correctamente.');
        } else {
            alert('Error: ' + data.message);
        }
    })
    .catch(error => {
        alert('Error al enviar formulario');
        console.error(error);
    });
});

function getCSRFToken() {
    const name = 'csrftoken';
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
        const trimmed = cookie.trim();
        if (trimmed.startsWith(name + '=')) {
            return trimmed.substring(name.length + 1);
        }
    }
    return '';
}

document.addEventListener("DOMContentLoaded", function () {
    const infraestructuraForm = document.getElementById("formulario-infraestructura");

    if (infraestructuraForm) {
        infraestructuraForm.addEventListener("submit", function (e) {
            e.preventDefault();

            const formData = new FormData(infraestructuraForm);
            const jsonData = {};

            for (const [key, value] of formData.entries()) {
                jsonData[key] = value;
            }

            jsonData['sheet_id'] = document.getElementById('sheet-id')?.value;

            fetch('/guardar_formulario_infraestructura/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken()
                },
                body: JSON.stringify(jsonData)
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    alert('Datos de infraestructura guardados correctamente.');
                } else {
                    alert('Error: ' + data.message);
                }
            })
            .catch(error => {
                alert('Error al enviar formulario de infraestructura');
                console.error(error);
            });
        });
    }
});
