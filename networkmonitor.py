
import platform
import os
import subprocess
import time
#import colorama
#import click

from networkmonitor import Ping, Config, TerminalOutput, Http
from networkmonitor import (
    NetworkMonitorException, 
    InvalidProtocol
    )

def init():
    """
    Init is the applications start point.  From here we will call in what we need.

    """
    config = Config("config.json")

    # Loop though all the nodes

    while True:

        # Generate the class that handles all the writing to the terminal
        output = TerminalOutput()
        # Check if we got our config file
        # We can refresh the the sources each time we call the file for live updates
        cfg = config.UpdateConfig() 

        # Insert a header
        output.InsertHeader()

        for node in cfg.Nodes:
            # Generate friendly vars
            nodeName:str    = node['Name']
            nodeAddress:str = node["Address"]
            nodeProtocol:str= node["Protocol"]

            # 
            if nodeProtocol.lower() == "icmp":               
                p = Ping()
                status = p.ProcessICMP(nodeAddress)
                protocol = output.AdjustColumn("ICMP", 10)

            elif nodeProtocol.lower().__contains__("http"):
                h = Http()
                if nodeProtocol.lower().__contains__("get"):
                    status = h.TestHttpGet(nodeAddress)

                protocol = output.AdjustColumn("HTTP", 10)
            else:
                raise InvalidProtocol(f"{nodeProtocol} is invalid. Use ICMP and HTTP:Get.")
                
            name = output.AdjustColumn(nodeName, 20)
            status = output.AdjustColumn(status, 10)    
            
            output.AddRow(f"{name}{status}{protocol}")
            
            # Check to see if we have nodes under this level


        output.InsertFooter()
        output.StartSleep(cfg.SleepTimer)

init()