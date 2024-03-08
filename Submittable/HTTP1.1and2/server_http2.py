import json
import socket
import os

import h2.connection
import h2.events
import h2.config

import os
import math
from hyperframe.frame import SettingsFrame
from hyper import HTTP20Connection
#!pip install h2==2.6
#!pip install hyper==0.7.0
# changed values in h2.settings

def send_request_header_as_response(conn, event):
    stream_id = event.stream_id
    #print(dict(event.headers).keys())
    #print(dict(event.headers).values())
    response_data = json.dumps(dict(event.headers)).encode('utf-8')

    conn.send_headers(
        stream_id=stream_id,
        headers=[
            (':status', '200'),
            ('server', 'basic-h2-server/1.0'),
            ('content-length', str(len(response_data))),
            ('content-type', 'application/json'),
        ],
    )
    conn.send_data(
        stream_id=stream_id,
        data=response_data,
        end_stream=True
    )

def send_chunked_response(conn, event):
    chunk_size = 10000 # bytes
    stream_id = event.stream_id

    my_path = './' + dict(event.headers)[':path']

    if my_path == './':
        print('root')
        response_data = b'Welcome to our server'
        response_code = str(200)
        content_type = 'text/plain'
        response_size = str(len(response_data))
        conn.send_headers(
            stream_id=stream_id,
            headers=[
                (':status', response_code),
                ('server', 'basic-h2-server/1.0'),
                ('content-length', response_size),
                ('content-type', content_type),
            ],
        )
        conn.send_data(
            stream_id=stream_id,
            data=response_data,
            end_stream=False
        )
    else:
        if os.path.isfile(my_path):
            #print('file found')
            file_size = os.path.getsize(my_path)
            response_size = str(file_size)
            response_code = str(200)
            content_type = 'application/octet-stream'
            conn.send_headers(
                stream_id=stream_id,
                headers=[
                    (':status', response_code),
                    ('server', 'basic-h2-server/1.0'),
                    ('content-length', response_size),
                    ('content-type', content_type),
                ],
            )

            num_chunks = math.ceil(file_size/chunk_size)
            #print('num_chunks', num_chunks)
            with open(my_path, 'rb') as file:
                for i in range(num_chunks):
                    response_data = file.read(chunk_size)
                    conn.send_data(
                        stream_id=stream_id,
                        data=response_data,
                        end_stream=i == num_chunks-1
                    )

        else:
            print('no file')
            response_data = b'file not found'
            response_code = str(200)
            content_type = 'text/plain'
            response_size = str(len(response_data))
            conn.send_headers(
                stream_id=stream_id,
                headers=[
                    (':status', response_code),
                    ('server', 'basic-h2-server/1.0'),
                    ('content-length', response_size),
                    ('content-type', content_type),
                ],
            )
            conn.send_data(
                stream_id=stream_id,
                data=response_data,
                end_stream=False
            )
def send_response(conn, event):
    stream_id = event.stream_id
    #print(dict(event.headers).keys())
    #print(dict(event.headers).values())

    my_path = './' + dict(event.headers)[':path']

    if my_path == './':
        response_data = b'Welcome to our server'
        response_code = str(200)
        content_type = 'text/plain'
    else:
        if os.path.isfile(my_path):
            with open(my_path, 'rb') as file:
                response_data = file.read()
            response_code = str(200)
            content_type = 'application/octet-stream'
        else:
            print('file not found')
            response_data = b'file not found'
            response_code = str(200)
            content_type = 'text/plain'
    conn.send_headers(
        stream_id=stream_id,
        headers=[
            (':status', response_code),
            ('server', 'basic-h2-server/1.0'),
            ('content-length', str(len(response_data))),
            ('content-type', content_type),
        ],
    )
    conn.send_data(
        stream_id=stream_id,
        data=response_data,
        end_stream=True
    )

def handle(sock):
    config = h2.config.H2Configuration(client_side=False)

    conn = h2.connection.H2Connection(config=config)
    conn.initiate_connection()
    sock.sendall(conn.data_to_send())

    while True:
        data = sock.recv(65535)
        if not data:
            break

        events = conn.receive_data(data)
        for event in events:
            if isinstance(event, h2.events.RequestReceived):
                send_response(conn, event)

        data_to_send = conn.data_to_send()
        if data_to_send:
            sock.sendall(data_to_send)


sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('0.0.0.0', 8080))
sock.listen(5)

while True:
    handle(sock.accept()[0])