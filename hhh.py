import time
import httpx
import numpy as np
import asyncio

async def transfer_http2(file_size, num_runs, source_url, destination_url):
    transfer_times = []
    total_bytes_transferred = 0
    # client = httpx.AsyncClient(http2=True)
    async with httpx.AsyncClient(http2=True) as client:
        for _ in range(num_runs):
            start_time = time.time()
            response = await client.get(source_url)
            print(response.http_version)
            with open(destination_url, 'wb') as f:
                f.write(response.content)
            end_time = time.time()
            transfer_time = end_time - start_time
            transfer_times.append(transfer_time)
            total_bytes_transferred += file_size
    return transfer_times, total_bytes_transferred

source_url_http2 = 'http://192.168.1.77:8000/A_10kB'  # Adjust server IP and port if needed
destination_url_http2 = 'A_10kB'  # Save in local directory

num_runs = 10

async def main_async():
    task = asyncio.create_task(transfer_http2(10 * 1024, num_runs, source_url_http2, destination_url_http2))
    await task
    return task.result()

task = asyncio.create_task(transfer_http2(10 * 1024, num_runs, source_url_http2, destination_url_http2))


average_transfer_time = np.mean(transfer_times_http2)
std_dev_transfer_time = np.std(transfer_times_http2)

# Calculate throughput statistics in kilobits per second
total_transfer_time = sum(transfer_times_http2)
#average_throughput_kbps = (total_bytes_transferred * 8 / 1000) / total_transfer_time  # Convert bytes to kilobits and seconds to kiloseconds
average_throughput_kbps = (total_bytes_transferred * 8 / 1000) / num_runs  # Convert bytes to kilobits and seconds to kiloseconds
std_dev_throughput_kbps = np.std(transfer_times_http2)

print("Average Transfer Time:", average_transfer_time)
print("Standard Deviation of Transfer Time:", std_dev_transfer_time)
print("Average Throughput:", average_throughput_kbps, "kilobits per second")
print("Standard Deviation of Throughput:", std_dev_throughput_kbps, "kilobits per second")