
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
        #self.c = OldConfig(config)
        self.iconfig = config
        #self.CfgContext = ContextConfig(config)
        #self.CfgContext.GetWorkingConfigClass(True)
        #self.CfgContext.ReadConfig()

        self.report = []       
        self.LastRefresh = datetime.datetime.now()
        pass

    def Start(self, force:bool=False):
        if force == False:
            res = self.__CheckRefreshTimer()
            if res == True:
                self.__Worker()
        else:
            self.__Worker()
        
    def __Worker(self):
        self.iconfig.ReadConfig
        report = self.iconfig.Nodes
        requirement:bool = True

        for node in report:
            if requirement == True:
                np = node.protocol.lower()
                if np == "icmp":
                    cp = ContextProtocols(IProtocols(node.address, "ICMP"))
                    cp.GetWorkingClass(True)
                    cp.Start()

                    node.ms     = cp.MS
                    node.status = cp.Status
                elif np == "http:get":
                    i = IProtocols(node.address, "HTTP:Get")
                    cp = ContextProtocols(i)
                    cp.GetWorkingClass(True)
                    cp.Start()

                    node.ms     = cp.MS
                    node.status = cp.Status
                elif np == "http:post":
                    i = IProtocols(node.address, "HTTP:Post")
                    cp = ContextProtocols(i)
                    cp.GetWorkingClass(True)
                    cp.Start()

                    node.status = cp.Status
                    node.ms     = cp.MS
                else:
                    raise InvalidProtocol(f"{node.protocol} is invalid. Use ICMP, HTTP:Get, HTTP:POST.")

                if node.required == True and node.status == "Offline":
                    requirement = False
            else:
                node.status = "Offline"

            # Work has been finished
            #Copy our local version to the global scope
            self.LastRefresh = datetime.datetime.now()
            self.report = report
            #self.Status = 'Offline'
            #self.WorkerActive = False

    def __CheckRefreshTimer(self):
        """
        Gets the time of the last update and adds the SleepTimer value and checks if it needs to run again.
        Returns bool
        """
        

        hour = 0
        mins = 2
        sec  = 0

        last = datetime.datetime.now()
        print(last)

        newHour = last.hour + hour
        if newHour >= 24:
            hour = newHour - 24
            pass

        newMin = last.minute + mins
        if last.minute + mins >= 60:
            mins = newMin - mins
            pass

        newSec = last.second + sec
        if last.second + sec >= 60:
            sec = newSec - sec
            pass

        last = last.replace(hour=newHour, minute=newMin, second=newSec)
        print(last)

        if now <= last:
            print("time is diff")
        print()

        a = self.iconfig.SleepInterval/60
        s = str(a)
        arr = s.split('.')
        
        if arr.__len__() == 3:
            lastHour = self.LastRefresh.hour + int(arr[0])
            lastMin = self.LastRefresh.minute + int(arr[1]) 
            lastSec = self.LastRefresh.second + int(arr[3])
        elif arr.__len__() == 2:
            lastMin = self.LastRefresh.minute + int(arr[0])
            lastSec = self.LastRefresh.second + int(arr[1])

        curTime = datetime.datetime.now()

        if arr.__len__() == 3:
            if lastHour >= curTime.hour and lastMin >= curTime.minute and lastSec >= curTime.second:
                return True
            else:
                return False
        elif arr.__len__() == 2:
            if curTime.minute >= lastMin and curTime.second >= lastSec:
                return True
            else:
                return False
           
    def __StartRest(self):
        self.Status = "Asleep"        
        time.sleep(self.c.SleepTimer)

    def Close(self):
        if self.WorkerActive == True:
            pass
        pass
