
import os
import time
import json

from networkmonitor.src import Nodes
from networkmonitor.src import InvalidNodeConfiguration
#from networkmonitor.src import YamlConfig

class OldConfig:
    """
    About:
    Config class will handle the read/write to configuration files.
    Will load '.yaml' or '.json' types.
    """

    def __init__(self, PathConfig:str):
        self.PathConfig = PathConfig
        self.nodes = []

        try:
            if PathConfig.endswith('yaml'):
                self.PathConfig = PathConfig
                #y = YamlConfig()
                # send to yaml processor


            if PathConfig.endswith('json'):
                # Send to json processor
                self.PathConfig = PathConfig
                self.__JsonUpdateConfig()

        except InvalidNodeConfiguration:
            print(f"Expected a configuration file type of '.yaml' or '.json'")

        pass

    def UpdateConfig(self):
        while True:
            if os.path.exists(self.PathConfig) == True:
                # found the file
                try:
                    cfg = Config(self.PathConfig)
                    if cfg.nodes != "":
                        return cfg
                except Exception:
                    print("Trying again in 30 seconds.")
                    time.sleep(30)
            else:
                print("No config.json was found.  Exiting...")
                exit()

    def __JsonUpdateConfig(self):
        try:
            with open(self.PathConfig) as jsonFile:
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

