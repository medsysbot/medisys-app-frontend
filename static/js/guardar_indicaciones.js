document.addEventListener("DOMContentLoaded", function () {
    const botonGuardar = document.getElementById("guardarIndicacionesBtn");

    if (botonGuardar) {
        botonGuardar.addEventListener("click", async function () {
            const indicaciones = document.getElementById("textoIndicaciones")?.value;

            if (!indicaciones) {
                alert("Por favor, escribe las indicaciones antes de guardar.");
                return;
            }

            try {
                const response = await fetch("/guardar_indicaciones", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({ indicaciones: indicaciones }),
                });

                if (response.ok) {
                    alert("Indicaciones guardadas correctamente.");
                } else {
                    alert("Error al guardar las indicaciones. Intenta nuevamente.");
                }
            } catch (error) {
                console.error("Error:", error);
                alert("Error al conectar con el servidor.");
            }
        });
    }
});
