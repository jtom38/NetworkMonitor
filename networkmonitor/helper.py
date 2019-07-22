
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

    def AdjustColumn(self, value:str, Width:int):
        """
        Formats the value to size correctly in the desired width of the column

        :param value: Contains the str that will be displayed
        :param Width: Defines how many characters wide the text needs to be sized to

        :retuns: str
        """   
        if value.__len__() < Width:
            while value.__len__() < Width:
                value = f"{value} "

        elif value.__len__() > Width:
            value = value[0:Width]
        return value




