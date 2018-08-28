from bottle import route, run, install,template, request
from bottle_sqlite import SQLitePlugin

install(SQLitePlugin(dbfile=r'.\\inventory.db'))


@route('/show/<devicename>')
def show_device(db,devicename):
	command = db.execute('SELECT id,name,os from devices where name = ?',(devicename,))
	row = command.fetchone() or None
	if row:
		return template('{{id}},{{name}},{{os}}',id = row['id'],name=row['name'],os=row['os'])
	else:
		return template('The specified device with the name: {{name}}, could not be found!', name=devicename)

@route('/show')
def querylike(db):
	os = request.query.os or None
	id = request.query.id or None
	name = request.query.name or None
	querystring = []

	if os:
		querystring.append("os='{}'".format(os))

	if id:
		querystring.append('id={}'.format(id))

	if name:
		querystring.append("name='{}'".format(name))

	if len(querystring) == 0:
		return 'Invalid query!'
	else:
		query = 'SELECT id,name,os from devices where {}'.format(' AND '.join(querystring))
		print(query)
		command = db.execute(query)
		row = command.fetchone() or None

		if row:
			return template('{{id}},{{name}},{{os}}',id = row['id'],name=row['name'],os=row['os'])
		else:
			return template('The specified device with the specification: {{name}}, could not be found!', name=' AND '.join(querystring))


run(host = 'localhost', port = 8080, debug = True)