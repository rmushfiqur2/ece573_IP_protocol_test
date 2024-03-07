import argparse
import logging
import asyncio

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
    loop = asyncio.get_event_loop()
    client = TorrentClient(torrent_file, destination, loop, ip, port, download_times)

    future1 = asyncio.ensure_future(client.connect_to_peers())
    future2 = asyncio.ensure_future(client.keep_alive())

    # future1.done(), await future1
    await future1
    await
    loop.close()

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()


if __name__ == '__main__':
    #parser = argparse.ArgumentParser(description='CLI BitTorrent Client')
    #parser.add_argument('source', help='locaiton of the torrent file')
    #parser.add_argument('destination', help='specify location of downloaded files')
    #args = parser.parse_args()

    #main('2women.torrent', './', '10.153.21.85', '6881')
    main('A_10MB.torrent', './', '10.153.21.85', '6881', 2)
