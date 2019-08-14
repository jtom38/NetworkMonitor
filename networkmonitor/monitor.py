
import datetime
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

    def __init__(self, config:IConfig):
        self.iconfig = config

        self.CfgContext = ContextConfig(config)
        self.CfgContext.GetWorkingConfigClass(True)
        self.CfgContext.ReadConfig()

        self.refresh = RefreshTimer(config)

        self.report = []       
        self.LastRefresh = datetime.datetime.now()
        self.NextRefresh = datetime.datetime.now()
        pass

    def Start(self, force:bool=False):
        if force == False:
            res = self.refresh.CheckRefreshTimer()

            #res = self.__CheckRefreshTimer()
            if res == True:
                self.__Worker()
        else:
            self.__Worker()
        
    def __Worker(self):
        self.CfgContext.ReadConfig()
        report = self.CfgContext.configuration.nodes
        requirement:bool = True

        for node in report:
            if requirement == True:
                np = node.protocol.lower()
                if np == "icmp":
                    cp = ContextProtocols(IProtocols(node.address, "ICMP"))
                    cp.GetWorkingClass(True)
                    cp.Start()
                elif np == "http:get":
                    i = IProtocols(node.address, "HTTP:Get")
                    cp = ContextProtocols(i)
                    cp.GetWorkingClass(True)
                    cp.Start()
                elif np == "http:post":
                    i = IProtocols(node.address, "HTTP:Post")
                    cp = ContextProtocols(i)
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


