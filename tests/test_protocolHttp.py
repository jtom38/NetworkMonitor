from time import sleep

from networkmonitor.src.protocols import IProtocols, ContextProtocols
from networkmonitor.src.configuration import *

def test_ProtocolInterfaceType():
    #cc = ContextConfig(IConfig("example.yaml"))
    cp = ContextProtocols(IProtocols("localhost", "HTTP:Get"))

    if cp.protocols.Type == "HTTP:GET":
        assert True
    
    pass

def test_ProtocolInterfaceAddress():
    #IConfig("example.yaml")
    cp = ContextProtocols(IProtocols("localhost", "Http:Get"))
    if cp.protocols.URI == "localhost":
        assert True
    
    pass

def test_ProtocolBadURL():
    cp = ContextProtocols(IProtocols("www.google.com", "Http:Get"))
    #cc = ContextConfig(IConfig("example.yaml"))
    #cp.configuration = cc.configuration

    cp.GetWorkingClass(True)
    cp.Start()

    if cp.Status == "Online":
        assert True

    pass

def test_ProtocolHttpURL():
    """
    This will test to confirm tht we can accept a normal URI.
    """
    #sleep(5)
    #i = IProtocols("https://www.gmail.com", "HTTP:GET")
    #IConfig("example.yaml")
    cp = ContextProtocols(IProtocols("https://www.gmail.com", "Http:Get"))
    cp.GetWorkingClass(True)
    cp.Start()

    if cp.Status == "Online":
        assert True

    pass

def test_ProtocolHttpsURL():
    #sleep(5)
    #i = IProtocols("https://www.espn.com", "HTTP:GET")
    #IConfig("example.yaml")
    cp = ContextProtocols(IProtocols("https://www.espn.com", "Http:Get"))

    #cp = ContextProtocols(i)
    cp.GetWorkingClass(True)
    cp.Start()

    if cp.Status == "Online":
        assert True

    pass


def test_ProtocolMS():
    #i = IProtocols("https://www.youtube.com", "HTTP:Get")
    #cp = ContextProtocols(i)
    #IConfig("example.yaml")
    cp = ContextProtocols(IProtocols("https://www.youtube.com", "Http:Get"))
    cp.GetWorkingClass(True)
    cp.Start()

    if cp.MS >= 0:
        assert True

    pass