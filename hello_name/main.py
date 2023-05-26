from bottle import Bottle, request, run, template

app = Bottle()

@app.route('/')
def ask_name():
    return template('name_form')

@app.route('/hello', method='GET')
def hello():
    name = request.query.name
    return template('hello', name=name)

run(app, host='localhost', port=8080, debug=True)
