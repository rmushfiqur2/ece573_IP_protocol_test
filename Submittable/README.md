## HTTP1.1 and HTTP2
### Environment
```
conda create --name http_env python=3.8
conda activate http_env
pip install requests==2.31.0
```
Although HTTP2 requires h2=2.6.0 and hyper=0.7.0 we modified the library file to change the maximum frame size of a request to 10 MB. We have provided the library files within the codes, so you do not need to change/download anything.

### Transfer files HTTP 1.1

To transfer files using HTTP1.1 protocol, run server execution file in one computer and client execution file in another computer. Change the IP address of the server in the client file.

```
# server (either computer A or B)
python server_http1.1.py
# client (change to clientB when needed)
python clientA-http1.1.py
```

### Transfer files HTTP 2.0

To transfer files using HTTP2.0 protocol, run server execution file in one computer and client execution file in another computer. Change the IP address of the server in the client file.

```
cd HTTP1.1and2
# server (either computer A or B)
python server_http2.py
# client (change to clientB when needed)
python clientA-http2.py
```

## GPRC

### Environment
````
pip install grpcio
pip install google-api-python-client
pip install unary-coding
pip install protobuf==3  [We use proto3 as protocol buffer version in chunk.proto file]
````

### Transfer files using GRPC
```
cd GRPC
# server side
python demo_server.py
# client side
python demo_client.py
```

Please address the ip address of the server in `demo_client.py`.


## BitTorrent

### Environment of Computer 1 (that we will use for seeding)
We have tested with a Ubuntu system, with necessary building commands from <a href="https://www.libtorrent.org/building.html">libtorrent.org</a>:
```angular2html
sudo apt install libboost-tools-dev libboost-dev libboost-system-dev
echo "using gcc ;" >>~/user-config.jam
b2 crypto=openssl cxxstd=14 release
```
Then we can use libtorrent using pip:
```angular2html
pip install libtorrent
```
### Environment of Computer 2,3, or 4 (that we will use for receiving file)

```
pip install requests==2.10.0
pip install bcoding=1.5.0
pip install bitstring
```

### File transfer using bittorrent protocol

```angular2html
cd Bittorrent
# computer 1 (have the files)
python com1.py
# computer 2, 3 and 4 (please run simultaneously on three computers)
python com234.py
```

Please ensure that the IP address of computer 1 is updated in `com234.py`. Also, for downloading each of the files (10kB, 100kB, 1MB and 10MB) uncomment the respective line. We have tested simultaneously downloading each of the file from three computers.


## Detail Information on GRPC

### Generation of protocol buffer messages and gRPC service stubs

- [x] At first, we define the structure of the data to serialize in a proto file (we named this file as `chunk.proto`) . Then we use protocol buffer compiler protoc to generate data access classes using by the following python command. This command will automatically generate two files named `chunk_pb2.py` and `chunk_pb2_grpc.py`:

- ``python -m grpc_tools.protoc --proto_path=. ./chunk.proto --python_out=. --grpc_python_out=.``
