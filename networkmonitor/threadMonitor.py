
from networkmonitor import Ping, Http, TerminalOutput, Config
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

        self.report = []
        pass

    def Start(self):
        self.WorkerActive = True
        self.__Worker()
        pass

    def __Worker(self):

        while self.WorkerActive == True:
            self.c.UpdateConfig()
            self.report.clear()
            self.report = self.c.nodes

            requirement:bool = True

            for node in self.report:
                #n:Nodes
                #n.
                if requirement == True:

                    np = node.protocol.lower()
                    if np == "icmp":
                        
                        node.status = self.p.PingHost(node.address)
                        node.ms = self.p.ms
                        node.status = self.p.Status
                    elif np == "http:get":
                        node.status = self.h.Get(node.address)
                        #protocol = self.o.AdjustColumn("HTTP:GET", 10)
                    elif np == "http:post":
                        node.status = self.h.Post(node.address)
                        #protocol = self.o.AdjustColumn("HTTP:POST", 10)
                    else:
                        raise InvalidProtocol(f"{node.protocol} is invalid. Use ICMP, HTTP:Get, HTTP:POST.")

                    if node.required == True and node.status == "Offline":
                        requirement = False
                else:
                    node.status = "Offline"
        pass

    def Close(self):
        if self.WorkerActive == True:
            pass
        pass


#m = Monitor("config.json")
#m.Start()
