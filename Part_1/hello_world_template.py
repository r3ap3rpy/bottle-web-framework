from bottle import run, route, template

@route('/')
def index():
	return template("Hello {{name}}, welcome to bottle!",name = 'Stranger')

run(host = 'localhost', port = 8080, debug = True)
