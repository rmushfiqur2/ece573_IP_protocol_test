import csv
import lib2
import time

def transfer(num_runs, source_url, destination_url):
    transfer_times = []
    content_bytes = []
    header_bytes = []

    url_parts = source_url.split('/')
    hostname_port = url_parts[0]  # 'localhost:12888'
    in_file_name = url_parts[1]  # 'A_20'
    client = lib2.FileClient(hostname_port)

    for _ in range(num_runs):
        start_time = time.time()
        header_bytes_individual, content_bytes_individual = client.download(in_file_name, destination_url)
        end_time = time.time()
        transfer_time = end_time - start_time
        transfer_times.append(transfer_time)
        header_bytes.append(header_bytes_individual)
        content_bytes.append(content_bytes_individual)
    return transfer_times, content_bytes, header_bytes

def file_write(transfer_times, content_bytes, header_bytes, filename):
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
        #print(((sum(header_bytes)+sum(content_bytes))/sum(transfer_times))/1024, ' kBPS')

server_ip_addr = '10.153.43.198'
server_port = '8898'


filename = 'B_10kB'
source_url = server_ip_addr + ':' + server_port + '/' + filename
transfer_times, content_bytes, header_bytes = transfer(10000, source_url, filename)
file_write(transfer_times, content_bytes, header_bytes,filename)

filename = 'B_100kB'
source_url = server_ip_addr + ':' + server_port + '/' + filename
transfer_times, content_bytes, header_bytes = transfer(1000, source_url, filename)
file_write(transfer_times, content_bytes, header_bytes,filename)

filename = 'B_1MB'
source_url = server_ip_addr + ':' + server_port + '/' + filename
transfer_times, content_bytes, header_bytes = transfer(10, source_url, filename)
file_write(transfer_times, content_bytes, header_bytes,filename)

filename = 'B_10MB'
source_url = server_ip_addr + ':' + server_port + '/' + filename
transfer_times, content_bytes, header_bytes = transfer(1, source_url, filename)
file_write(transfer_times, content_bytes, header_bytes,filename)