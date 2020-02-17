import flask
app=flask.Flask(__name__)
print(__name__)
@app.route('/')
def hello():
    return 'hello world'
@app.route('/hi')
def hi():
    return 'hi world'

if __name__=='__main__':
    app.run()