
import platform
import os
import subprocess
import time

from PyMonitor import Ping, Config, TerminalOutput

def init():
    """
    Init is the applications start point.  From here we will call in what we need.

    """

    # Check if we got our config file
    if os.path.exists('config.json') == True:
        # found the file
        cfg = Config('config.json')

    icmp = Ping()
    output = TerminalOutput()
    # Loop though all the nodes
    while True:
        
        # Insert a header
        hName = output.AdjustColumn("Name", 20)
        hStatus = output.AdjustColumn("Status", 10)
        hProtocol=output.AdjustColumn("Protocol",10)
        output.AddRow(f"{hName}{hStatus}{hProtocol}")

        for node in cfg.Nodes:
            name = output.AdjustColumn(node['Name'], 20)

            if node['Protocol'] == "ICMP":
                res = icmp.PingHost(node['Address'])                        
                if res == 0:
                    status:str = "Online"
                else:
                    status:str = "Offline"

            status = output.AdjustColumn(status, 10)
            protocol = output.AdjustColumn("ICMP", 10)
            output.AddRow(f"{name}{status}{protocol}")
        
        output.StartSleep(cfg.SleepTimer)


def MainLoop():
    pass

init()