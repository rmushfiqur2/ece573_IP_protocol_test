import argparse
import logging
import asyncio
import time
import csv

from bittorrent.client import TorrentClient

logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)

# create console handler with a higher log level
fh = logging.FileHandler('bittorrent.log')
ch = logging.StreamHandler()
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

async def main(torrent_file, destination, ip, port, download_times=1):
    # file download multiple times unnecessarily (to measure speed)

    transfer_times = []
    content_bytes = []
    header_bytes = []
    
    for _ in range(download_times):
        print('download started/ restarted')
        client = TorrentClient(torrent_file, destination, loop, ip, port)

        start_time = time.time()

        task1 = asyncio.create_task(client.connect_to_peers()) # task started
        task2 = asyncio.create_task(client.keep_alive()) # task started

        result = await task1
        task1.cancel()
        task2.cancel()
        #result2 = await task2 # loop sleeps for 90 s, so better not wait for it

        end_time = time.time()
        transfer_times.append(end_time - start_time)
        content_bytes.append(client.content_bytes)
        header_bytes.append(client.total_app_layer_bytes - client.content_bytes)
        #print('time: ', end_time - start_time)
        #loop.close()
        #time.sleep(0.1)

    # Transpose arrays into rows
    data = zip(transfer_times, content_bytes, header_bytes)
    # Define the file name
    file_name = torrent_file + '.csv'
    # Write data to CSV file
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write header if needed
        writer.writerow(['Time(s)', 'Content(bytes)', 'Header(bytes)'])  # Example header
        # Write data rows
        for row in data:
            writer.writerow(row)
    print((sum(header_bytes) + sum(content_bytes)) / sum(transfer_times) / 1000, ' kBPS')



if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    asyncio.run(main('A_10MB.torrent', './', '10.153.50.73', '6881', 1))
    #asyncio.run(main('A_1MB.torrent', './', '10.153.50.73', '6881', 3))
    #asyncio.run(main('A_100kB.torrent', './', '10.153.50.73', '6881', 33))
    #asyncio.run(main('A_10kB.torrent', './', '10.153.50.73', '6881', 333))

    loop.close() # without closing loop the A_10MB is locked by the process and it is 0  kB