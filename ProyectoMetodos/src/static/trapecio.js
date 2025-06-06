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

        if (selectedMethod === 'trapecio') {
            handleTrapecioResponse(data);
        } else if (!method_no_graphic) {
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

function handleTrapecioResponse(data) {
    // Mostrar la tabla de áreas individuales
    displayTrapecioTable(data.detalle_trapecios, data.solution);
    
    // Crear gráfica con trapecios de colores
    createTrapecioChart(data);
}

function displayTrapecioTable(detalleTrapecios, solucionTotal) {
    // Crear o actualizar la tabla de resultados
    let tableContainer = document.getElementById('trapecioTableContainer');
    
    if (!tableContainer) {
        tableContainer = document.createElement('div');
        tableContainer.id = 'trapecioTableContainer';
        tableContainer.style.marginTop = '20px';
        
        // Insertar después del gráfico o en un contenedor específico
        const graphDiv = document.getElementById('graphDiv');
        graphDiv.parentNode.insertBefore(tableContainer, graphDiv.nextSibling);
    }

    let tableHTML = `
        <h3>Resultados del Método del Trapecio</h3>
        <p><strong>Área Total: ${solucionTotal.toFixed(6)}</strong></p>
        <table style="border-collapse: collapse; width: 100%; margin-top: 10px; border: 1px solid #ddd;">
            <thead style="background-color: #f2f2f2;">
                <tr>
                    <th style="border: 1px solid #ddd; padding: 8px; text-align: center;">Trapecio</th>
                    <th style="border: 1px solid #ddd; padding: 8px; text-align: center;">Intervalo</th>
                    <th style="border: 1px solid #ddd; padding: 8px; text-align: center;">f(x₀)</th>
                    <th style="border: 1px solid #ddd; padding: 8px; text-align: center;">f(x₁)</th>
                    <th style="border: 1px solid #ddd; padding: 8px; text-align: center;">Área</th>
                    <th style="border: 1px solid #ddd; padding: 8px; text-align: center;">Color</th>
                </tr>
            </thead>
            <tbody>
    `;

    const colors = generateTrapecioColors(detalleTrapecios.length);
    
    detalleTrapecios.forEach((trapecio, index) => {
        const color = colors[index];
        tableHTML += `
            <tr>
                <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">${trapecio.trapecio}</td>
                <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">[${trapecio.intervalo[0].toFixed(3)}, ${trapecio.intervalo[1].toFixed(3)}]</td>
                <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">${trapecio.base_izq.toFixed(6)}</td>
                <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">${trapecio.base_der.toFixed(6)}</td>
                <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">${trapecio.area.toFixed(6)}</td>
                <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">
                    <div style="width: 20px; height: 20px; background-color: ${color}; margin: 0 auto; border: 1px solid #000;"></div>
                </td>
            </tr>
        `;
    });

    tableHTML += `
            </tbody>
        </table>
    `;

    tableContainer.innerHTML = tableHTML;
}

function generateTrapecioColors(numTrapecios) {
    const colors = [];
    const hueStep = 360 / numTrapecios;
    
    for (let i = 0; i < numTrapecios; i++) {
        const hue = (i * hueStep) % 360;
        const color = `hsla(${hue}, 70%, 60%, 0.7)`;
        colors.push(color);
    }
    
    return colors;
}

function createTrapecioChart(data) {
    const graphDiv = document.getElementById('graphDiv');
    const graphData = JSON.parse(data.graph_data);
    
    // Generar colores para los trapecios
    const colors = generateTrapecioColors(data.detalle_trapecios.length);
    
    // Crear trazas individuales para cada trapecio
    const trapecioTraces = [];
    
    data.detalle_trapecios.forEach((trapecio, index) => {
        const x0 = trapecio.intervalo[0];
        const x1 = trapecio.intervalo[1];
        const y0 = trapecio.base_izq;
        const y1 = trapecio.base_der;
        
        // Crear el trapecio como un polígono
        const trapecioTrace = {
            x: [x0, x1, x1, x0, x0],
            y: [0, 0, y1, y0, 0],
            fill: 'toself',
            fillcolor: colors[index],
            line: {
                color: colors[index].replace('0.7', '1'), // Color más sólido para el borde
                width: 2
            },
            name: `Trapecio ${index + 1} (Área: ${trapecio.area.toFixed(4)})`,
            type: 'scatter',
            mode: 'lines',
            hovertemplate: `<b>Trapecio ${index + 1}</b><br>` +
                         `Intervalo: [${x0.toFixed(3)}, ${x1.toFixed(3)}]<br>` +
                         `f(${x0.toFixed(3)}) = ${y0.toFixed(4)}<br>` +
                         `f(${x1.toFixed(3)}) = ${y1.toFixed(4)}<br>` +
                         `Área: ${trapecio.area.toFixed(6)}<extra></extra>`
        };
        
        trapecioTraces.push(trapecioTrace);
    });
    
    // Combinar las trazas originales con las de los trapecios
    const allTraces = [...graphData.data, ...trapecioTraces];
    
    // Actualizar el layout
    const updatedLayout = {
        ...graphData.layout,
        title: `${graphData.layout.title}<br><sub>Área Total: ${data.solution.toFixed(6)}</sub>`,
        showlegend: true,
        legend: {
            x: 1,
            y: 1,
            xanchor: 'left',
            yanchor: 'top'
        }
    };
    
    Plotly.newPlot(graphDiv, allTraces, updatedLayout);
}