from bottle import route, run, template, request

# /wikipage?pageid=10&section=b

@route('/wikipage')
def wiki_page():
	pageid = request.query.pageid or '1'
	section = request.query.section or 'a'
	return template("The requested wiki page {{pageid}} section {{section}}",pageid = pageid, section = section)

run(host = 'localhost', port = 8080, debug = True)
