from flask import Flask, render_template, request
app = Flask (__name__)
@app.route('/')
def index():
    return render_template("index.html", count = "67")

@app.route("/contact")
def contato():
    return render_template("contact.html", phone = "(87) 94002-8922")

@app.route("/biography")
def bio():
    return render_template("bio.html", bio = "Conversey")

@app.route("/products")
def products():
    return render_template("products.html", disclaimer = "Please note that at this time, our shoes are available for in-store purchase only. We do not offer delivery services. We appreciate your understanding and encourage you to visit us to try on and purchase your favorite pairs!")

@app.route("/soma/<int:num1>/<int:num2>")
@app.route("/calculadora/")
def continha (num1, num2):
    soma = num1 + num2
    subtracao = num1 - num2
    divisao = num1 / num2
    multiplicacao = num1 * num2
    return f"Soma: {soma}, Subtração: {subtracao}, Divisão: {divisao}, Multiplicação: {multiplicacao}"

@app.route('/formulario', methods = ["GET", "POST"])
def formulario():
    if request.method == "GET":
        return render_template("dados.html")
    elif request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        msg = request.form["mensagem"]
        return f{"Nome: {nome}, Email: {email}, Mensagem: {msg}"}

if __name__ == '__main__':
    app.run()