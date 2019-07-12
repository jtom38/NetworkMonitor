
"""
This contains the collections that can be used within the application
"""

class LogsCol():
    """
    LogsCol contains the format for how log data will be stored in memory
    """
    

    def __init__(self, level:str ='',message:str = '', name:str = '', 
                address:str = '', protocol:str='' ):
        import datetime
        self.level      = level
        self.message    = message
        self.name       = name
        self.address    = address
        self.protocol   = protocol
        self.time       = datetime.datetime.now()

        pass    
    pass

class NodesCol():
    """
    NodesCol contains a record for the nodes.  Use this in an list to store the records.
    """
    def __init__(self):
        pass
