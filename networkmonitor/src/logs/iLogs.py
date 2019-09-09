

class ILogs():
    r"""
    About:
    ILog tells ContextLogs about where to look and how to handle log data.
    """
    def __init__(self):
        self.DBType:str = "sqlite"
        self.DBFile:str = "networkmonitor.sqlite"
        pass