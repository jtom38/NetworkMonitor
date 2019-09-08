
from typing import List
from networkmonitor.src import LogsCol
import sqlite3

class ContextLogs:
    def __init__(self):
        #self.logs: List[LogsCol] = [] 
        sqlite3.connect()
        pass
    
    def AddLog(self, Log: LogsCol):
        #self.logs.append(Log)
        pass