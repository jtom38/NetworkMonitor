import platform
from subprocess import DEVNULL, STDOUT, call

class Ping:

    def __init__(self):
        pass

    def PingHost(self, hostname:str):
        if platform.system().lower() == "windows":       
            param = '-n'
        else:
            param = '-c'
        pass

        cmd = ['ping', param, '1', hostname]
        return call(cmd, stdout=DEVNULL, stderr=STDOUT)
        

if __name__ == "__main__":
    Ping
    pass