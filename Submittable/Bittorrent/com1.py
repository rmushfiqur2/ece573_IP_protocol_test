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

while True:
   time.sleep(1)