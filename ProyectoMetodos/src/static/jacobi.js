document.getElementById('nVar_jac').addEventListener('change', function() {
    const nVar = parseInt(this.value);
    const header = document.getElementById('matrix_header_jac');
    const body = document.getElementById('matrix_body_jac');
    
    // Limpiar la tabla
    header.innerHTML = '';
    body.innerHTML = '';
    
    // Generar encabezados (x1, x2, ..., xn | r)
    for (let i = 1; i <= nVar; i++) {
        const th = document.createElement('th');
        th.textContent = `x${i}`;
        header.appendChild(th);
    }
    const thResult = document.createElement('th');
    thResult.textContent = 'r';
    header.appendChild(thResult);
    
    // Generar filas de la matriz (nVar filas)
    for (let i = 0; i < nVar; i++) {
        const tr = document.createElement('tr');
        
        // Campos para coeficientes
        for (let j = 0; j < nVar; j++) {
            const td = document.createElement('td');
            const input = document.createElement('input');
            input.type = 'number';
            input.className = 'form-control matrix-input';
            input.placeholder = `a${i+1}${j+1}`;
            input.dataset.row = i;
            input.dataset.col = j;
            td.appendChild(input);
            tr.appendChild(td);
        }
        
        // Campo para término independiente
        const tdResult = document.createElement('td');
        const inputResult = document.createElement('input');
        inputResult.type = 'number';
        inputResult.className = 'form-control matrix-input';
        inputResult.placeholder = `r${i+1}`;
        inputResult.dataset.row = i;
        inputResult.dataset.col = nVar; // Última columna
        tdResult.appendChild(inputResult);
        tr.appendChild(tdResult);
        
        body.appendChild(tr);
    }
});
document.getElementById('sendJacobi').addEventListener('click', function(event) {
    event.preventDefault(); 
    const functionInput = document.getElementById('display').value;
    const selectedMethod = document.getElementById('method').value;

    let dataToSend = {
        function: functionInput,
        method: selectedMethod
    };

    let apiUrl = '';

    // Incluye nVar y matriz si el método es 'jacobi'
    if (selectedMethod === 'jacobi') {
        const nVar = parseInt(document.getElementById('nVar_jac').value);
        const inputs = document.querySelectorAll('.matrix-input');
        const matrix = [];
        let currentRow = [];

        inputs.forEach((input, index) => {
            const value = input.value || '0'; // Default a 0 si está vacío
            currentRow.push(value);

            // Al completar una fila (nVar+1 elementos)
            if ((index + 1) % (nVar + 1) === 0) {
                matrix.push(currentRow.join(','));
                currentRow = [];
            }
        });

        apiUrl = '/api/jacobi';
        dataToSend.nVar_jac = nVar;
        dataToSend.matriz_jac = matrix.join('\n');

        console.log('Datos enviados:', dataToSend);
        method_no_graphic = true;
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

            // Métodos sin gráfica
        if (selectedMethod === 'jacobi') {
            const jacobiDisplay = document.getElementById('jacobiDisplay');
            const solutionArray = data.solution.split(',').map(s => s.trim());

            let formattedSolution = 'Solución Jacobi:\n';
            solutionArray.forEach((val, i) => {
                formattedSolution += `x${i + 1} = ${val}\n`;
            });

            jacobiDisplay.value = formattedSolution;
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
