import os
from concurrent import futures

import grpc
import time

import chunk_pb2, chunk_pb2_grpc

CHUNK_SIZE = 1024 * 1024  # 1MB


def get_file_chunks(filename):
    with open(filename, 'rb') as f:
        while True:
            piece = f.read(CHUNK_SIZE);
            if len(piece) == 0:
                return
            yield chunk_pb2.Chunk(buffer=piece)

class FileServer(chunk_pb2_grpc.FileServerServicer):
    def __init__(self):

        class FileServer(chunk_pb2_grpc.FileServerServicer):

            def download(self, request, context):
                #print("Server downloading", request.name)

                file_names = ['A_10kB', 'A_100kB', 'A_1MB', 'A_10MB','B_10kB', 'B_100kB', 'B_1MB', 'B_10MB']
                for name in file_names:
                    if request.name==name:
                        #print(name)
                        return get_file_chunks(name)

        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
        chunk_pb2_grpc.add_FileServerServicer_to_server(FileServer(), self.server)

    def start(self, port):
        print("Server is running on the port: ", port)
        self.server.add_insecure_port(f'[::]:{port}')
        self.server.start()

        try:
            while True:
                time.sleep(60*60*24)
        except KeyboardInterrupt:
            self.server.stop(0)