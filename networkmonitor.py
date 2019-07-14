
import platform
import os
import subprocess
import time
#import colorama
#import click

from networkmonitor import Ping, Config, TerminalOutput, Http
from networkmonitor import (
    NetworkMonitorException, 
    InvalidProtocol,
    InvalidNodeConfiguration
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

        for node in cfg.nodes:
            # Generate friendly vars
            try:
                nodeName:str        = node.name
                nodeAddress:str     = node.address
                nodeProtocol:str    = node.protocol
            except:
                raise InvalidNodeConfiguration(f"A node is missing one of the required properties. "
                    "Please make sure all nodes have the following. "
                    "Name, Address and Protocol")
            nodeCategory            = node.category

            np = nodeProtocol.lower()
            if np == "icmp":               
                p = Ping()
                status = p.ProcessICMP(nodeAddress)
                protocol = output.AdjustColumn("ICMP", 10)
            elif np == "http:get":
                h = Http()
                status = h.TestHttpGet(nodeAddress, 80)
                protocol = output.AdjustColumn("HTTP:GET", 10)
            elif np == "http:post":
                h = Http()
                status = h.Post(nodeAddress)
                protocol = output.AdjustColumn("HTTP:POST", 10)
            else:
                raise InvalidProtocol(f"{nodeProtocol} is invalid. Use ICMP, HTTP:Get, HTTP:POST.")
                
            name        = output.AdjustColumn(nodeName, 20)
            status      = output.AdjustColumn(status, 10)
            category    = output.AdjustColumn(nodeCategory, 20)
            
            output.AddRow(f"{name}{status}{protocol}{category}")
            
            # Check to see if we have nodes under this level


        output.InsertFooter()
        output.StartSleep(cfg.SleepTimer)

init()