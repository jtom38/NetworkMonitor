

class IConfig:
    """
    IConfig is a interface to be used with the configuration loader.
    This acts as a template for how the Config works
    """

    def __init__(self, PathConfig:str, NewConfig = False):
        self.PathConfig:str = PathConfig
        self.ConfigType:str = ""
        self.NewConfig:bool = NewConfig

        if PathConfig.endswith('.yaml'):
            self.ConfigType = "yaml"
        elif PathConfig.endswith(".json"):
            self.ConfigType = "json"
        else:
            self.ConfigType = "error"
        pass

    def UpdateConfig(self):
        pass

    def MakeNewConfig(self):
        """
        When requested we will generated a new configuration file 
        """
        pass
        
