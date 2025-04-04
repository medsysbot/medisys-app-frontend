document.addEventListener("DOMContentLoaded", function () {
    const botonGuardar = document.getElementById("guardarResumenBtn");

    if (botonGuardar) {
        botonGuardar.addEventListener("click", async function () {
            const texto = document.getElementById("resumenTexto")?.value;

            if (!texto) {
                alert("Por favor, escribe el resumen antes de guardar.");
                return;
            }

            try {
                const response = await fetch("/guardar_historia_resumida", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({ resumen: texto }),
                });

                if (response.ok) {
                    alert("Historia resumida guardada correctamente.");
                } else {
                    alert("Error al guardar el resumen. Intenta nuevamente.");
                }
            } catch (error) {
                console.error("Error:", error);
                alert("Error al conectar con el servidor.");
            }
        });
    }
});
