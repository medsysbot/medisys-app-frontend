function imprimirPDF() {
    const iframe = document.querySelector('iframe');
    if (iframe && iframe.contentWindow) {
        iframe.contentWindow.focus();
        iframe.contentWindow.print();
    } else {
        alert("No se encontró el documento PDF para imprimir.");
    }
}

function eliminarPDF() {
    const visor = document.getElementById('pdf-visor');
    if (visor) {
        visor.setAttribute('src', '');
        alert("PDF eliminado del visor.");
    }
}

function enviarFormulario(formId) {
    const form = document.getElementById(formId);
    if (form) {
        form.submit();
    } else {
        alert("Formulario no encontrado.");
    }
}
