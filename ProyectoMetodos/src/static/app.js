let method_no_graphic = false; 
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

window.latexToSymPy = function (latex) {
    return latex
        .replace(/\\cdot/g, '*')
        .replace(/\^/g, '**')
        .replace(/\\sqrt{([^}]*)}/g, 'sqrt($1)')
        .replace(/\\sqrt\s*([0-9a-zA-Z\.]+)/g, 'sqrt($1)')
        .replace(/\\frac\s*([0-9a-zA-Z]+)\s*([0-9a-zA-Z]+)/g, '($1/$2)')
        .replace(/\\frac{([^}]*)}{([^}]*)}/g, '($1/$2)')
        .replace(/\\sin/g, 'sin')
        .replace(/\\cos/g, 'cos')
        .replace(/\\tan/g, 'tan')
        .replace(/\\log/g, 'log')
        .replace(/\\ln/g, 'log')
        .replace(/\\exp/g, 'exp')
        .replace(/\\pi/g, 'pi')
        .replace(/\\e/g, 'E')
        .replace(/\\left\(/g, '(')
        .replace(/\\right\)/g, ')');
};

window.addEventListener('DOMContentLoaded', () => {
    const mathField = document.getElementById('displayMath');
    
    const hiddenInput = document.getElementById('display');

    if (mathField && hiddenInput) {
        mathField.addEventListener('input', (e) => {
            const latex = e.target.value;
            const converted = window.latexToSymPy(latex);
            hiddenInput.value = converted;

            console.log("LaTeX:", latex);
            console.log("Convertido para SymPy:", converted);
        });
    } else {
        console.warn("No se encontró el campo displayMath o display");
    }
});

window.addEventListener('DOMContentLoaded', () => {
    const mathField = document.getElementById('transformadaMath');

    const hiddenInput = document.getElementById('transformada');

    if (mathField && hiddenInput) {
        mathField.addEventListener('input', (e) => {
            const latex = e.target.value;
            const converted = window.latexToSymPy(latex);
            hiddenInput.value = converted;

            console.log("LaTeX:", latex);
            console.log("Convertido para SymPy:", converted);
        });
    } else {
        console.warn("No se encontró el campo transformadaMath o transformada");
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

    method_no_graphic = false; 

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

document.getElementById('refreshButton').addEventListener('click', function() {
    location.reload(); // Recarga la página
});
