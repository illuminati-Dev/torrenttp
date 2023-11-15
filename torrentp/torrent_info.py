import libtorrent as lt

class TorrentInfo:
    def __init__(self, path, libtorrent):
        self._path = path
        self._lt = libtorrent
        self._info = self.create_torrent_info()

    def show_info(self):
        # You can implement a method to display information about the torrent here.
        pass

    def create_torrent_info(self):
        return self._lt.torrent_info(self._path)

    def __str__(self):
        return f"TorrentInfo(path='{self._path}')"

    def __repr__(self):
        return self.__str__()

    def __call__(self):
        return self.create_torrent_info()
