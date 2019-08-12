
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
        self.config.ReadConfig()
        self.Nodes          = self.config.config.Nodes
        self.SleepInterval  = self.config.config.SleepInterval
        #if self.type == "yaml":
        #    y = YamlConfig(self.config)
        #    y.ReadConfig()
        #    self.Nodes = y.Nodes
        #elif self.type == "json":
        #    j = JsonConfig(self.config)
        #    j.ReadConfig()
        #    self.Nodes = j.Nodes
        #else:
        #    pass
        pass

    def NewConfig(self):
        """
        Handler for NewConfig requests.        
        """
        default = {
            "SleepInterval": "120",
            'Nodes': [
                {
                    'Name':'LocalHost',
                    'Address': '172.0.0.1',
                    'Protocol': 'ICMP',
                    'Required': True,
                    'Category': "local"
                },
                {
                    'Name'      : 'Wan',
                    'Address'   : '192.168.0.1',
                    'Protocol'  : 'ICMP',
                    'Required'  : True,
                    'Category'  : "Local"
                },
                {
                    'Name'      : 'Google',
                    'Address'   : 'google.com',
                    'Protocol'  : 'ICMP',
                    'Required'  : False,
                    'Category'  : "External"
                },
                {
                    'Name'      : 'Google',
                    'Address'   : 'https://google.com',
                    'Protocol'  : 'Http:Get',
                    'Required'  : False,
                    'Category'  : "External"
                } 
            ]
        }
        self.config.NewConfig(default)        
        pass

    def __GetConfigType__(self):
        if self.config.config.PathConfig.endswith('yaml'):
            return 'yaml'
        elif self.config.config.PathConfig.endswith('json'):
            return 'json'
        else:
            return None
