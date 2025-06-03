
let switchDisplayTransf = false;

//Variable usada para los metodos que no deben graficarse no generen problemas
let method_no_graphic = false; 


function addToDisplay(value) {
    if (switchDisplayTransf) {
        document.getElementById('transformada').value += value;
    } else {
        document.getElementById('display').value += value;
    }
}

function clearDisplay() {
    if (switchDisplayTransf) {
        document.getElementById('transformada').value = '';
    } else {  
        document.getElementById('display').value = '';
    }
}

function deleteLastChar() {
    if (switchDisplayTransf) {
        let currentVal = document.getElementById('transformada').value;
        document.getElementById('transformada').value = currentVal.slice(0, -1);
    } else {
        let currentVal = document.getElementById('display').value;
        document.getElementById('display').value = currentVal.slice(0, -1); 
    }
}


// funcion encargada de actualizar el elemento por defecto de lista desplegable 
// segun el metodo seleccionado

document.addEventListener('DOMContentLoaded', function() {
    // Extraer el puerto de la URL
    const currentUrl = window.location.href;
    const currentPort = currentUrl.match(/:\d+/);

    // Verificar si se encontró un puerto y establecer el método por defecto
    if (currentPort) {
        const port = currentPort[0].slice(1);  // Obtener solo el número del puerto
        const methodSelect = document.getElementById('method');

        // Establecer el método según el puerto
        switch (port) {
            case '5000':
                methodSelect.value = 'biseccion';
                break;
            case '5001':
                methodSelect.value = 'puntoFijo';
                break;
            case '5002':
                methodSelect.value = 'newton';
                break;
            case '5003':
                methodSelect.value = 'secante';
                break;
            case '5005':
                methodSelect.value = 'jacobi';
                break;
            case '5006':
                methodSelect.value = 'gauss';
                break;       
            case '5007':
                methodSelect.value = 'trapecio';
                break;
            case '5008':
                methodSelect.value = 'simpson';
                break;
            case '5009':
                methodSelect.value = 'euler';
                break;         
            default:
                methodSelect.value = '';  // Ninguno seleccionado
                break;
        }
        
        // Inicializar el comportamiento de los campos
        toggleFields();
    }
});


// Mostrar/Ocultar campos específicos según el método y definir el puerto
function toggleFields() {
    const method = document.getElementById('method').value;
    const bisectionFields = document.getElementById('bisectionFields');
    const fixedPointFields = document.getElementById('fixedPointFields');
    const newtonFields = document.getElementById('newtonFields');
    const secanteFields = document.getElementById('secanteFields');

    const jacobiFields = document.getElementById('jacobiFields');
    const gaussFields = document.getElementById('gaussFields');
    const trapecioFields = document.getElementById('trapecioFields');
    const simpsonFields = document.getElementById('simpsonFields');
    const eulerFields = document.getElementById('eulerFields');



    //inicialización variables booleanas
    switchDisplayTransf = false;
    method_no_graphic = false; 
    //

    let newPort;  // Definir puerto específico según el método seleccionado

    switch (method) {
        case 'biseccion':
            bisectionFields.style.display = 'block';
            fixedPointFields.style.display = 'none';
            newtonFields.style.display = 'none';
            secanteFields.style.display = 'none';
            gaussFields.style.display = 'none';
            simpsonFields.style.display = 'none';
            jacobiFields.style.display = 'none';
            trapecioFields.style.display = 'none';
            eulerFields.style.display = 'none';
            newPort = 5000;
            break;
        case 'puntoFijo':
            fixedPointFields.style.display = 'block';
            bisectionFields.style.display = 'none';
            newtonFields.style.display = 'none';
            secanteFields.style.display = 'none';
            gaussFields.style.display = 'none';
            simpsonFields.style.display = 'none';
            jacobiFields.style.display = 'none';
            trapecioFields.style.display = 'none';
            eulerFields.style.display = 'none';
            newPort = 5001;
            break;
        case 'newton':
            newtonFields.style.display = 'block';
            bisectionFields.style.display = 'none';
            fixedPointFields.style.display = 'none';
            secanteFields.style.display = 'none';
            gaussFields.style.display = 'none';
            simpsonFields.style.display = 'none';
            jacobiFields.style.display = 'none';
            trapecioFields.style.display = 'none';
            eulerFields.style.display = 'none';
            newPort = 5002;
            break;
        case 'secante':
            secanteFields.style.display = 'block';
            newtonFields.style.display = 'none';
            bisectionFields.style.display = 'none';
            fixedPointFields.style.display = 'none';
            gaussFields.style.display = 'none';
            simpsonFields.style.display = 'none';
            jacobiFields.style.display = 'none';
            trapecioFields.style.display = 'none';
            eulerFields.style.display = 'none';
            newPort = 5003;
            break;
        case 'jacobi':
            jacobiFields.style.display = 'block';
            secanteFields.style.display = 'none';
            newtonFields.style.display = 'none';
            bisectionFields.style.display = 'none';
            fixedPointFields.style.display = 'none';
            trapecioFields.style.display = 'none';
            gaussFields.style.display = 'none';
            simpsonFields.style.display = 'none';
            eulerFields.style.display = 'none';
            newPort = 5005;
            break;
        case 'gauss':
            gaussFields.style.display = 'block';
            jacobiFields.style.display = 'none';
            secanteFields.style.display = 'none';
            newtonFields.style.display = 'none';
            bisectionFields.style.display = 'none';
            fixedPointFields.style.display = 'none';
            trapecioFields.style.display = 'none';
            simpsonFields.style.display = 'none';
            eulerFields.style.display = 'none';
            newPort = 5006;
            break;        
        case 'trapecio':
            trapecioFields.style.display = 'block';
            jacobiFields.style.display = 'none';
            secanteFields.style.display = 'none';
            newtonFields.style.display = 'none';
            bisectionFields.style.display = 'none';
            fixedPointFields.style.display = 'none';
            gaussFields.style.display = 'none';
            simpsonFields.style.display = 'none';
            eulerFields.style.display = 'none';
            newPort = 5007;
            break;
         case 'trapecio':
            trapecioFields.style.display = 'block';
            jacobiFields.style.display = 'none';
            secanteFields.style.display = 'none';
            newtonFields.style.display = 'none';
            bisectionFields.style.display = 'none';
            fixedPointFields.style.display = 'none';
            gaussFields.style.display = 'none';
            simpsonFields.style.display = 'none';
            eulerFields.style.display = 'none';
            newPort = 5007;
            break;
        case 'simpson':
            simpsonFields.style.display = 'block';
            trapecioFields.style.display = 'none';
            jacobiFields.style.display = 'none';
            secanteFields.style.display = 'none';
            newtonFields.style.display = 'none';
            bisectionFields.style.display = 'none';
            fixedPointFields.style.display = 'none';
            gaussFields.style.display = 'none';
            eulerFields.style.display = 'none';
            newPort = 5008;
            break;   
        case 'euler':
            simpsonFields.style.display = 'none';
            trapecioFields.style.display = 'none';
            jacobiFields.style.display = 'none';
            secanteFields.style.display = 'none';
            newtonFields.style.display = 'none';
            bisectionFields.style.display = 'none';
            fixedPointFields.style.display = 'none';
            gaussFields.style.display = 'none';
            eulerFields.style.display = 'block';
            newPort = 5009;
            break;                 
        default:
            break;
    }

    // Cambiar el puerto en la URL actual si el puerto es definido
    if (newPort) {
        const currentUrl = window.location.href;
        const currentPort = currentUrl.match(/:\d+/);

        // Verificar si el puerto actual es diferente del nuevo puerto
        if (!currentPort || currentPort[0].slice(1) !== newPort.toString()) {
            const newUrl = currentUrl.replace(/:\d+/, `:${newPort}`);
            window.location.href = newUrl;  // Redirigir a la nueva URL con el puerto actualizado
        }
    }
}

// Función para enviar datos al servidor
document.getElementById('sendData').addEventListener('click', function(event) {
    event.preventDefault(); 
    const functionInput = document.getElementById('display').value;
    const selectedMethod = document.getElementById('method').value;

    let dataToSend = {
        function: functionInput,
        method: selectedMethod
    };

    let apiUrl = ''; 
    // Incluye xi y xu si el método es 'biseccion'
    if (selectedMethod === 'biseccion') {
        apiUrl = '/api/biseccion';
        const xi = document.getElementById('xi').value;
        const xu = document.getElementById('xu').value;
        dataToSend.xi = parseFloat(xi);
        dataToSend.xu = parseFloat(xu);
    }

    // Incluye xo y la transformada si el método es 'puntoFijo'
    if (selectedMethod === 'puntoFijo') {
        apiUrl = '/api/punto_fijo';
        const transformada = document.getElementById('transformada').value;
        dataToSend.transformada = transformada;
        const xo = document.getElementById('xo').value;
        dataToSend.xo = parseFloat(xo);
    }

    // Incluye xo si el método es 'newton'
    if (selectedMethod === 'newton') {
        apiUrl = '/api/newton';
        const xo = document.getElementById('xo_newton').value;
        dataToSend.xo_newton = parseFloat(xo);
    }

    // Incluye x0 y x1 si el método es 'secante'
    if (selectedMethod === 'secante') {
        apiUrl = '/api/secante';
        const x0 = document.getElementById('x0_sec').value;
        const x1 = document.getElementById('x1_sec').value;
        dataToSend.x0_sec = parseFloat(x0);
        dataToSend.x1_sec = parseFloat(x1);
    }


    // Incluye nVar y matriz si el método es 'jacobi'
    if (selectedMethod === 'jacobi') {
        apiUrl = '/api/jacobi';
        const nVar = document.getElementById('nVar_jac').value;
        const matriz = document.getElementById('matriz_jac').value;
        dataToSend.nVar_jac = parseFloat(nVar);
        dataToSend.matriz_jac = matriz;  // Envia la matriz como cadena de texto

        method_no_graphic = true
    }

    if (selectedMethod === 'gauss') {
        apiUrl = '/api/gauss';
        const nVar = document.getElementById('nVar_gau').value;
        const matriz = document.getElementById('matriz_gau').value;
        dataToSend.nVar_gau = parseFloat(nVar);
        dataToSend.matriz_gau = matriz;  // Envia la matriz como cadena de texto

        method_no_graphic = true
    }


    // Incluye a, b, número de trapecios si el método es 'trapecio'
    if (selectedMethod === 'trapecio') {
        apiUrl = '/api/trapecio';
        const a = document.getElementById('a_trap').value;
        const b = document.getElementById('b_trap').value;
        const num = document.getElementById('num_trap').value;

        dataToSend.a_trap = parseFloat(a);
        dataToSend.b_trap = parseFloat(b);
        dataToSend.num_trap = parseInt(num);
    }

    if (selectedMethod === 'simpson') {
        apiUrl = '/api/simpson';
        const a = document.getElementById('a_simp').value;
        const b = document.getElementById('b_simp').value;
        const num = document.getElementById('num_simp').value;

        dataToSend.a_simp = parseFloat(a);
        dataToSend.b_simp = parseFloat(b);
        dataToSend.num_simp = parseInt(num);
    }

    if (selectedMethod === 'euler') {
        apiUrl = '/api/euler';
        const x0 = document.getElementById('x0').value;
        const y0 = document.getElementById('y0').value;
        const h = document.getElementById('h').value;
        const n = document.getElementById('n').value;
        const expresion = document.getElementById('expression_euler').value;

        dataToSend.x0 = parseFloat(x0);
        dataToSend.y0 = parseFloat(y0);
        dataToSend.h = parseFloat(h);
        dataToSend.n = parseInt(n);
        dataToSend.expresion = expresion;
    }




    // Enviar datos al servidor usando Fetch API
     fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(dataToSend),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Respuesta del servidor:', data);

        if (data.alert_error) {
            alert(data.message);
            return;
        }

        if (!method_no_graphic) {
            if (selectedMethod === 'euler') {
                const eulerDisplay = document.getElementById('eulerDisplay');

                if (data.resultado) {
                    eulerDisplay.innerText = JSON.stringify(data.resultado, null, 2);

                    const x_vals = data.resultado.x;
                    const y_vals = data.resultado.y;
                    const y_real_vals = data.resultado.y_real

                    // Configurar las trazas del gráfico
                    const traces = [{
                        x: x_vals,
                        y: y_vals,
                        mode: 'lines+markers',
                        name: 'Aproximación Euler',
                        line: {color: '#1f77b4'} // Azul estándar de Plotly
                    }];

                    // Añadir solución exacta si existe y tiene valores
                    const hasRealSolution = y_real_vals.length > 0 && y_real_vals.some(y => y !== null);
                    if (hasRealSolution) {
                        traces.push({
                            x: x_vals,
                            y: y_real_vals,
                            mode: 'lines',
                            name: 'Solución Exacta',
                            line: {
                                color: '#ff7f0e', // Naranja estándar de Plotly
                                dash: 'dash'
                            }
                        });
                    }

                    // Configuración del layout
                    const layout = {
                        title: hasRealSolution 
                            ? 'Método de Euler vs Solución Exacta' 
                            : 'Aproximación con Método de Euler',
                        xaxis: { title: 'x' },
                        yaxis: { title: 'y' },
                        margin: {t: 40, b: 40, l: 50, r: 20},
                        hovermode: 'closest',
                        showlegend: true
                    };

                    // Dibujar el gráfico
                    const graphDiv = document.getElementById('graphDiv');
                    Plotly.newPlot(graphDiv, traces, layout);
                } else if (data.error) {
                    eulerDisplay.innerText = `Error: ${data.error}`;
                }
            } else {
                // Otros métodos con gráfica
                const graphDiv = document.getElementById('graphDiv');
                const graphData = JSON.parse(data.graph_data);
                Plotly.newPlot(graphDiv, graphData.data, graphData.layout);
            }
        } else {
            // Métodos sin gráfica
            if (selectedMethod === 'jacobi') {
                const jacobiDisplay = document.getElementById('jacobiDisplay');
                jacobiDisplay.innerText = `Solución Jacobi: ${data.solution}`;
            }
            if (selectedMethod === 'gauss') {
                const gaussDisplay = document.getElementById('gaussDisplay');
                gaussDisplay.innerText = `Solución Gauss: ${data.solution}`;
            }
            if (selectedMethod === 'euler') {
                const eulerDisplay = document.getElementById('eulerDisplay');
                eulerDisplay.innerText = `Solución Euler: ${data.solution}`;
            }
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

// Botones adicionales
document.getElementById('acceptFunction').addEventListener('click', function() {
    switchDisplayTransf = true;
});

document.getElementById('refreshButton').addEventListener('click', function() {
    location.reload(); // Recarga la página
});
