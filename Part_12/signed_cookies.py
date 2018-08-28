from bottle import get, post, route, request, response, run, redirect

allowed_account = ['admin','user','poweruser']

@get('/')
def index():
	return """
		<form action="/" method="post">
		Username: <input name="username" type="text" />
		Password: <input name="password" type="password" />
		<input value="Login" type="submit" />
		</form>
	"""

@post('/')
def index():
	username = request.forms.get('username')
	password = request.forms.get('password')
	if username == 'admin' and password == 'password':
		response.set_cookie('account', username, secret = 'MySuperSecretSignedCookie')		
		return redirect('/restricted')
	elif username == 'user' and password == 'pass':
		response.set_cookie('account', username, secret = 'MySuperSecretSignedCookie')		
		return redirect('/restricted')
	elif username == 'poweruser' and password == 'ass':
		response.set_cookie('account', username, secret = 'MySuperSecretSignedCookie')		
		return redirect('/restricted')
	else:
		return redirect('/')

@get('/restricted') 
def restricted():
	username = request.get_cookie('account', secret = 'MySuperSecretSignedCookie')
	if username:
		return 'Welcome: {} to the restricted area!'.format(username)
	else:
		return 'You are not authorized'

run(host = 'localhost', port = 8080, debug = True)