from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
 return "<h1> Flask + Gunicorn + Nginx funcionando en Docker</h1>"
@app.route("/saludo/<nombre>")
def saludo(nombre):
 return f"<h2>Hola, {nombre.capitalize()}!</h2>"
if __name__ == "__main__":
 app.run(host="0.0.0.0", port=5000)