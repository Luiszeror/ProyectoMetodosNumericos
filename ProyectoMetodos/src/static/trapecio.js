document.getElementById('sendTrapecio').addEventListener('click', function(event) {
    event.preventDefault(); 
    const functionInput = document.getElementById('display').value;
    const selectedMethod = document.getElementById('method').value;

    let dataToSend = {
        function: functionInput,
        method: selectedMethod
    };

    let apiUrl = '';

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
        
            // Otros métodos con gráfica
            const graphDiv = document.getElementById('graphDiv');
            const graphData = JSON.parse(data.graph_data);
            Plotly.newPlot(graphDiv, graphData.data, graphData.layout);
            
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