
from networkmonitor.src.protocols import IProtocols, Ping

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
            p.Start()
            self.Status = p.Status
            self.MS = p.ms

        
        pass    