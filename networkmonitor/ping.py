import platform
#from subprocess import DEVNULL, STDOUT, call, run
import subprocess

from .terminal import TerminalOutput

class Ping:

    def __init__(self):
        pass

    def ProcessICMP(self, URI:str):
        
        if URI.lower().__contains__('http') == True:
            URI = URI.replace("http://", "")
        
        if URI.lower().__contains__('https://') == True:
            URI = URI.replace()

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
        #return call(cmd, stdout=DEVNULL, stderr=STDOUT)
        try:
            d = subprocess.run(cmd, stderr=subprocess.STDOUT)
            #d = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
            print(d)
        except:
            pass
        

#if __name__ == "__main__":
    #Ping
    #pass