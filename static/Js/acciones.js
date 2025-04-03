
function guardarFormulario() {
  alert("Formulario guardado.");  // Esto después se conecta al backend real
}

function eliminarFormulario() {
  const form = document.querySelector("form");
  if (form) form.reset();
}
