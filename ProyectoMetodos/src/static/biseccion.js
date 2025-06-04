document.getElementById('sendBiseccion').addEventListener('click', function(event) {
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
        console.error('Error:', error);
    });
});