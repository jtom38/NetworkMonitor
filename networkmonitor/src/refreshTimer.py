
from datetime import datetime, timedelta
from networkmonitor.src.configuration import *

class RefreshTimer():
    def __init__(self, iconfig:IConfig):
        self.iconfig = iconfig
        self.config = ContextConfig(iconfig)
        self.config.GetWorkingConfigClass(True)
        self.config.ReadConfig()

        self.LastRefresh:datetime = datetime.now()
        self.NextRefresh:datetime = self.LastRefresh
        pass

    def CheckRefreshTimer(self)->bool:
        """
        Gets the time of the last update and adds the SleepTimer value and checks if it needs to run again.
        Returns bool
        """
        #now = self.LastRefresh
        now = datetime.now()
        if now >= self.NextRefresh:
            # Refresh
            self.SetNextRefresh()
            self.LastRefresh = now
            return True
        else:
            return False

    def SetNextRefresh(self)->None:
        n = self.LastRefresh
        si = self.config.configuration.sleepInterval
        td = timedelta(hours=si.hours, minutes=si.minutes, seconds=si.seconds)

        n = n + td

        self.NextRefresh = n

    def GetNextRefresh(self)->str:
        res:str = f"{self.NextRefresh.hour}:{self.NextRefresh.minute}"
        return res

    def GetHour(self, now:datetime, diff:int):
        n = now.hour + diff
        if n >= 24:
            # Get the remainder
            r = n - 24

            # Adjust the new time value
            n = 0 + r
            return [n, r] 

        return [n]
   
    def GetMin(self, now:datetime, diff:int):
        n = now.minute + diff
        if n == 60:
            r = 1
            n = 0
            return [n,r]
        elif n >= 61:
            r = n - 60
            n = r
            return [n,r]
        
        return [n]

    def GetSec(self, now:datetime, diff:int):
        n = now.second + diff
        if n >= 60:            
            r = n - 60
            n = 0 + r
            return [n,r]
        return [n]

    