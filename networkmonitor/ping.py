import platform
from subprocess import DEVNULL, STDOUT, call

from .terminal import TerminalOutput

class Ping:

    def __init__(self):
        pass

    def ProcessICMP(self, URI:str):

        res = self.PingHost(URI)
        if res == 0:
            status:str = "Online"       
        else:
            status:str = "Offline"

        return status

    def PingHost(self, hostname:str):
        if platform.system().lower() == "windows":       
            param = '-n'
        else:
            param = '-c'
        pass

        cmd = ['ping', param, '1', hostname]
        return call(cmd, stdout=DEVNULL, stderr=STDOUT)
        

#if __name__ == "__main__":
    #Ping
    #pass