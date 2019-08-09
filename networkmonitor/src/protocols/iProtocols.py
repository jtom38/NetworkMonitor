

class IProtocols:
    def __init__(self):
        #self.Status:str = ''
        #self.MS:int     = -1
        self.URI:str    = ""
        self.Type:str   = ""
        pass

    def Start():
        """
        This is the default method that will be used to talk to a host to get the status of the device.
        """
        pass

