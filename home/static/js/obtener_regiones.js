document.addEventListener('DOMContentLoaded', function () {
    // Cargar el archivo JSON
    fetch('/static/data/regiones_chile.json')
        .then(response => response.json())
        .then(data => {
            const regionSelect = document.getElementById('region');
            const ciudadSelect = document.getElementById('ciudad');
            const comunaSelect = document.getElementById('comuna');

            // Función para cargar las regiones en el select
            const loadRegions = () => {
                Object.keys(data).forEach(region => {
                    const option = document.createElement('option');
                    option.value = region;
                    option.textContent = region;
                    regionSelect.appendChild(option);
                });
            };

            // Función para cargar las ciudades según la región seleccionada
            const loadCities = (region) => {
                // Limpiar ciudad y comuna
                ciudadSelect.innerHTML = '<option value="" disabled selected>Selecciona una ciudad</option>';
                comunaSelect.innerHTML = '<option value="" disabled selected>Selecciona una comuna</option>';
                comunaSelect.disabled = true;

                if (region && data[region]) {
                    ciudadSelect.disabled = false;

                    Object.keys(data[region]).forEach(city => {
                        const option = document.createElement('option');
                        option.value = city;
                        option.textContent = city;
                        ciudadSelect.appendChild(option);
                    });
                } else {
                    ciudadSelect.disabled = true;
                }
            };

            // Función para cargar las comunas según la ciudad seleccionada
            const loadCommunes = (region, city) => {
                // Limpiar comuna
                comunaSelect.innerHTML = '<option value="" disabled selected>Selecciona una comuna</option>';

                if (city && data[region] && data[region][city]) {
                    comunaSelect.disabled = false;

                    data[region][city].forEach(comuna => {
                        const option = document.createElement('option');
                        option.value = comuna;
                        option.textContent = comuna;
                        comunaSelect.appendChild(option);
                    });
                } else {
                    comunaSelect.disabled = true;
                }
            };

            // Inicializar las regiones en el select
            loadRegions();

            // Actualizar ciudades cuando se cambia la región
            regionSelect.addEventListener('change', function () {
                const selectedRegion = regionSelect.value;
                loadCities(selectedRegion);
            });

            // Actualizar comunas cuando se cambia la ciudad
            ciudadSelect.addEventListener('change', function () {
                const selectedRegion = regionSelect.value;
                const selectedCity = ciudadSelect.value;
                loadCommunes(selectedRegion, selectedCity);
            });
        })
        .catch(error => {
            console.error('Error al cargar el archivo JSON:', error);
        });
});
