
import os
import time
import json

from networkmonitor.src.configuration import IConfig
from networkmonitor.src.collections import Nodes

class JsonConfig:
    def __init__(self, config:IConfig):
        self.config = config
        pass

    def NewConfig(self):
        pass

    def ReadConfig(self):
        p = os.path.abspath(self.config.PathConfig)
        if os.path.exists(p) == True:
            # found the file
            self.__JsonUpdateConfig()
            try:
                #cfg = Config(self.PathConfig)
                #if cfg.nodes != "":
                    #return cfg
                pass
            except Exception:
                print("Trying again in 30 seconds.")
                time.sleep(30)
        else:
            print(f"{self.config.PathConfig} was not found.  Exiting...")
            exit()

    def __JsonUpdateConfig(self):
        try:
            with open(self.config.PathConfig) as jsonFile:
                res = json.load(jsonFile)
                
                self.SleepTimer:int = res['SleepInterval']
                self.__JsonParseNodes(res)
                #self.Nodes = res['Nodes'] 
        except Exception:
            print(f'Failed to load {self.PathConfig}')

    def __JsonParseNodes(self, json:str):
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

    