from bottle import static_file, route, run, static_file

@route('/show/<file>')
def show(file):
	return static_file(file, root = r'.\\')

@route('/download/<file>')
def download(file):
	return static_file(file, root = r'.\\', download = file)

run(host = 'localhost', port = 8080, debug = True)