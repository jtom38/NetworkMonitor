
from networkmonitor.src.protocols import IProtocols, Ping, Http
from networkmonitor.src.configuration import *
from networkmonitor.src.exceptions import InvalidProtocol

class ContextProtocols:

    def __init__(self, protocols:IProtocols):
        # All results are places here
        self.protocols:IProtocols   = protocols
        #self.iconfig:IConfig        = iconfig

        #self.__config__:ContextConfig(self.iconfig)
        #self.__config__.GetWorkingConfigClass(True)
        #self.__config__.ReadConfig()

        self.Status:str             = ''
        self.MS:int                 = -1
        pass

    def Start(self):
        self.protocols.Start()
        self.Status = self.protocols.Status
        self.MS = int(self.protocols.MS)
        pass   
    
    def GetWorkingClass(self, replaceInterface:bool = False):
        """
        This is used to generate a working class based off the config type.
        If we know the type and have a class we can use, make a new instance and return it.
        Currently returns YamlConfig or JsonConfig.

        @param:replaceInterface = If True it will take the generated class and place it in self.config.  If False, return value.
        """
        if self.protocols.Type.lower() == "icmp":
            p = Ping(self.protocols)
        elif self.protocols.Type.lower() == "http:get":
            p = Http(self.protocols)
        elif self.protocols.Type.lower() == "http:post":
            p = Http(self.protocols)
        else:
            raise InvalidProtocol(f"Requested protocol is not supported: {self.protocols.Type}")

        if replaceInterface == True:
            self.protocols = p
        else: 
            return p
