
from os.path import exists
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

    def AddLog(self, Log:LogsCol) -> bool:
        raise NotImplementedError

    def CloseConnection(self) -> None:
        raise NotImplementedError