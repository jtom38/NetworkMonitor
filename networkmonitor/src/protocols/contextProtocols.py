
from networkmonitor.src.protocols import IProtocols, Ping, Http
from networkmonitor.src.exceptions import InvalidProtocol

class ContextProtocols:

    def __init__(self, protocols:IProtocols):
        # All results are places here
        self.protocols:IProtocols   = protocols

        self.Status:str             = ''
        self.MS:int                 = -1
        pass

    def Start(self):
        if self.protocols.Type.lower() == "icmp":
            p = Ping(self.protocols)
        elif self.protocols.Type.lower() == "http:get":
            p = Http(self.protocols)
        elif self.protocols.Type.lower() == "http:post":
            p = Http(self.protocols)
        else:
            raise InvalidProtocol(f"Requested protocol is not supported: {self.protocols.Type}")
            
        p.Start()
        self.Status = p.Status
        self.MS = int(p.MS)
        pass    