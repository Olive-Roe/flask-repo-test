from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Hello World! </h1>'

@app.route('/<name>')
def index2(name):
    return '<h1> Hello, {}! Nice to meet you. </h1>'.format(name)

if __name__  == "__main__":
    app.run(debug=True)


