
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

class Nodes():
    """
    NodesCol contains a record for the nodes from the config file.  Use this in an list to store the records.
    name = Contains the user defined name
    address = Contains the address to monitor
    protocol = Defines how to test
    required = Defines if this needs to be active if failure happens.
    category = Defines the user 
    """
    def __init__(self, name:str, address:str, protocol:str):
        self.name:str       = name
        self.address:str    = address
        self.protocol:str   = protocol
        self.required:bool  = False
        self.category:str   = ''
        self.status:str     = ''
        self.message:str    = ''
        pass

class NodeStatusCol():
    """
    NodeStatusCol contains the active information for each of the nodes health.
    """
