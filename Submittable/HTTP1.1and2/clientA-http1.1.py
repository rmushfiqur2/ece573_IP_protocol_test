import time
import requests
import csv

def receive_http1_1(num_runs, source_url, destination_url):
    transfer_times = []
    content_bytes = []
    header_bytes = []
    s = requests.Session() # Session keeps the connection alive
    for _ in range(num_runs):
        start_time = time.time()
        with s.get(source_url) as response: # with so that response is closed after this block
            with open(destination_url, 'wb') as f:
                f.write(response.content)
            end_time = time.time()
            transfer_time = end_time - start_time
            transfer_times.append(transfer_time)
            header_bytes.append(len(str(response.headers)))
            content_bytes.append(int(response.headers['Content-length']))
    return transfer_times, content_bytes, header_bytes

server_ip_addr = 'http://10.153.50.73' # internal ip addr (on same AP/ public ip address)
server_port = '8000'

# 10 kB
filename = 'B_10kB'
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
print((sum(header_bytes)+sum(content_bytes))/sum(transfer_times)/1000, ' kBPS')

# 100 kB

filename = 'B_100kB'
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
print((sum(header_bytes)+sum(content_bytes))/sum(transfer_times)/1000, ' kBPS')

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
print((sum(header_bytes)+sum(content_bytes))/sum(transfer_times)/1000, ' kBPS')

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
print((sum(header_bytes)+sum(content_bytes))/sum(transfer_times)/1000, ' kBPS')
