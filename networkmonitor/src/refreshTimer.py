
import datetime

class RefreshTimer():
    def __init__(self):
        
        pass

    def __CheckRefreshTimer(self):
        """
        Gets the time of the last update and adds the SleepTimer value and checks if it needs to run again.
        Returns bool
        """
        now = self.LastRefresh
        newHour = now.hour + self.CfgContext.configuration.sleepInterval.hours
        if newHour >= 24:
            newHour = newHour - 24
            pass

        newMin = now.minute + self.CfgContext.configuration.sleepInterval.minutes
        if newMin >= 60:
            newMin = newMin - 60
            pass

        newSec = now.second + self.CfgContext.configuration.sleepInterval.seconds
        if newSec >= 60:
            newSec = newSec - 60
            pass

        now = now.replace(hour=newHour, minute=newMin, second=00)

        if self.LastRefresh >= now:
            # Refresh
            self.SetNextRefresh()
            self.LastRefresh = now
            return True

    def SetNextRefresh(self):
        n = self.LastRefresh

        newSec = n.second + self.CfgContext.configuration.sleepInterval.seconds
        if newSec >= 60:
            newSec = newSec - 60
            pass

        newMin = n.minute + self.CfgContext.configuration.sleepInterval.minutes
        if newMin >= 60:
            newMin = newMin - 60
            pass

        newHour = n.hour + self.CfgContext.configuration.sleepInterval.hours
        if newHour >= 24:
            newHour = newHour - 24
            pass

        n = n.replace(hour=newHour, minute=newMin, second=00)

    def GetNextRefresh(self):
        now = datetime.datetime.now()
        newHour = now.hour + self.CfgContext.configuration.sleepInterval.hours
        if newHour >= 24:
            newHour = newHour - 24
            pass

        newMin = now.minute + self.CfgContext.configuration.sleepInterval.minutes
        if newMin >= 60:
            newMin = newMin - 60
            pass

        newSec = now.second + self.CfgContext.configuration.sleepInterval.seconds
        if newSec >= 60:
            newSec = newSec - 60
            pass

        return f"{now.hour}:{now.minute}"


    
