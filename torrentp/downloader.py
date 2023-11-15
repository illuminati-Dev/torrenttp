import sys
import time
import logging

class Downloader:
    def __init__(self, session, torrent_info, save_path, libtorrent, is_magnet):
        self._session = session
        self._torrent_info = torrent_info
        self._save_path = save_path
        self._file = None
        self._lt = libtorrent
        self._add_torrent_params = None
        self._is_magnet = is_magnet

    def status(self):
        if not self._is_magnet:
            self._file = self._session.add_torrent({'ti': self._torrent_info, 'save_path': self._save_path})
        else:
            self._add_torrent_params = self._torrent_info
            self._add_torrent_params.save_path = self._save_path
            self._file = self._session.add_torrent(self._add_torrent_params)
        return self._file.status()

    def download(self):
        try:
            print(f'Start downloading {self.name}')
            while not self._file.status().is_seeding:
                s = self.status()

                print('\r%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' % (
                    s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000,
                    s.num_peers, s.state), end=' ')

                sys.stdout.flush()
                time.sleep(1)
                
            print(f'Successfully Downloaded {self.name}')
            return self.name
        except Exception as e:
            logging.error(f"Error downloading {self.name}: {e}")
            raise

    @property
    def name(self):
        return self._file.status().name

    def __str__(self):
        return f"Downloader(session={self._session}, save_path='{self._save_path}')"

    def __repr__(self):
        return self.__str__()

    def __call__(self):
        pass  
