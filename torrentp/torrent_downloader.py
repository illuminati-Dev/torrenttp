from .session import Session
from .torrent_info import TorrentInfo
from .downloader import Downloader
import libtorrent as lt

class TorrentDownloader:
    def __init__(self, file_path, save_path):
        self._file_path = file_path
        self._save_path = save_path
        self._downloader = None
        self._torrent_info = None
        self._lt = lt
        self._file = None
        self._add_torrent_params = None
        self._session = Session(self._lt)

    def start_download(self):
        if self._file_path.startswith('magnet:'):
            self._add_torrent_params = self._lt.parse_magnet_uri(self._file_path)
            self._add_torrent_params.save_path = self._save_path

            # Check if the attribute exists before using it
            if hasattr(lt.torrent_flags, 'enable_undecoded_pieces'):
                self._add_torrent_params.flags |= lt.torrent_flags.enable_undecoded_pieces

            # Enable DHT and PEX for magnet links
            self._add_torrent_params.flags |= lt.torrent_flags.enable_dht
            self._add_torrent_params.flags |= lt.torrent_flags.enable_peer_exchange

            self._downloader = Downloader(session=self._session, torrent_info=self._add_torrent_params,
                                          save_path=self._save_path, libtorrent=lt, is_magnet=True)
        else:
            self._torrent_info = TorrentInfo(self._file_path, self._lt)
            self._downloader = Downloader(session=self._session, torrent_info=self._torrent_info,
                                          save_path=self._save_path, libtorrent=None, is_magnet=False)

        self._file = self._downloader
        return self._file.download()

    def __str__(self):
        return f"TorrentDownloader(file_path={self._file_path}, save_path={self._save_path})"

    def __repr__(self):
        return self.__str__()

    def __call__(self, *args, **kwargs):
        # Add your custom logic here
        print("TorrentDownloader instance called!")
        # You can perform any custom actions or return a specific value
