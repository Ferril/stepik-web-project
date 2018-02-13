def app(environ, start_response):
	status = '200 OK'
	start_response(status, [('Content-Type', 'text/plain')])
	q_strinq = environ['QUERY_STRING'].split('&')
	resp = ''
	for x in q_string:
		resp += x + '\n'
	return resp
