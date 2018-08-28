from bottle import get, post, delete, run

@get('/')
def index():
	return 'Welcome to bottle project!'

@post('/')
def index_post():
	return 'Welcome from POST to bottle project!'

@delete('/')
def index_delete():
	return 'Welcome from DELETE to bottle project!'


run(host = 'localhost', port = 8080, debug = True)
