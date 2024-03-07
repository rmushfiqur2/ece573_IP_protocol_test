import grpc

import chunk_pb2, chunk_pb2_grpc

CHUNK_SIZE = 1024 * 1024  # 1MB


def save_chunks_to_file(chunks, filename):
    metadata = chunks.initial_metadata()  # Get initial metadata associated with the RPC call
    header_bytes = sum(len(key) + len(value) for key, value in metadata)  # Calculate total length of metadata
    content_length = 0
    with open(filename, 'wb') as f:
        for chunk in chunks:
            f.write(chunk.buffer)
            content_length += len(chunk.buffer)

    return header_bytes, content_length

class FileClient:
    def __init__(self, address):
        channel = grpc.insecure_channel(address)
        self.stub = chunk_pb2_grpc.FileServerStub(channel)

    def download(self, target_name, out_file_name):
        response = self.stub.download(chunk_pb2.Request(name=target_name))
        header_bytes, content_bytes = save_chunks_to_file(response, out_file_name)
        return header_bytes, content_bytes  # implemented code