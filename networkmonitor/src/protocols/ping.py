import platform
import typing
import subprocess

from networkmonitor.src.protocols import IProtocols
from networkmonitor.src.configuration import *
from networkmonitor.src import Configuration

class Ping:
    def __init__(self, protocol:IProtocols):
        self.Protocol:IProtocols    = protocol


        #self.iconfig:IConfig        = iconfig
        #self.config:ContextConfig   = ContextConfig(self.iconfig)
        #self.config.GetWorkingConfigClass(True)
        #self.config.ReadConfig()

        self.configuration:Configuration = Configuration()

        self.Status:str             = ''
        self.MS:int                 = -1
        pass

    def Start(self):
        r"""
        Pings the requested host.

        :param hostname: defines url
        """
        
        URI = self.__CleanURI(self.Protocol.URI)
        cmd = self.__GetCommand(URI)
        try:
            d = subprocess.run(cmd, stdout=subprocess.PIPE ,stderr=subprocess.PIPE)
            self.__ProcessReturnCode(d.returncode)
            self.__ProcessTravelTime(str(d.stdout))
        except:
            pass

    def __CleanURI(self, URI:str):
        if URI.lower().__contains__('http') == True:
            URI = URI.replace("http://", "")
        
        if URI.lower().__contains__('https://') == True:
            URI = URI.replace("https://", '')

        return URI

    def __GetCommand(self, URI:str):
        if platform.system().lower() == "windows":       
            param = '-n'
        else:
            param = '-c'
        pass

        #if self.configuration.protocols.icmp.timeout >= 0:
        #    timeout = self.configuration.protocols.icmp.timeout
        #    if platform.system().lower() == "windows":
        #        timeoutParam = '-W'
        #    else:
        #        timeoutParam = '-W'
        #    pass
        #
        #    return ['ping', param, '1', timeoutParam, str(timeout), URI]

        return ['ping', param, '1', URI]
 
    def __ProcessReturnCode(self, returncode:int ):
        if returncode == 0:
            self.Status = 'Online'        
        else:
            self.Status = 'Offline'

    def __ProcessTravelTime(self, stdout:str):
        s:str = str(stdout)

        if platform.system().lower() == 'windows':
            pass
        else:

            # Extract the first value
            time = s.find('time=')
            ms = s.find(' ms')
            t = s[time:ms]
            time:str = t.replace('time=', '')

            # Remove .xxx
            i = time.find('.')
            t = time[0:i]
            
            # store the result
            self.MS = int(t)
        