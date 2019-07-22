
import os
import time
import json

from networkmonitor.src import Nodes

class Config:
    """
    About:
    Config class will handle the read/write to configuration files.
    """

    def __init__(self, JsonConfig:str):
        self.jsonConfig = JsonConfig
        self.nodes = []
        try:
            with open(JsonConfig) as jsonFile:
                res = json.load(jsonFile)
                
                self.SleepTimer:int = res['SleepInterval']
                self.__ParseNodes(res)
                #self.Nodes = res['Nodes'] 
        except Exception:
            print(f'Failed to load {self.jsonConfig}')
        
        pass

    def UpdateConfig(self):
        while True:
            if os.path.exists(self.jsonConfig) == True:
                # found the file
                try:
                    cfg = Config(self.jsonConfig)
                    if cfg.nodes != "":
                        return cfg
                except Exception:
                    print("Trying again in 30 seconds.")
                    time.sleep(30)
            else:
                print("No config.json was found.  Exiting...")
                exit()

    def __ParseNodes(self, json:str):
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
