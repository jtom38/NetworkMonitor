

class IConfig:
    """
    IConfig is a interface to be used with the configuration loader.
    This acts as a template for how the Config works.
    Once this is filled in call ConfigContext and pass this in
    """

    def __init__(self, PathConfig:str, NewConfig = False):
        self.PathConfig:str = PathConfig
        self.NewConfig:bool = NewConfig
        pass

    def ReadConfig(self):
        """
        Reads the configuration file stored in memory and processes what it finds.
        """
        pass

    def NewConfig(self):
        """
        When requested we will generated a new configuration file 
        """
        pass
        
