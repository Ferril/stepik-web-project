def app(environ, start_response):
	status = '200 OK'
	data ='\n'.join(environ['QUERY_STRING'].split('&'))
	start_response(status, [('Content-Type', 'text/plain')])
	return [data.strip().encode()]
