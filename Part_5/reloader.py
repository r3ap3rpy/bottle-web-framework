from bottle import route, run

@route('/')
def index():
	return 'Welcome'

@route('/anothercontextroute')
def anothercontextroute():
	return 'Just another context route!'

run(host='localhost', port = 8080, reloader=True, debug = True)