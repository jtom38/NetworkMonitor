
from networkmonitor.src.exceptions import InvalidProtocol
from networkmonitor.src.collections import LogsCol
from networkmonitor.src.logs import ILogs, SQLite

class ContextLogs:
    r"""
    ContextLogs
    """
    def __init__(self, ILog: ILogs) -> None:
        self.__ilogs__: ILogs = ILog

        self.DBType = ILog.DBType
        self.DBFile = ILog.DBFile

        
        pass

    def __GetClass__(self) -> None:
        if self.DBType.lower() == "sqlite":
            l = SQLite(self.__ilogs__)
        else:
            raise InvalidProtocol(f"Requested Log type is not supported.  See Documentation for supported log types.")
        
        self.interface = l

    def AddLog(self, Log: LogsCol) -> None:
        self.interface.AddLog(log)
        pass

