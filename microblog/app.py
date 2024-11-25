from flask import Flask, render_template, request
import sqlite3

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

@app.route('/check/<int:age>')
def check(age):
     return "You are " + str(age) + " years old"

@app.route('/check1/<int:adult>')
def check1(adult):
     if adult >= 18:
          return "You're officially an adult"
     if adult < 18:
          return "Get out, child"

@app.route('/check2/<float:bulletin>')
def check2(bulletin):
     if bulletin >=7:
          return "passou miseravi"
     elif bulletin <7 and bulletin >=3:
          return "oooo recuperaçãum"
     else:
          return "fora."

@app.route('/logar')
def logar():
    user = request.form["admin"]
    passw = request.form["345"]

    if user == "admin" and passw == "345":
         return "your account info"
    else:
         return "wrong, bye"