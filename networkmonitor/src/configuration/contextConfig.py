
import os

from networkmonitor.src.configuration import IConfig, YamlConfig, JsonConfig
from networkmonitor.src.collections import Configuration

class ContextConfig:
    """
    ConfigContext is the handler for the IConfig and tells the process who needs to do what.
    
    Methods are the same as IConfig
    """
    def __init__(self, config: IConfig):
        self.config:IConfig     = config
        self.type:str           = self.__GetConfigType__()

        self.configuration      = Configuration()
        #self.SleepInterval:int  = -1
        #self.Nodes:Nodes        = []
        pass

    def __GetConfigType__(self):

        # Did we get our IConfig on its own?
        try:
            if self.config.argPathConfig.endswith('yaml'):
                return 'yaml'
            elif self.config.argPathConfig.endswith('json'):
                return 'json'
            else:
                return None
        except:
            pass

        # it came in with another class attached.
        # Looks like it should be YamlConfig or JsonConfig then IConfig
        try:
            if self.config.config.PathConfig.endswith('yaml'):
                return 'yaml'
            elif self.config.config.PathConfig.endswith('json'):
                return 'json'
            else:
                return None
        except:
            pass

    def GetWorkingConfigClass(self, replaceConfig:bool = False):
        """
        This is used to generate a working class based off the config type.
        If we know the type and have a class we can use, make a new instance and return it.
        Currently returns YamlConfig or JsonConfig.

        @param:replaceConfig = If True it will take the generated class and place it in self.config.  If False, return value.
        """
        if self.type == "yaml":
            c = YamlConfig(self.config)
            return self.__ReplaceWorkingConfig(replaceConfig, c)
        elif self.type == "json":
            j = JsonConfig(self.config)
            return self.__ReplaceWorkingConfig(replaceConfig, j)

        else:
            pass
        
    def __ReplaceWorkingConfig(self, replaceConfig:bool, passedClass):
        if replaceConfig == True:
            self.config = passedClass
        else:
            return passedClass

    def ReadConfig(self):
        self.configuration.nodes = []
        self.config.ReadConfig()
        self.configuration = self.config.configuration
        #self.configuration.nodes = self.config.nodes
        #self.configuration.sleepInterval = self.config.sleepInterval
        #self.Nodes          = self.config.config.Nodes
        #self.SleepInterval  = self.config.config.SleepInterval
        pass

    def NewConfig(self):
        """
        Handler for NewConfig requests.        
        """
        default = {
            "SleepInterval":{
                "Hours": 0,
                "Minutes": 2,
                "Seconds": 0
            },
            "Protocols":{
                "ICMP":{
                    "Timeout":0
                }
            },
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

