document.addEventListener("DOMContentLoaded", function () {
    const botonGuardar = document.getElementById("guardarHistoriaBtn");

    if (botonGuardar) {
        botonGuardar.addEventListener("click", async function () {
            const texto = document.getElementById("historiaTexto")?.value;

            if (!texto) {
                alert("Por favor, escribe la historia clínica antes de guardar.");
                return;
            }

            try {
                const response = await fetch("/guardar_historia_completa", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({ historia: texto }),
                });

                if (response.ok) {
                    alert("Historia clínica guardada correctamente.");
                } else {
                    alert("Error al guardar la historia. Intenta nuevamente.");
                }
            } catch (error) {
                console.error("Error:", error);
                alert("Error al conectar con el servidor.");
            }
        });
    }
});
