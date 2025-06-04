document.getElementById('sendEuler').addEventListener('click', function(event) {
    event.preventDefault(); 
    const functionInput = document.getElementById('display').value;
    const selectedMethod = document.getElementById('method').value;

    let dataToSend = {
        function: functionInput,
        method: selectedMethod
    };

    let apiUrl = '';
    

    if (selectedMethod === 'euler') {
        apiUrl = '/api/euler';
        const x0 = document.getElementById('x0').value;
        const y0 = document.getElementById('y0').value;
        const h = document.getElementById('h').value;
        const n = document.getElementById('n').value;
        const expresion = document.getElementById('display').value;

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
                    let htmlContent = `
                        <div class="euler-results">
                            <h4>Resultados del Método de Euler</h4>
                            <div class="params">
                                <p><strong>Parámetros:</strong> 
                                x₀ = ${data.resultado.x[0]}, y₀ = ${data.resultado.y[0]}, 
                                h = ${data.resultado.h}, iteraciones = ${data.resultado.n}</p>
                            </div>
                            <div class="table-responsive">
                                <table class="table table-bordered table-striped">
                                    <thead class="thead-dark">
                                        <tr>
                                            <th>Iteración</th>
                                            <th>x</th>
                                            <th>y (Euler)</th>
                                            ${data.resultado.y_real ? '<th>y (Exacto)</th><th>Error</th>' : ''}
                                        </tr>
                                    </thead>
                                    <tbody>`;
                        
                        // Llenar la tabla con los datos
                        for (let i = 0; i <= data.resultado.n; i++) {
                            htmlContent += `
                                <tr>
                                    <td>${i}</td>
                                    <td>${data.resultado.x[i].toFixed(6)}</td>
                                    <td>${data.resultado.y[i].toFixed(6)}</td>`;
                            
                            if (data.resultado.y_real) {
                                const error = data.resultado.y_real[i] !== undefined ? 
                                    Math.abs(data.resultado.y[i] - data.resultado.y_real[i]).toFixed(6) : 'N/A';
                                
                                htmlContent += `
                                    <td>${data.resultado.y_real[i] ? data.resultado.y_real[i].toFixed(6) : 'N/A'}</td>
                                    <td>${error}</td>`;
                            }
                            
                            htmlContent += `</tr>`;
                        }
                        
                        htmlContent += `
                                    </tbody>
                                </table>
                            </div>
                            <div class="summary">
                                <p><strong>Resumen:</strong></p>
                                <ul>
                                    <li>Valor final aproximado: ${data.resultado.y[data.resultado.n].toFixed(6)}</li>
                                    ${data.resultado.y_real ? 
                                    `<li>Valor final exacto: ${data.resultado.y_real[data.resultado.n].toFixed(6)}</li>
                                    <li>Error final: ${Math.abs(data.resultado.y[data.resultado.n] - data.resultado.y_real[data.resultado.n]).toFixed(6)}</li>` : ''}
                                </ul>
                            </div>
                        </div>`;
                        
                        // Reemplaza la asignación al textarea por:
                        document.getElementById('eulerResultsContainer').innerHTML = htmlContent;

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
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});