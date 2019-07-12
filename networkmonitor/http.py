
import requests

from .terminal import TerminalOutput


class Http:
    def __init__(self):
        pass

    def Get(self, URI: str):

        try:
            r = requests.get(URI)
            if r.status_code == 200:
                return "Online"
            else: 
                return "Offline"
        except Exception:
            raise "Make sure the url has 'http://' for basic requests."

    def Post(self, URI:str):
        
        try:
            r = requests.post(url=URI)
            if r.status_code == 200:
                return "Online"
            else:
                return "Offline"
        except:
            pass
    
