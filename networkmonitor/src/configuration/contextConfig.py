
import os

from networkmonitor.src.configuration import IConfig, YamlConfig, JsonConfig
from networkmonitor.src.collections import Nodes

class ContextConfig:
    """
    ConfigContext is the handler for the IConfig and tells the process who needs to do what.

    Methods are the same as IConfig
    """
    def __init__(self, config: IConfig):
        self.config:IConfig     = config
        self.type:str           = self.__GetConfigType__()

        self.SleepInterval:int  = -1
        self.Nodes:Nodes        = []
        pass
    
    def ReadConfig(self):
        if self.type == "yaml":
            y = YamlConfig(self.config)
            y.ReadConfig()
            self.Nodes = y.Nodes
        elif self.type == "json":
            j = JsonConfig(self.config)
            j.ReadConfig()
            self.Nodes = j.Nodes
        else:
            pass
        pass

    def NewConfig(self):
        pass

    def __GetConfigType__(self):
        if self.config.PathConfig.endswith('yaml'):
            return 'yaml'
        elif self.config.PathConfig.endswith('json'):
            return 'json'
        else:
            return None
