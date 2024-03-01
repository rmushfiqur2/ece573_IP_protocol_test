import time
import requests
import numpy as np
import csv

def receive_http1_1(num_runs, source_url, destination_url):
    transfer_times = []
    content_bytes = []
    header_bytes = []
    #s = requests.Session()
    for _ in range(num_runs):
        start_time = time.time()
        #with s.get(source_url) as response:
        response = requests.get(source_url)
        end_time = time.time()
        #with open(destination_url, 'wb') as f:
            #f.write(response.content)
        transfer_time = end_time - start_time
        transfer_times.append(transfer_time)
        #content_bytes.append(len(str(response.content)))
        header_bytes.append(len(str(response.headers)))
        #print(str(response.content)[0:40])
        #print(len(str(response.content)))
        #print(str(response.headers))
        #print(str(response.text)[0:40])
        #print(len(str(response.text)))
        content_bytes.append(int(response.headers['Content-length']))
    return transfer_times, content_bytes, header_bytes

server_ip_addr = 'http://10.153.61.9' # internal ip addr (on same AP/ public ip address)
server_port = '8890'

# test.txt
"""filename = 'test.txt'
source_url = server_ip_addr + ':' + server_port + '/' + filename
destination_url = filename  # Save in local directory

transfer_times, content_bytes, header_bytes = receive_http1_1(10, source_url, destination_url)

# Transpose arrays into rows
data = zip(transfer_times, content_bytes, header_bytes)
# Define the file name
file_name = filename + '.csv'
# Write data to CSV file
with open(file_name, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write header if needed
    writer.writerow(['Time(s)', 'Content(bytes)', 'Header(bytes)'])  # Example header
    # Write data rows
    for row in data:
        writer.writerow(row)"""


# 10 kB
filename = 'A_10kB'
source_url = server_ip_addr + ':' + server_port + '/Data_files/' + filename
destination_url = 'Data_files/' + filename  # Save in local directory

transfer_times, content_bytes, header_bytes = receive_http1_1(1000, source_url, destination_url)

# Transpose arrays into rows
data = zip(transfer_times, content_bytes, header_bytes)
# Define the file name
file_name = filename + '.csv'
# Write data to CSV file
with open(file_name, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write header if needed
    writer.writerow(['Time(s)', 'Content(bytes)', 'Header(bytes)'])  # Example header
    # Write data rows
    for row in data:
        writer.writerow(row)

# 100 kB

filename = 'A_100kB'
source_url = server_ip_addr + ':' + server_port + '/Data_files/' + filename
destination_url = 'Data_files/' + filename  # Save in local directory

transfer_times, content_bytes, header_bytes = receive_http1_1(100, source_url, destination_url)

# Transpose arrays into rows
data = zip(transfer_times, content_bytes, header_bytes)
# Define the file name
file_name = filename + '.csv'
# Write data to CSV file
with open(file_name, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write header if needed
    writer.writerow(['Time(s)', 'Content(bytes)', 'Header(bytes)'])  # Example header
    # Write data rows
    for row in data:
        writer.writerow(row)

# 1 MB

filename = 'A_1MB'
source_url = server_ip_addr + ':' + server_port + '/Data_files/' + filename
destination_url = 'Data_files/' + filename  # Save in local directory

transfer_times, content_bytes, header_bytes = receive_http1_1(10, source_url, destination_url)

# Transpose arrays into rows
data = zip(transfer_times, content_bytes, header_bytes)
# Define the file name
file_name = filename + '.csv'
# Write data to CSV file
with open(file_name, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write header if needed
    writer.writerow(['Time(s)', 'Content(bytes)', 'Header(bytes)'])  # Example header
    # Write data rows
    for row in data:
        writer.writerow(row)

# 10 MB

filename = 'A_10MB'
source_url = server_ip_addr + ':' + server_port + '/Data_files/' + filename
destination_url = 'Data_files/' + filename  # Save in local directory

transfer_times, content_bytes, header_bytes = receive_http1_1(1, source_url, destination_url)

# Transpose arrays into rows
data = zip(transfer_times, content_bytes, header_bytes)
# Define the file name
file_name = filename + '.csv'
# Write data to CSV file
with open(file_name, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write header if needed
    writer.writerow(['Time(s)', 'Content(bytes)', 'Header(bytes)'])  # Example header
    # Write data rows
    for row in data:
        writer.writerow(row)
