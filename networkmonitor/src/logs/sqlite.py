
import datetime
from networkmonitor.src.collections import LogsCol
from networkmonitor.src.logs import ILogs
from sqlite3 import connect, Cursor
import sqlite3

class SQLite:
    def __init__(self, ILogs:ILogs) -> None:
        self.__ilogs__:ILogs = ILogs 

        self.table:str  = "logs"
        self.file:str   = ILogs.DBFile
        
        self.sql:connect = connect(self.file)
        self.cursor: Cursor = self.sql.cursor()        
        self.__generatetable__()
        pass

    def __generatetable__(self) -> bool:
        command:str = f'''Create TABLE {self.table} (
            key         TEXT PRIMARY KEY, 
            level       TEXT, 
            message     TEXT, 
            name        TEXT, 
            address     TEXT, 
            protocol    TEXT, 
            time        NUMERIC)'''
        try:
            self.cursor.execute(command)
            self.sql.commit()
            return True
        except:
            return False

    def __convertToSqlTime__(self, logtime:datetime.datetime) -> sqlite3.Time:
        try:
            t = sqlite3.Time(hour=logtime.hour, minute=logtime.minute, )
            return t
        except:
            return None

    def Close(self) -> None:
        try:
            self.cursor.close()
        except:
            pass
    
    def Add(self, Log: LogsCol) -> bool:
        sqlTime = self.__convertToSqlTime__(Log.time)
        
        self.cursor.execute(f"Insert INTO {self.table} (key, level, message, name, address, protocol, time) Values ('{Log.key}', '{Log.level}', '{Log.message}', '{Log.name}', '{Log.address}', '{Log.protocol}', '{sqlTime}')")

    def GetByKey(self, key:str):
        res =  self.cursor.execute(f"Select * from {self.table} where key = '{key}' ")
        return res

    def GetTop(self,top:int):
        res =  self.cursor.execute(f"Select * from {self.table} Top 1")
        return res
        