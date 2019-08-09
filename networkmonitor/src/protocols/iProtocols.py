

class IProtocols:
    def __init__(self, URI:str, Type:str):
        #self.Status:str = ''
        #self.MS:int     = -1
        self.URI:str    = URI
        self.Type:str   = Type
        pass

    def Start():
        """
        This is the default method that will be used to talk to a host to get the status of the device.
        """
        pass

