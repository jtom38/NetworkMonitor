
from networkmonitor.src.collections import LogsCol
from networkmonitor.src.logs import ILogs
from sqlite3 import connect, Cursor

class SQLite:
    def __init__(self, ILogs:ILogs) -> None:
        self.__ilogs__:ILogs = ILogs 

        self.table:str  = "logs"
        self.file:str   = "networkmonitor.sqlite"
        
        self.sql:connect = connect(self.file)
        self.cursor: Cursor = self.sql.cursor()        
        self.__generatetable__()
        pass

    def __generatetable__(self) -> False:
        command:str = "Create TABLE logs (key PRIMARY KEY, level, message, name, address, protocol, time)"
        try:
            self.cursor.execute(command)
            return True
        except:
            return False
    
    def AddLog(self, Log: LogsCol):
        #self.logs.append(Log)
        pass