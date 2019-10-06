
import os
import csv
from typing import List

from networkmonitor.src.collections import LogsCol
from networkmonitor.src.logs import ILogs
from networkmonitor.src.exceptions import FailedToGenerateNewFile

class CSV(ILogs):
    """
    This is a logging endpoint to read/write from CSV based files.
    """
    def __init__(self, ILogs:ILogs ):
        self.__ilogs__:ILogs = ILogs
        self.DBType = "csv"
        self.DBFile = ILogs.DBFile

        self.__InitFile__()
        pass

    def __InitFile__(self) -> None:
        if os.path.exists(self.DBFile) == False:
            with open(self.DBFile, mode='w') as csvFile:
                writer = csv.writer(csvFile, delimiter=',')
                writer.writerow(['key', 'level', 'message', 'name', 'address', 'protocol', 'time'])
        pass

    def __ReadCsvFile__(self): 
        records:list = []
        with open(self.DBFile, newline='') as csvFile:
            r = csv.DictReader(csvFile)
            for i in r:
                log:LogsCol =self.__ConvertDictToClass__(i)
                records.append(log)
        return records

    def __AddRow__(self, Log:LogsCol) -> bool:
        try:
            with open(self.DBFile, mode='a') as csvFile:
                writer = csv.writer(csvFile, delimiter=',')
                writer.writerow([Log.key, Log.level, Log.message, Log.name, Log.address, Log.protocol, Log.time] )
                
            return True
        except:
            raise Exception(f"Failed to write the requested log message. {Log.__str__()}")
            #return False
        pass

    def __ConvertDictToClass__(self, dict) -> LogsCol:
        l = LogsCol(
            level=      dict['level'], 
            message=    dict['message'], 
            name=       dict['name'], 
            address=    dict['address'], 
            protocol=   dict['protocol']
        )
        l.key = dict['key']
        l.time = dict['time']
        return l

    def Close(self) -> None:
        # Currently, I do not thing with csv files!  
        # The file is closed as soon as we are done with it
        # I am needed for the interface.
        pass

    def Add(self,Log:LogsCol) -> bool:
        res:bool = False
        res = self.__AddRow__(Log)
        return res

    def AddMany(self, Logs:List[LogsCol] ) -> bool:
        res:bool = False
        for i in Logs:
            res = self.__AddRow__(i)
            if res is False:
                raise FailedToGenerateNewFile(f"Requested Log message containing: {i.name} - {i.message}")        
        return res

    def GetByKey(self, key:str) -> LogsCol:
        """
        Checks the index for the requested key.  
        Returns the record found if any.
        """

        items = self.__ReadCsvFile__()

        for i in items:
            if key == i.key:
                return i

        return LogsCol()

        pass

    def GetTop(self, top:int) -> List[LogsCol]:
        records:List[LogsCol] = self.__ReadCsvFile__()
        
        return records[top-1]

    def GetAll(self) -> List[LogsCol]:
        return self.__ReadCsvFile__()

    def OrderByDate(self, items: List[LogsCol]) -> List[LogsCol]:
        

