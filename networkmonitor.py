
import platform
import os
import subprocess
import time
#import click

from networkmonitor import Ping, Config, TerminalOutput, Http

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
            # Get the name of the column stored,
            name = output.AdjustColumn(node['Name'], 20)
            
            if node['Protocol'] == "ICMP":               
                p = Ping()
                status = p.ProcessICMP(node["Address"])
                protocol = output.AdjustColumn("ICMP", 10)

            elif node['Protocol'] == "HTTP":
                h = Http()
                status = h.ProcessHTTP(node['Address'])
                protocol = output.AdjustColumn("HTTP", 10)
            else:
                pass
            status = output.AdjustColumn(status, 10)    
            
            output.AddRow(f"{name}{status}{protocol}")        

        output.InsertFooter()
        output.StartSleep(cfg.SleepTimer)

init()