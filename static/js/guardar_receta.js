document.addEventListener("DOMContentLoaded", function () {
    const botonGuardar = document.getElementById("guardarRecetaBtn");

    if (botonGuardar) {
        botonGuardar.addEventListener("click", async function () {
            const receta = document.getElementById("textoReceta")?.value;

            if (!receta) {
                alert("Por favor, escribe la receta antes de guardar.");
                return;
            }

            try {
                const response = await fetch("/guardar_receta", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({ receta: receta }),
                });

                if (response.ok) {
                    alert("Receta guardada correctamente.");
                } else {
                    alert("Error al guardar la receta. Intenta nuevamente.");
                }
            } catch (error) {
                console.error("Error:", error);
                alert("Error al conectar con el servidor.");
            }
        });
    }
});
