from http.server import HTTPServer, SimpleHTTPRequestHandler #2
#the HTTPServer class from the http.server module to create an HTTP server that listens for TCP connections.
#2 handles HTTP GET requests by serving files from the current directory and its subdirectories. It's a simple
  # way to set up an HTTP server for serving static files.
import socket

class SingleTCPHTTPServer(HTTPServer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.connections = []

    def process_request(self, request, client_address):
        if self.connections:
            # If there's an existing connection, close the new one
            request.close()
        else:
            # Accept the new connection and store it
            self.connections.append(request)
            super().process_request(request, client_address)
            print('new')

    def close_request(self, request):
        self.connections.remove(request)
        super().close_request(request)

class MyRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Serve files from the current directory
        SimpleHTTPRequestHandler.do_GET(self)

server_address = ('', 8890)  # Listen on all interfaces on port 8889
httpd = SingleTCPHTTPServer(server_address, MyRequestHandler)

print('Server started on port 8890')
httpd.serve_forever()