
import os
import yaml
import json

from networkmonitor.src.configuration import IConfig
from networkmonitor.src.collections import Nodes, SleepInterval
from networkmonitor.src.exceptions import FailedToLoadConfigurationFile, FailedToGenerateNewFile

class YamlConfig(IConfig):
    def __init__(self, config: IConfig):
        self.config:IConfig                 = config
        self.sleepInterval:SleepInterval    = SleepInterval()
        self.nodes                          = []
        pass

    def NewConfig(self, defaultConfig):
        """
        Generates a new configuration file based off values given to the class
        """
        if os.path.exists(self.config.PathConfig) == True:
            raise FailedToGenerateNewFile(f"Attempted to generate a new file at {self.config.PathConfig} because a file was already present.  Pick a different file name or remove the existing file.")

        with open("example.yaml", mode='r') as default:
            y = yaml.safe_load(default)

        with open(self.config.PathConfig, mode='w') as yamlFile:
            yaml.dump(y, yamlFile, default_flow_style=False)
            
        
        pass

    def ReadConfig(self):
        p = os.path.abspath(self.config.PathConfig)
        if os.path.exists(p) == True:
            try:
                with open(self.config.PathConfig) as yamlFile:
                    raw = yaml.safe_load(yamlFile)

                    self.__ParseSleepInterval(raw['SleepInterval'])
                    self.__ParseNodes(raw)
            except FailedToLoadConfigurationFile:
                print(f'Configuration file was found at {p}.  Ran into a problem loading the file into memory.  Was the file locked?  Is the file format wrong?')
        else:
            pass

        pass

    def __ParseSleepInterval(self, json:str):
        self.sleepInterval.hours    = json['Hours']
        self.sleepInterval.minutes  = json['Minutes']
        self.sleepInterval.seconds  = json['Seconds']

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

            #self.Nodes.append(node)
            self.nodes.append(node)
        pass