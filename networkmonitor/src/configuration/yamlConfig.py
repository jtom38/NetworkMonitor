
import os
import yaml

from networkmonitor.src.configuration import IConfig
from networkmonitor.src.collections import Nodes
from networkmonitor.src.exceptions import FailedToLoadConfigurationFile

class YamlConfig:
    def __init__(self, config: IConfig):
        self.config:IConfig     = config
        self.SleepTimer:int     = -1
        self.Nodes              = []
        pass

    def NewConfig(self):
        """
        Generates a new configuration file based off values given to the class
        """
        pass

    def ReadConfig(self):
        p = os.path.abspath(self.config.PathConfig)
        if os.path.exists(p) == True:
            try:
                with open(self.config.PathConfig) as yamlFile:
                    raw = yaml.load(yamlFile)
                    self.SleepTimer = raw['SleepInterval']
                    self.__ParseNodes(raw)
            except FailedToLoadConfigurationFile:
                print(f'Configuration file was found at {p}.  Ran into a problem loading the file into memory.  Was the file locked?  Is the file format wrong?')
        else:
            pass

        pass

    def __ParseNodes(self, raw:str):
        for d in raw['Nodes']:
            try:
                node = Nodes(d['Name'], d['Address'], d['Protocol'])
            except Exception:
                pass

            try:
                if d['Required'] == True:
                    node.required = True
            except:
                node.required = False
            
            try:
                c:str = d['Category']
                if c.__contains__('') == True:
                    node.category == ''
                else:
                    node.category == c
            except:
                node.category = ''

            self.Nodes.append(node)
        pass