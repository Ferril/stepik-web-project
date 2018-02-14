def app(environ, start_response):
	status = '200 OK'
	start_response(status, [('Content-Type', 'text/plain')])
	data ='\r\n'.join(environ['QUERY_STRING'].split('&'))
	return data
