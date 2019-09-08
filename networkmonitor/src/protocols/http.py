
import requests
import typing

from networkmonitor.src.protocols import IProtocols

class Http:
    def __init__(self, protocol:IProtocols):
        self.protocol   = protocol
        self.URI:str    = ''
        self.Status:str = ''
        self.MS:int     = -1
        pass

    def Start(self):
        self.__CleanAddress__()

        if self.protocol.Type.lower() == "http:get":
            return self.__Get()
        elif self.protocol.Type.lower() == "http:post":
            return self.__Post()
        
        pass

    def __Get(self):
        try:
            r = requests.get(self.protocol.URI)

            self.MS = int(r.elapsed.microseconds)
            if r.status_code == 200:
                self.Status = "Online"
                r.close()
                return True
            else: 
                self.Status = "Offline"
                r.close()
                return False
        except Exception:
            raise "Make sure the url has 'http://' for basic requests."

    def __Post(self):
        try:
            r = requests.post(self.protocol.URI)
            self.ms = r.elapsed.microseconds
            if r.status_code == 200:
                self.status = "Online"
                r.close()
                return True
            else:
                self.status = "Offline"
                r.close()
                return False
        except:
            pass

    def __CleanAddress__(self):
        """
        This will clean up the address that is given.
        If the address does not start with "http://", we will add it!
        """
        adjustUri: bool = False
        uri:str = self.protocol.URI

        if uri.startswith("http://") or uri.startswith('https://')== False:
            adjustUri = True
                        
        if adjustUri == True:
            self.protocol.URI = f"http://{uri}"