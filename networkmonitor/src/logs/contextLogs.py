
from os.path import exists
from typing import List

from networkmonitor.src.exceptions import InvalidLogType
from networkmonitor.src.collections import LogsCol
from networkmonitor.src.logs import ILogs, SQLite, CSV

class ContextLogs:
    r"""
    ContextLogs
    """
    def __init__(self, ILog: ILogs) -> None:
        self.__ilogs__: ILogs = ILog
        self.__CheckInterface__()

        self.DBType = ILog.DBType
        self.DBFile = ILog.DBFile
        self.__GetClass__()
        pass

    def __CheckInterface__(self) -> None:
        types:[str] = ['sqlite', 'csv']
        TypeValid:bool = False

        # Check the type for the log source
        for i in types:
            if self.__ilogs__.DBType.lower() == i:
                TypeValid = True

        if TypeValid == False:
            raise InvalidLogType(f"Log type of:{self.__ilogs__.DBType} is not supported.  Use SQLite.")

    def __GetClass__(self) -> None:
        if self.DBType.lower() == "sqlite":
            l = SQLite(self.__ilogs__)
        elif self.DBType.lower() == "csv":
            l = CSV(self.__ilogs__)
        else:
            pass
            
        self.__interface__ = l

    def Close(self) -> None:
        """
        This releases the currently locked resources.
        Run this when you are done working with the desired worker.
        """
        self.__interface__.Close()
        pass

    def Add(self, Log: LogsCol) -> bool:        
        """
        This adds a single record to the worker.
        """
        res:bool = False
        res = self.__interface__.Add(Log)
        return res

    def AddMany(self, Logs:List[LogsCol]) -> bool:
        res:bool = False
        res = self.__interface__.AddMany(Logs)
        return res

    def GetByKey(self, key:str) -> LogsCol:
        self.__interface__.GetByKey(key)

    def GetTop(self, top:int) -> List[LogsCol]:
        res = self.__interface__.GetTop(top)
        return res


