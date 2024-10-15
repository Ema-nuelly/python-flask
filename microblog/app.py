from flask import Flask
app = Flask (__name__)
@app.route('/')
def index():
    return '<h2>                                                     oieee'
if __name__ == '__main__':
    app.run()