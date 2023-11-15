import libtorrent as lt

class Session:
    def __init__(self, libtorrent):
        self._user_agent = 'python client v0.1'
        self._listen_interfaces = '0.0.0.0'
        self._port = 6881  # Port should be an integer, not a string
        self._download_rate_limit = 0
        self._upload_rate_limit = 0  # Fixed variable name
        self._lt = libtorrent

        # Call create_session in the constructor to create the session when an object is instantiated
        self._session = self.create_session()

    def create_session(self):
        settings = {
            'listen_interfaces': f'{self._listen_interfaces}:{self._port}',
            'user_agent': self._user_agent,
            'download_rate_limit': self._download_rate_limit,
            'upload_rate_limit': self._upload_rate_limit
        }
        return self._lt.session(settings)

    def __str__(self):
        return f"Session(user_agent='{self._user_agent}', listen_interfaces='{self._listen_interfaces}:{self._port}')"

    def __repr__(self):
        return self.__str__()

    def __call__(self):
        return self._session
