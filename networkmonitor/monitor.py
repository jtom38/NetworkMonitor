
import datetime
from networkmonitor import OldConfig
from networkmonitor.src.configuration import *
from networkmonitor.src.protocols import *
from networkmonitor.src import Nodes
from networkmonitor.src import InvalidProtocol, InvalidNodeConfiguration
from networkmonitor.src import CleanTime

class Monitor():
    """
    Monitor is the working class that checks all the requested nodes.
    """

    def __init__(self, config:IConfig):
        self.iconfig = config

        self.CfgContext = ContextConfig(config)
        self.CfgContext.GetWorkingConfigClass(True)
        self.CfgContext.ReadConfig()

        self.report = []       
        self.LastRefresh = datetime.datetime.now()
        self.NextRefresh = datetime.datetime.now()
        pass

    def Start(self, force:bool=False):
        if force == False:
            res = self.__CheckRefreshTimer()
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


    def __CheckRefreshTimer(self):
        """
        Gets the time of the last update and adds the SleepTimer value and checks if it needs to run again.
        Returns bool
        """
        now = self.LastRefresh
        newHour = now.hour + self.CfgContext.configuration.sleepInterval.hours
        if newHour >= 24:
            newHour = newHour - 24
            pass

        newMin = now.minute + self.CfgContext.configuration.sleepInterval.minutes
        if newMin >= 60:
            newMin = newMin - 60
            pass

        newSec = now.second + self.CfgContext.configuration.sleepInterval.seconds
        if newSec >= 60:
            newSec = newSec - 60
            pass

        now = now.replace(hour=newHour, minute=newMin, second=00)

        if self.LastRefresh >= now:
            # Refresh
            self.SetNextRefresh()
            self.LastRefresh = now
            return True

    def SetNextRefresh(self):
        n = self.LastRefresh

        newSec = n.second + self.CfgContext.configuration.sleepInterval.seconds
        if newSec >= 60:
            newSec = newSec - 60
            pass

        newMin = n.minute + self.CfgContext.configuration.sleepInterval.minutes
        if newMin >= 60:
            newMin = newMin - 60
            pass

        newHour = n.hour + self.CfgContext.configuration.sleepInterval.hours
        if newHour >= 24:
            newHour = newHour - 24
            pass

        n = n.replace(hour=newHour, minute=newMin, second=00)

    def GetNextRefresh(self):
        now = datetime.datetime.now()
        newHour = now.hour + self.CfgContext.configuration.sleepInterval.hours
        if newHour >= 24:
            newHour = newHour - 24
            pass

        newMin = now.minute + self.CfgContext.configuration.sleepInterval.minutes
        if newMin >= 60:
            newMin = newMin - 60
            pass

        newSec = now.second + self.CfgContext.configuration.sleepInterval.seconds
        if newSec >= 60:
            newSec = newSec - 60
            pass

        return f"{now.hour}:{now.minute}"
