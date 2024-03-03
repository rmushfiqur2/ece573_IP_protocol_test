import time
import csv
from hyper import HTTP20Connection
import time

def receive_http2(num_runs, host, source_url, destination_url, n_outstanding_req=1):
    conn = HTTP20Connection(host, network_buffer=10885760)
    transfer_times = []
    content_bytes = []
    header_bytes = []

    for j in range(num_runs // n_outstanding_req):
        n_requests = []
        n_times = []
        for i in range(n_outstanding_req):
            r = conn.request('GET', source_url)
            n_requests.append(r)
            start_time = time.time()
            n_times.append(start_time)
        for i in range(n_outstanding_req):
            resp = conn.get_response(n_requests[i])
            with open(destination_url, 'wb') as f:
                f.write(resp.read())
            end_time = time.time()
            transfer_times.append(end_time - n_times[i])
            header_bytes.append(len(str(resp.headers)))
            content_bytes.append(int(str(dict(resp.headers)[b'content-length'][0])[2:-1]))
    conn.close()

    return transfer_times, content_bytes, header_bytes

server_ip_addr = 'http://10.153.50.73' # internal ip addr (on same AP/ public ip address)
server_port = '8000'
host = server_ip_addr + ':' + server_port

# 10 kB
filename = 'B_10kB'
source_url = 'Data_files/' + filename
destination_url = 'Data_files/' + filename  # Save in local directory

transfer_times, content_bytes, header_bytes = receive_http2(10000, host, source_url, destination_url, n_outstanding_req=10)

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
print((sum(header_bytes)+sum(content_bytes))/sum(transfer_times)/8, ' kBPS')

# 100 kB

filename = 'B_100kB'
source_url = '/Data_files/' + filename
destination_url = 'Data_files/' + filename  # Save in local directory

transfer_times, content_bytes, header_bytes = receive_http2(1000, host, source_url, destination_url, n_outstanding_req=10)

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
print((sum(header_bytes)+sum(content_bytes))/sum(transfer_times)/8, ' kBPS')

# 1 MB

filename = 'B_1MB'
source_url = '/Data_files/' + filename
destination_url = 'Data_files/' + filename  # Save in local directory

transfer_times, content_bytes, header_bytes = receive_http2(10, host, source_url, destination_url, n_outstanding_req=10)

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
print((sum(header_bytes)+sum(content_bytes))/sum(transfer_times)/8, ' kBPS')

# 10 MB

filename = 'B_10MB'
source_url = '/Data_files/' + filename
destination_url = 'Data_files/' + filename  # Save in local directory

transfer_times, content_bytes, header_bytes = receive_http2(1, host, source_url, destination_url, n_outstanding_req=1)

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
print((sum(header_bytes)+sum(content_bytes))/sum(transfer_times)/8, ' kBPS')
