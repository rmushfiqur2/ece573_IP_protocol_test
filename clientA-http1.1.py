import time
import requests
import numpy as np
import csv

def receive_http1_1(num_runs, source_url, destination_url):
    transfer_times = []
    content_bytes = []
    header_bytes = []
    for _ in range(num_runs):
        start_time = time.time()
        response = requests.get(source_url)
        with open(destination_url, 'wb') as f:
            f.write(response.content)
        end_time = time.time()
        transfer_time = end_time - start_time
        transfer_times.append(transfer_time)
        content_bytes.append(len(str(response.content)))
        header_bytes.append(len(str(response.headers)))
    return transfer_times

server_ip_addr = 'http://192.168.1.11' # internal ip addr (on same AP/ public ip address)
server_port = '8000'

# 10 kB
filename = 'B_10kB'
source_url = server_ip_addr + ':' + server_port + '/Data_files/' + filename
destination_url = 'Data_files/' + filename  # Save in local directory

transfer_times, content_bytes, header_bytes = receive_http1_1(10000, source_url, destination_url)

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

filename = 'B_100kB'
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

# 1 MB

filename = 'B_1MB'
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

filename = 'B_10MB'
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
