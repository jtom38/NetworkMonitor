
import requests

#from .terminal import TerminalOutput


class Http:
    def __init__(self):
        self.URI:str    = ''
        self.status:str = ''
        self.ms:int     = -1
        
        pass

    def Get(self, URI: str):

        try:
            r = requests.get(URI)

            self.ms = r.elapsed.microseconds
            if r.status_code == 200:
                self.status = "Online"
                return True
            else: 
                self.status = "Offline"
                return False
        except Exception:
            raise "Make sure the url has 'http://' for basic requests."

    def Post(self, URI:str):
        
        try:
            r = requests.post(url=URI)
            self.ms = r.elapsed.microseconds
            if r.status_code == 200:
                self.status = "Online"
                return True
            else:
                self.status = "Offline"
                return False
        except:
            pass