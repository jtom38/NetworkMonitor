
import requests
import typing

from networkmonitor.src.protocols import IProtocols

class Http:
    def __init__(self, protocol:IProtocols):
        self.protocol   = protocol
        self.URI:str    = ''
        self.status:str = ''
        self.ms:int     = -1
        pass

    def Get(self):

        try:
            r = requests.get(self.protocol.URI)

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
            self.URI = URI
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