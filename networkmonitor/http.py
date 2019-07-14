
import requests

#from .terminal import TerminalOutput


class Http:
    def __init__(self):
        pass

    def Get(self, URI: str):

        try:
            r = requests.get(URI)
            if r.status_code == 200:
                return True
            else: 
                return False
        except Exception:
            raise "Make sure the url has 'http://' for basic requests."

    def Post(self, URI:str):
        
        try:
            r = requests.post(url=URI)
            if r.status_code == 200:
                return True
            else:
                return False
        except:
            pass
    
