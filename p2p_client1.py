'''
You should try libtorrent (rasterbar). http://libtorrent.org
If you want to write your client in python, on linux, install it with:
sudo apt-get install python-libtorrent
A very simple example of python code to use it to download a torrent:
'''

import libtorrent as lt
import time
import sys

ses = lt.session()
print(ses)
ses.listen_on(6881, 6891)


info = lt.torrent_info('A_10kB.torrent')
h = ses.add_torrent({'ti': info, 'save_path': './Data_files/'})
print('starting', h.name())
while (h.status().state != lt.torrent_status.seeding):
   time.sleep(1)
print('complete')

info = lt.torrent_info('A_100kB.torrent')
h = ses.add_torrent({'ti': info, 'save_path': './Data_files/'})
while (h.status().state != lt.torrent_status.seeding):
   time.sleep(1)
print('complete')

info = lt.torrent_info('A_1MB.torrent')
h = ses.add_torrent({'ti': info, 'save_path': './Data_files/'})
while (h.status().state != lt.torrent_status.seeding):
   time.sleep(1)
print('complete')

info = lt.torrent_info('A_10MB.torrent')
h = ses.add_torrent({'ti': info, 'save_path': './Data_files/'})
while (h.status().state != lt.torrent_status.seeding):
   time.sleep(1)
print('complete')

"""while (h.status().state != lt.torrent_status.seeding):
   s = h.status()

   state_str = ['queued', 'checking', 'downloading metadata',
      'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']
   print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
      (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000,
      s.num_peers, state_str[s.state]))
   sys.stdout.flush()

   time.sleep(1)

print(h.name(), 'complete')"""

while True:
   time.sleep(1)