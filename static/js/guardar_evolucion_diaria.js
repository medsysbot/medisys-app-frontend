document.addEventListener("DOMContentLoaded", function () {
    const botonGuardar = document.getElementById("guardarEvolucionBtn");

    if (botonGuardar) {
        botonGuardar.addEventListener("click", async function () {
            const texto = document.getElementById("evolucionTexto")?.value;

            if (!texto) {
                alert("Por favor, escribe la evolución antes de guardar.");
                return;
            }

            try {
                const response = await fetch("/guardar_evolucion_diaria", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({ evolucion: texto }),
                });

                if (response.ok) {
                    alert("Evolución diaria guardada correctamente.");
                } else {
                    alert("Error al guardar la evolución. Intenta nuevamente.");
                }
            } catch (error) {
                console.error("Error:", error);
                alert("Error al conectar con el servidor.");
            }
        });
    }
});
