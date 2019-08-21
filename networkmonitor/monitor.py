
import datetime
import typing
from networkmonitor import OldConfig
from networkmonitor.src.configuration import *
from networkmonitor.src.protocols import *
from networkmonitor.src import Nodes
from networkmonitor.src import InvalidProtocol, InvalidNodeConfiguration
#from networkmonitor.src import CleanTime
from networkmonitor.src import RefreshTimer

class Monitor():
    """
    Monitor is the working class that checks all the requested nodes.
    """

    def __init__(self, iconfig:IConfig):
        self.iconfig = iconfig

        self.config = ContextConfig(self.iconfig)
        self.config.GetWorkingConfigClass(True)
        self.config.ReadConfig()

        self.refresh = RefreshTimer(self.iconfig)

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
        
    def __Worker(self)->None:
        self.config.ReadConfig()
        report = self.config.configuration.nodes
        requirement:bool = True

        for node in self.config.configuration.nodes:
            if requirement == True:
                np = node.protocol.lower()
                if np == "icmp":
                    p = IProtocols(node.address, 'ICMP')
                    p.configuration = self.config.configuration
                    cp = ContextProtocols(p)
                    
                    cp.GetWorkingClass(True)
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


