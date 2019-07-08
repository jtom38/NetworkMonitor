
import os
import time
import json

class Config:
    """
    About:
    Config class will handle the read/write to configuration files.
    """

    def __init__(self, JsonConfig:str):
        try:
            with open(JsonConfig) as jsonFile:
                res = json.load(jsonFile)
                
                self.SleepTimer:int = res['SleepInterval']
                self.Nodes = res['Nodes'] 
        except Exception:
            print(f'Failed to load {JsonConfig}')
        
        pass

    def UpdateConfig(self):
        while True:
            if os.path.exists('config.json') == True:
                # found the file
                try:
                    cfg = Config('config.json')
                    if cfg.Nodes != "":
                        return cfg
                except Exception:
                    print("Trying again in 30 seconds.")
                    time.sleep(30)
            else:
                print("No config.json was found.  Exiting...")
                exit()
   
    def __ParseInterval(self, json:str):
        """
        About:
        This checks the json that was sent to see if we can get the sleep timer value
        """
        self.SleepTimer:int = json['SleepInterval'] 
        pass

    def __ParseNodes(self, json:str):
        for d in json['Nodes']:
            print(d['Name'])
        pass

#if __name__ == "__main__":
    #Config
    #pass