
import datetime

class CleanTime():
    """
    This class cleans and checks the refresh timer.
    If the value is higher then expected it will be cleaned up.

    Methods:

    """
    def __init__(self):
        self.nextDay:bool    = True
        self.hour:int        = 0
        self.minute: int     = 0
        self.second: int     = 0
        pass

    def CleanTime(self):
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
            self.__CleanSecondValue(lastRefresh.second + int(arr[3]))
            self.__CleanMinuteValue(lastRefresh.minute  + int(arr[1]))
            self.__CleanHourValue(lastRefresh.hour    + int(arr[0]))

        elif arr.__len__() == 2:
            self.__CleanMinuteValue(lastRefresh.second + int(arr[1]))
            self.__CleanMinuteValue(lastRefresh.minute + int(arr[0]))
            self.__CleanHourValue(lastRefresh.hour)
            
        elif arr.__len__() == 1:
            self.__CleanMinuteValue(lastRefresh.second + int(arr[1]))
            lastRefresh.minute
            lastRefresh.hour

        return self.__GetMessage()

    def __CleanSecondValue(self, second:int):
        if second >= 60:
            i = second - 60
            self.second = 0
            self.minute += i        
        else:
            self.second = second

    def __CleanMinuteValue(self, minute:int):
        if minute >= 60:
            i = minute - 60
            self.minute = 0
            self.hour += i
        else:
            self.minute = minute

    def __CleanHourValue(self, hour:int):
        if hour >= 24:
            i = hour - 24
            self.hour = 0
        else:
            self.hour = hour

    def __GetMessage(self):
        s:str = ""
        m:str = ""
        h:str = ""

        if self.second <= 9:
            i = str(self.second)
            s = f"0{i}"
        else:
            s = self.second
        
        if self.minute <= 9:
            i = str(self.minute)
            m = f"0{i}"
        else:
            m = self.minute

        if self.hour <= 9:
            i = str(self.hour)
            h = f"0{i}"
        else:
            h = self.hour

        return f"{h}:{m}:{s}"
     