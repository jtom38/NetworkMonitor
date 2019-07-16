
from datetime import datetime

class Helper():
    def __init__(self):
        pass
    
    def GetNextNodeRefreshTime(self, sleepTimer:int, lastRefresh:datetime):
        """
        Returns the second value before nodes are checked again
        :param sleepTimer   = Contains the sleep timer value from config
        :param lastRefresh  = Contains the datetime value of the last refresh
        """
        
        # Convert lastRefresh into long seconds based off sleepTimer value
        a:float = sleepTimer / 60
        s:str = str(a)
        arr = s.split('.')

        if arr.__len__() == 3:
            hour =      lastRefresh.hour    + int(arr[0])
            minute =    lastRefresh.minute  + int(arr[1])
            sec =       lastRefresh.second  + int(arr[2])
        elif arr.__len__() == 2:
            hour        = lastRefresh.hour
            minute      = lastRefresh.minute + int(arr[0])
            sec         = lastRefresh.second + int(arr[1])
        elif arr.__len__() == 1:
            hour        = lastRefresh.hour
            minute      = lastRefresh.minute
            sec         = lastRefresh.second + int(arr[1])

        return f"{hour}:{minute}:{sec}"



