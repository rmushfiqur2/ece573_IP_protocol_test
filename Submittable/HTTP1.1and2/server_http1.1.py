from http.server import HTTPServer, SimpleHTTPRequestHandler

class MyRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        SimpleHTTPRequestHandler.do_GET(self)


server_address = ('', 8000)  # Listen on all interfaces on port 8000
httpd = HTTPServer(server_address, MyRequestHandler)
print('Server started on port 8000...')
httpd.serve_forever()