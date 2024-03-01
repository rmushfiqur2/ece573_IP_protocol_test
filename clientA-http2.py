import time
import requests
import numpy as np
import csv
import httpx
import asyncio
import pickle

# result:
# without multiplexing
# HTTP 1.1 without async 14012 kBPS
# HTTP 2 without async 13909 kBPS
# HTTP 2 with async 12519 kBPS
# HTTP 1.1 with async 13000 kBPS

async def receive_http2(num_runs, source_url, destination_url):
    transfer_times = []
    content_bytes = []
    header_bytes = []

    async with httpx.AsyncClient(http2=True) as client:
        for _ in range(num_runs):
            start_time = time.time()
            response = await client.get(source_url) # client.get is a async function
            end_time = time.time()
            #with open(destination_url, 'wb') as f:
                #f.write(response.content)
            transfer_time = end_time - start_time
            transfer_times.append(transfer_time)
            header_bytes.append(len(str(response.headers)) - 9)
            content_bytes.append(int(response.headers['content-length']))
            # content_bytes.append(len(int(response.headers))
            print(response.http_version)
            print(response.status_code)
    return transfer_times, content_bytes, header_bytes

async def receive_http2_multiplexing(num_runs, source_url, destination_url):

    async with httpx.AsyncClient(http2=True) as client:
        urls = [source_url] * num_runs

        # Send requests asynchronously
        tasks = [client.get(url) for url in urls]
        start_time = time.time()
        responses = await asyncio.gather(*tasks)
        end_time = time.time()

        # Process responses
        for response in responses:
            with open(destination_url, 'wb') as f:
                f.write(response.content)
        print(response.status_code)
        #print(response.headers)
        print(response.http_version)

        content_bytes = int(dict(response.headers)['content-length'])
        header_bytes = len(str(response.headers)) - 9
        print('content bytes', content_bytes)
        print(header_bytes)
        print('header bytes', header_bytes)


    return [end_time - start_time], [content_bytes * num_runs], [header_bytes*num_runs]

server_ip_addr = 'http://192.168.1.77' # internal ip addr (on same AP/ public ip address)
server_port = '8000'
server_ip_addr = 'https://www.example.com'
server_port = '443' #https

server_ip_addr = 'http://localhost'
server_port = '8895' #https

# test.txt
filename = 'index.html'
source_url = server_ip_addr + ':' + server_port + '/' + filename
destination_url = filename  # Save in local directory

loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(receive_http2_multiplexing(10, source_url, destination_url)), # sum is an async function and contains a task/ portion starting with async
]
done, pending = loop.run_until_complete(asyncio.wait(tasks))
loop.close()

for future in done:
    value = future.result() #may raise an exception if coroutine failed
    transfer_times, content_bytes, header_bytes = value

# Transpose arrays into rows
data = zip(transfer_times, content_bytes, header_bytes)
# Define the file name
file_name = filename + '-http2.csv'
# Write data to CSV file
with open(file_name, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write header if needed
    writer.writerow(['Time(s)', 'Content(bytes)', 'Header(bytes)'])  # Example header
    # Write data rows
    for row in data:
        writer.writerow(row)
print((sum(header_bytes)+sum(content_bytes))/sum(transfer_times), ' kBPS')

fhsdjhf = kfhokdf + 1
# 10 kB
filename = 'B_10kB'
source_url = server_ip_addr + ':' + server_port + '/Data_files/' + filename
destination_url = 'Data_files/' + filename  # Save in local directory

loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(receive_http2(10, source_url, destination_url)), # sum is an async function and contains a task/ portion starting with async
]
done, pending = loop.run_until_complete(asyncio.wait(tasks))
loop.close()

for future in done:
    value = future.result() #may raise an exception if coroutine failed
    transfer_times, content_bytes, header_bytes = value

# Transpose arrays into rows
data = zip(transfer_times, content_bytes, header_bytes)
# Define the file name
file_name = filename + '-http2.csv'
# Write data to CSV file
with open(file_name, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write header if needed
    writer.writerow(['Time(s)', 'Content(bytes)', 'Header(bytes)'])  # Example header
    # Write data rows
    for row in data:
        writer.writerow(row)
gfsdjhks = fjsdhf + 1
# 100 kB

filename = 'B_100kB'
source_url = server_ip_addr + ':' + server_port + '/Data_files/' + filename
destination_url = 'Data_files/' + filename  # Save in local directory

transfer_times, content_bytes, header_bytes = receive_http2(10, source_url, destination_url)

# Transpose arrays into rows
data = zip(transfer_times, content_bytes, header_bytes)
# Define the file name
file_name = filename + '-http2.csv'
# Write data to CSV file
with open(file_name, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write header if needed
    writer.writerow(['Time(s)', 'Content(bytes)', 'Header(bytes)'])  # Example header
    # Write data rows
    for row in data:
        writer.writerow(row)

# 1 MB

filename = 'B_1MB'
source_url = server_ip_addr + ':' + server_port + '/Data_files/' + filename
destination_url = 'Data_files/' + filename  # Save in local directory

transfer_times, content_bytes, header_bytes = receive_http2(10, source_url, destination_url)

# Transpose arrays into rows
data = zip(transfer_times, content_bytes, header_bytes)
# Define the file name
file_name = filename + '-http2.csv'
# Write data to CSV file
with open(file_name, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write header if needed
    writer.writerow(['Time(s)', 'Content(bytes)', 'Header(bytes)'])  # Example header
    # Write data rows
    for row in data:
        writer.writerow(row)

# 10 MB

filename = 'B_10MB'
source_url = server_ip_addr + ':' + server_port + '/Data_files/' + filename
destination_url = 'Data_files/' + filename  # Save in local directory

transfer_times, content_bytes, header_bytes = receive_http2(1, source_url, destination_url)

# Transpose arrays into rows
data = zip(transfer_times, content_bytes, header_bytes)
# Define the file name
file_name = filename + '-http2.csv'
# Write data to CSV file
with open(file_name, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write header if needed
    writer.writerow(['Time(s)', 'Content(bytes)', 'Header(bytes)'])  # Example header
    # Write data rows
    for row in data:
        writer.writerow(row)
