
import requests

from .terminal import TerminalOutput

class Http:
    def __init__(self):
        pass

    def ProcessHTTP(self, URL:str):
        
        res = self.TestHTTP(URL)
        if res == True:
            status:str = "Online"
        else:
            status:str = "Offline"
        return status

    def TestHTTP(self, URI ):
        r = requests.get(URI)
        if r.status_code == 200:
            return True
        else: 
            return False
        

#if __name__ == "__main__":
    #Http
    #pass