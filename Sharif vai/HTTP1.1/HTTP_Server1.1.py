from http.server import HTTPServer, SimpleHTTPRequestHandler
import time

from requests.models import Response



class MyRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        start_time = time.time()  # Record start time
        # Serve files from the current directory
        SimpleHTTPRequestHandler.do_GET(self)
        end_time = time.time()  # Record end time
        transfer_time = end_time - start_time
        print(f"Transfer Time: {transfer_time} seconds")

server_address = ('', 8000)  # Listen on all interfaces on port 8000
httpd = HTTPServer(server_address, MyRequestHandler)
print('Server started on port 8000...')
httpd.serve_forever()
