from flask import Flask
app = Flask (__name__)
@app.route('/')
def index():
    return 'oieee'

@app.route("/contato")
def contato():
    return '+5587996222499'
if __name__ == '__main__':
    app.run()