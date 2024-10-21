from flask import Flask, render_template
app = Flask (__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/contact")
def contato():
    return render_template("contact.html")
@app.route("/home")
def home():
    return 'HOME SWEET HOME'
if __name__ == '__main__':
    app.run()