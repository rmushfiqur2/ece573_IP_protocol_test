import time
import requests
import numpy as np
from urllib.request import urlopen


def transfer_http1_1(file_size, num_runs, source_url, destination_url):
    transfer_times = []
    for _ in range(num_runs):
        start_time = time.time()
        response = requests.get(source_url)
        #response = urlopen(source_url)
        #with open(destination_url, 'wb') as f:
            #f.write(response.content)
        end_time = time.time()
        transfer_time = end_time - start_time
        transfer_times.append(transfer_time)
    return transfer_times, response

source_url_http1_1 = 'http://10.153.27.251:8001/B_10kB'  # Adjust server IP and port if needed
#source_url_http1_1 = 'http://localhost:50009/B_10kB'  # Adjust server IP and port if needed
source_url_http1_1 = 'http://172.217.168.228/index.html'  # Adjust server IP and port if needed
destination_url_http1_1 = 'B_10kB'  # Save in local directory

num_runs = 1

transfer_times_http1_1, response = transfer_http1_1(10 * 1024, num_runs, source_url_http1_1, destination_url_http1_1)

#print(response.read().decode('utf-8')) valid for urlopen
#print(len(response.read().decode('utf-8')))

average_transfer_time = np.mean(transfer_times_http1_1)
std_dev_transfer_time = np.std(transfer_times_http1_1)

print("Average Transfer Time:", average_transfer_time)
print("Standard Deviation of Transfer Time:", std_dev_transfer_time)