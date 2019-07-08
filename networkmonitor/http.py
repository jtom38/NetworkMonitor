
import requests

from .terminal import TerminalOutput

class Http:
    def __init__(self):
        pass

    def TestHttpGet(self, URI ):
        r = requests.get(URI)

        if r.status_code == 200:
            return "Online"
        else: 
            return "Offline"
        

#if __name__ == "__main__":
    #Http
    #pass