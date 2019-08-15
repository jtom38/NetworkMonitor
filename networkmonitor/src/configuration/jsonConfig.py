
import os
import time
import json

from networkmonitor.src.configuration import IConfig
from networkmonitor.src.collections import Nodes, SleepInterval
from networkmonitor.src.exceptions import FailedToGenerateNewFile

class JsonConfig(IConfig):
    def __init__(self, config:IConfig):
        self.config:IConfig         = config
        self.sleepInterval:SleepInterval    = SleepInterval()
        self.nodes                  = []
        pass

    def NewConfig(self, defaultConfig):
        if os.path.exists(self.config.argPathConfig) == True:
            raise FailedToGenerateNewFile(f"Attempted to generate a new file at {self.config.argPathConfig} because a file was already present.  Pick a different file name or remove the existing file.")

        with open('example.json', mode='r') as default:
            j = json.load(default)

        with open(self.config.argPathConfig, mode='w') as jsonFile:
            json.dump(j, jsonFile)
        
        pass

    def ReadConfig(self):
        p = os.path.abspath(self.config.argPathConfig)
        if os.path.exists(p) == True:
            # found the file
            self.__JsonUpdateConfig()
        else:
            print(f"{self.config.argPathConfig} was not found.  Exiting...")
            exit()

    def __JsonUpdateConfig(self)->None:
        try:
            with open(self.config.argPathConfig) as jsonFile:
                res = json.load(jsonFile)
                
                #self.config.SleepInterval. = res['SleepInterval']
                self.__ParseSleepInterval(res['SleepInterval'])
                self.__JsonParseNodes(res)
                #self.Nodes = res['Nodes'] 
        except Exception:
            print(f'Failed to load {self.config.argPathConfig}')

    def __ParseSleepInterval(self, json:str)->None:
        self.sleepInterval.hours    = int(json['Hours'])
        self.sleepInterval.minutes  = int(json['Minutes'])
        self.sleepInterval.seconds  = int(json['Seconds'])

    def __JsonParseNodes(self, json:str)->None:
        for d in json['Nodes']:
            try:
                node = Nodes(d['Name'], d['Address'], d['Protocol'])
            except:
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

            self.nodes.append(node)
        pass

    