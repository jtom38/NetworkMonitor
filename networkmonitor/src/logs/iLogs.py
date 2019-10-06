

from os.path import exists
from typing import List
from networkmonitor.src.collections import LogsCol

class ILogs():
    r"""
    About:
    ILog tells ContextLogs about where to look and how to handle log data.
    """
    def __init__(self, DBType:str, DBFile:str):
        self.DBFile:str = DBFile
        self.DBType:str = DBType
        pass

    def Close(self) -> None:
        raise NotImplementedError

    def Add(self, Log:LogsCol) -> bool:
        raise NotImplementedError

    def AddMany(self, Logs:List[LogsCol]) -> bool:
        raise NotImplementedError

    def GetByKey(self, key:str) -> LogsCol:
        raise NotImplementedError

    def GetTop(self, top:int) -> List[LogsCol]:
        raise NotImplementedError

    def GetAll(self) ->List[LogsCol]:
        raise NotImplementedError
