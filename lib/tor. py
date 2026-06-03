import requests

class Tor:
    def __init__(self):
        self.session = requests.Session()

    def tor_installed(self):
        # Cek apakah Tor terinstal
        try:
            self.session.get('http://check.torproject.org')
            return True
        except Exception:
            return False

    def new_session(self, proxies):
        try:
            self.session.proxies = proxies
            return self.session
        except Exception:
            return None

    def stop_tor(self):
        # Stop Tor
        pass
