import socket
import sys


# https://docs.python.org/3/library/socket.html

"""HOST = None # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
print('Socket bind complete')
s.listen(10)
print('Socket now listening')
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
    data = conn.recv(1024)
    reply = 'Received: ' + data
    if not data:
        break
    conn.sendall(reply)
    conn.close()
s.close()"""
from requests.models import Response
the_response = Response()
the_response.code = "expired"
the_response.error_type = "expired"
the_response.status_code = 400
the_response._content = b'{ "key" : "a" }'

print(the_response.json())


# Echo server program
import socket
import sys

HOST = None               # Symbolic name meaning all available interfaces
PORT = 50009              # Arbitrary non-privileged port
s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
                              socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except OSError as msg:
        s = None
        continue
    try:
        s.bind(sa)
        s.listen(1)
    except OSError as msg:
        s.close()
        s = None
        continue
    print(str(res))
    break
if s is None:
    print('could not open socket')
    sys.exit(1)
print('listening')
conn, addr = s.accept()
with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data: break
        conn.send(data)
        #conn.send(the_response)
