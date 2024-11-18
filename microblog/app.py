from flask import Flask, render_template, request
app = Flask (__name__)
app.run(debug=True)
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
def continha(num1, num2):
    soma = num1 + num2
    subtracao = num1 - num2
    divisao = num1 / num2
    multiplicacao = num1 * num2
    return render_template(
        "calc.html",
        soma=soma,
        subtracao=subtracao,
        divisao=divisao,
        multiplicacao=multiplicacao
    )

@app.route("/dados")
def dados():
    return render_template("dados.html")

@app.route("/recebedados", methods=['POST'])
def recebedados():
    nome = request.form.get('nome')
    return nome

@app.route('/recebedados1', methods=['POST'])
def recebedados1():
	estado = request.form['estado'] 
                    
@app.route('/recebedados2', methods=['POST'])
def recebedados2():
	formacao = request.form['formacao']
                          
if __name__ == '__main__':
    app.run()

