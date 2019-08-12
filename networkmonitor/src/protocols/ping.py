import platform
import typing
import subprocess

from networkmonitor.src.protocols import IProtocols

class Ping:
    def __init__(self, protocol:IProtocols):
        self.Protocol:IProtocols    = protocol

        self.Status:str             = ''
        self.MS:int                 = -1
        #self.URI:str                = ''
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
            self.__ProcessTravelTime(d.stdout)
        except:
            pass

    def __CleanURI(self, URI:str):
        if URI.lower().__contains__('http') == True:
            URI = URI.replace("http://", "")
        
        if URI.lower().__contains__('https://') == True:
            URI = URI.replace()

        return URI

    def __GetCommand(self, URI:str):
        if platform.system().lower() == "windows":       
            param = '-n'
        else:
            param = '-c'
        pass

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
            time = s.find('time')
            ms = s.find(' ms')
            t = s[time:ms]
            time:str = t.replace('time=', '')

            # Remove .xxx
            i = time.find('.')
            t = time[0:i]
            
            # store the result
            self.ms = int(t)
        