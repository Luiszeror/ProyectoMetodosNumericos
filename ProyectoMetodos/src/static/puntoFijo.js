document.getElementById('sendpuntoFijo').addEventListener('click', function(event) {
    event.preventDefault(); 
    const functionInput = document.getElementById('display').value;
    const selectedMethod = document.getElementById('method').value;

    let dataToSend = {
        function: functionInput,
        method: selectedMethod
    };

    let apiUrl = ''; 
    // Incluye xo y la transformada si el método es 'puntoFijo'
    if (selectedMethod === 'puntoFijo') {
        apiUrl = '/api/punto_fijo';
        const transformada = document.getElementById('transformada').value;
        dataToSend.transformada = transformada;
        const xo = document.getElementById('xo').value;
        dataToSend.xo = parseFloat(xo);
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

        const graphDiv = document.getElementById('graphDiv');
        const graphData = JSON.parse(data.graph_data);
        Plotly.newPlot(graphDiv, graphData.data, graphData.layout);

    })
    .catch((error) => {
        console.error('Error:', error);
    });
});