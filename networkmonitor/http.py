
import requests

from .terminal import TerminalOutput


class Http:
    def __init__(self):
        pass

    def TestHttpGet(self, URI: str, Port:int ):
        try:
            r = requests.get(URI)
            if r.status_code == 200:
                return "Online"
            else: 
                return "Offline"
        except Exception:
            raise "Make sure the url has 'http://' for basic requests."

    def Post(self, URI:str, Port:int=-1):
        if Port != -1:
            sPort = str(Port)
            URI = f"{URI}:{Port}"
        try:
            r = requests.post(url=URI)
            if r.status_code == 200:
                return "Online"
            else:
                return "Offline"
    
