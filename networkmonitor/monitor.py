
import datetime
import typing
from networkmonitor import OldConfig
from networkmonitor.src.configuration import IConfig, ContextConfig
from networkmonitor.src.protocols import IProtocols, ContextProtocols
from networkmonitor.src import Configuration
from networkmonitor.src import Nodes
from networkmonitor.src import InvalidProtocol, InvalidNodeConfiguration
from networkmonitor.src import RefreshTimer

class Monitor():
    """
    Monitor is the working class that checks all the requested nodes.
    """

    def __init__(self, iconfig:IConfig):
        self.__iconfig__:IConfig = iconfig

        self.__config__:ContextConfig = ContextConfig(self.__iconfig__)
        self.__config__.GetWorkingConfigClass(True)
        self.__config__.ReadConfig()

        self.__configuration__:Configuration = Configuration()
        self.__configuration__ = self.__config__.configuration

        self.refresh = RefreshTimer(self.__iconfig__)

        self.report = []       
        self.LastRefresh = datetime.datetime.now()
        self.NextRefresh = datetime.datetime.now()
        pass

    def Start(self, force:bool=False) -> None:
        if force == False:
            res = self.refresh.CheckRefreshTimer()
            #res = self.__CheckRefreshTimer()
            if res == True:
                self.__Worker()
        else:
            self.__Worker()

    def __ReadConfig__(self) -> None:
        self.__config__.ReadConfig()
        self.__configuration__ = Configuration()
        self.__configuration__ = self.__config__.configuration
        
    def __Worker(self)->None:
        self.__ReadConfig__() 
        report = self.__configuration__.nodes
        requirement:bool = True

        for node in report:
            if requirement == True:
                np = node.protocol.lower()
                if np == "icmp":
                    cp = ContextProtocols(IProtocols(node.address, 'ICMP'))
                    cp.GetWorkingClass(True)
                    cp.configuration = self.__configuration__
                    cp.Start()
                elif np == "http:get":
                    cp = ContextProtocols(IProtocols(node.address, "HTTP:GET"))
                    cp.GetWorkingClass(True)
                    cp.Start()
                elif np == "http:post":
                    cp = ContextProtocols(IProtocols(node.address, "Http:Post"))
                    cp.GetWorkingClass(True)
                    cp.Start()
                else:
                    raise InvalidProtocol(f"{node.protocol} is invalid. Use ICMP, HTTP:Get, HTTP:POST.")
                
                node.ms     = cp.MS
                node.status = cp.Status
                
                if node.required == True and node.status == "Offline":
                    requirement = False
            else:
                node.status = "Offline"

            # Work has been finished
            #Copy our local version to the global scope
            self.LastRefresh = datetime.datetime.now()
            self.report = report