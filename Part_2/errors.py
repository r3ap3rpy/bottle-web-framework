from bottle import error, route, run, abort

@error(404)
def not_found(error):
	return 'The requested conted was not found!'

@error(401)
def not_found(error):
	return 'You shall not pass!!!!!'

@route('/')
def index():
	return 'Welcome to bottle!'

@route('/youshallnotpass')
def shallnotpass():
	abort(401)

run(host = 'localhost', port = 8080, debug = True)