from flask import Flask, render_template
app = Flask (__name__)
@app.route('/')
def index():
    return render_template("index.html", hour = "19:06")

@app.route("/contact")
def contato():
    return render_template("contact.html", phone = "(87) 94002-8922")

@app.route("/biography")
def bio():
    return render_template("bio.html", bio = "Conversey")

@app.route("/products")
def products():
    return render_template("products.html", disclaimer = "Conversey")

if __name__ == '__main__':
    app.run()