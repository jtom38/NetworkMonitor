
import typing
import uuid
import datetime

"""
This contains the collections that can be used within the application
"""

class LogsCol():
    """
    LogsCol contains the format for how log data will be stored in sql.
    """

    def __init__(self, level:str ='',
        message:str = '', 
        name:str = '', 
        address:str = '', 
        protocol:str='' ):

        self.key:str                = str(uuid.uuid4())
        self.level:str              = level
        self.message:str            = message
        self.name:str               = name
        self.address:str            = address
        self.protocol:str           = protocol
        self.time:datetime.datetime = datetime.datetime.now()
        pass    

    def __str__(self) -> str:
        """
        Converts the message to a string based result.
        """
        return f"{self.time} - {self.level} - {self.protocol} - {self.message}"

class Configuration():
    def __init__(self):
        self.sleepInterval:SleepInterval    = SleepInterval()
        self.protocols:CfgProtocols         = CfgProtocols() 
        self.nodes                          = []

        pass


class SleepInterval():
    r"""
    This is used as part of Configuration to define the sleep timeout configuration
    """
    def __init__(self):
        self.hours:int      = 0
        self.minutes:int    = 0
        self.seconds:int    = 0
        pass

class CfgProtocols():
    def __init__(self):
        self.icmp:CfgIcmp   = CfgIcmp()

class CfgIcmp():
    def __init__(self):
        self.timeout:int    = 0

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
        self.ms:int         = -1
        self.message:str    = ''
        pass

class NodeStatusCol():
    """
    NodeStatusCol contains the active information for each of the nodes health.
    """
