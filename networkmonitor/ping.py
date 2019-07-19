import platform
import typing
import subprocess

class Ping:

    def __init__(self):
        self.Status:str = ''
        self.ms:int     = -1
        self.URI:str    = ''
        pass

    def PingHost(self, hostname:str):
        """
        Pings the requested host.

        :param hostname: defines url
        """

        self.URI = hostname

        self.__CleanURI()

        cmd = self.__GetCommand()

        #return call(cmd, stdout=DEVNULL, stderr=STDOUT)
        try:
            d = subprocess.run(cmd, stdout=subprocess.PIPE ,stderr=subprocess.PIPE)

            self.__ProcessReturnCode(d.returncode)
            self.__ProcessTravelTime(d.stdout)
            
        except:
            pass

    def __CleanURI(self):
        if self.URI.lower().__contains__('http') == True:
            self.URI = self.URI.replace("http://", "")
        
        if self.URI.lower().__contains__('https://') == True:
            self.URI = self.URI.replace()

    def __GetCommand(self):
        if platform.system().lower() == "windows":       
            param = '-n'
        else:
            param = '-c'
        pass

        return ['ping', param, '1', self.URI]
 
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
        