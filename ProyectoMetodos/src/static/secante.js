document.getElementById('sendSecante').addEventListener('click', function(event) {
    event.preventDefault(); 
    const functionInput = document.getElementById('display').value;
    const selectedMethod = document.getElementById('method').value;

    let dataToSend = {
        function: functionInput,
        method: selectedMethod
    };

    let apiUrl = '';

    // Incluye x0 y x1 si el método es 'secante'
    if (selectedMethod === 'secante') {
        apiUrl = '/api/secante';
        const x0 = document.getElementById('x0_sec').value;
        const x1 = document.getElementById('x1_sec').value;
        dataToSend.x0_sec = parseFloat(x0);
        dataToSend.x1_sec = parseFloat(x1);
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
            
        } else {}
    })
    .catch((error) => {
        alert("Hubo un error al calcular la raíz: " + error.message);
    });
});