
import time
import datetime
from networkmonitor import Ping, Http, OldConfig
from networkmonitor.src import Nodes
from networkmonitor.src import InvalidProtocol, InvalidNodeConfiguration
from networkmonitor.src import CleanTime


class Monitor():
    """
    Monitor is the working class that checks all the requested nodes.
    """

    def __init__(self, config:str = ''):
        self.p = Ping()
        self.h = Http()
        #self.o = Helper()
        self.c = OldConfig(config)

        #self.WorkerActive = False
        #self.Status = "Unknown"

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

        #while self.WorkerActive == True:
        #self.Status = "Alive"
        self.c.UpdateConfig()
            
        report = self.c.nodes
        #with self.threadLock:
        #    globalVars.reports = report

        requirement:bool = True

        for node in report:
            if requirement == True:
                np = node.protocol.lower()
                if np == "icmp":
                    p = Ping()
                    p.PingHost(node.address)
                    node.ms     = p.ms
                    node.status = p.Status
                elif np == "http:get":
                    h = Http()
                    h.Get(node.address)
                    node.ms     = h.ms
                    node.status = h.status
                elif np == "http:post":
                    h = Http()
                    h.Post(node.address)
                    node.status = h.status
                    node.ms     = h.ms
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
        a = self.c.SleepTimer / 60
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
