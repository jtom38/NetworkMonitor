
from os.path import exists

from networkmonitor.src.exceptions import InvalidLogType
from networkmonitor.src.collections import LogsCol
from networkmonitor.src.logs import ILogs, SQLite

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
        types:[str] = ['sqlite']
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
        else:
            pass
            
        self.interface = l

    def CloseConnection(self) -> None:
        self.interface.CloseConnection()
        pass

    def AddLog(self, Log: LogsCol) -> bool:        
        self.interface.AddLog(Log)
        pass

