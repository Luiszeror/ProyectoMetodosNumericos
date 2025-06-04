document.getElementById('sendSimpson').addEventListener('click', function(event) {
    event.preventDefault(); 
    const functionInput = document.getElementById('display').value;
    const selectedMethod = document.getElementById('method').value;

    let dataToSend = {
        function: functionInput,
        method: selectedMethod
    };

    let apiUrl = '';

    if (selectedMethod === 'simpson') {
        apiUrl = '/api/simpson';
        const a = document.getElementById('a_simp').value;
        const b = document.getElementById('b_simp').value;
        const num = document.getElementById('num_simp').value;

        dataToSend.a_simp = parseFloat(a);
        dataToSend.b_simp = parseFloat(b);
        dataToSend.num_simp = parseInt(num);
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
            
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});