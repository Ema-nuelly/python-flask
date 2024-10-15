from flask import Flask
app = Flask (__name__)
@app.route('/')
def index():
    return '<h2>quero ir embora pra minha casinha dormir<h2>'
if __name__ == '__main__':
    app.run()