
import requests

from .terminal import TerminalOutput

class Http:
    def __init__(self):
        pass

    def TestHttpGet(self, URI ):
        try:
            r = requests.get(URI)
            if r.status_code == 200:
                return "Online"
            else: 
                return "Offline"
        except Exception:
            raise "Make sure the url has 'http://' for basic requests."
