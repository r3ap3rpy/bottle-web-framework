from bottle import route, run, request

@route('/', method=['GET','POST','DELETE'])
def index():
	if request.method == 'GET':
		return 'Welcome to bottle project!'
	elif request.method == 'POST':
		return 'Welcome from POST to bottle project!'
	elif request.method == 'DELETE':
		return 'Welcome from DELETE to bottle project!'
	


run(host = 'localhost', port = 8080, debug = True)
