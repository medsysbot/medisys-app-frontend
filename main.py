from flask import Flask, render_template

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registro")
def registro():
    return render_template("registro.html")

# 🔹 Agregá más rutas cuando lo necesites (historia, receta, etc.)

if __name__ == "__main__":
    app.run(debug=True)
