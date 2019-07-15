
import time
import datetime
#import threading
from networkmonitor import Ping, Http, TerminalOutput, Config, globalVars
from networkmonitor import Nodes
from networkmonitor import InvalidProtocol, InvalidNodeConfiguration


class Monitor():
    """
    Monitor is the working class that checks all the requested nodes.
    """

    def __init__(self, config:str = ''):
        self.p = Ping()
        self.h = Http()
        self.o = TerminalOutput()
        self.c = Config(config)

        self.WorkerActive = False
        self.Status = "Unknown"

        self.report = []       
        self.LastRefresh = datetime.datetime.now()
        pass

    def Start(self):
        self.__CheckRefreshTimer()
        self.WorkerActive = True
        self.__Worker()
        pass

    def __Worker(self):

        while self.WorkerActive == True:
            self.Status = "Alive"
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
            self.Status = 'Offline'
            self.WorkerActive = False

    def __CheckRefreshTimer(self):
        curTime = datetime.datetime.now()

        a = self.c.SleepTimer / 60
        a = str(a)
        arr = a.split('.')
        nt = self.LastRefresh.replace(minute=self.LastRefresh.minute+a[0])
        
        print(nt)
        

    def __StartRest(self):
        self.Status = "Asleep"        
        time.sleep(self.c.SleepTimer)

    def Close(self):
        if self.WorkerActive == True:
            pass
        pass

    @staticmethod
    def GetReport(self):
        return self.report

