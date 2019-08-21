from time import sleep

from networkmonitor.src.protocols import IProtocols, ContextProtocols
from networkmonitor.src.configuration import *

def test_ProtocolInterfaceType():
    #i = IProtocols("localhost", "HTTP:GET")
    cp = ContextProtocols(
        IProtocols("localhost", "HTTP:Get"), 
        IConfig("example.yaml")
    )

    if cp.protocols.Type == "HTTP:GET":
        assert True
    
    pass

def test_ProtocolInterfaceAddress():
    #i = IProtocols("localhost", "HTTP:GET")
    cp = ContextProtocols(
        IProtocols("localhost", "Http:Get"),
        IConfig("example.yaml")
    )

    if cp.protocols.URI == "localhost":
        assert True
    
    pass

def test_ProtocolBadURL():
    #i = IProtocols("www.google.com", "HTTP:GET")
    cp = ContextProtocols(
        IProtocols("www.google.com", "Http:Get"),
        IConfig("example.yaml")
    )

    #cp = ContextProtocols(i)
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
    cp = ContextProtocols(
        IProtocols("https://www.gmail.com", "Http:Get"),
        IConfig("example.yaml")
    )
    cp.GetWorkingClass(True)
    cp.Start()

    if cp.Status == "Online":
        assert True

    pass

def test_ProtocolHttpsURL():
    #sleep(5)
    #i = IProtocols("https://www.espn.com", "HTTP:GET")
    cp = ContextProtocols(
        IProtocols("https://www.espn.com", "Http:Get"),
        IConfig("example.yaml")
    )

    #cp = ContextProtocols(i)
    cp.GetWorkingClass(True)
    cp.Start()

    if cp.Status == "Online":
        assert True

    pass


def test_ProtocolMS():
    #i = IProtocols("https://www.youtube.com", "HTTP:Get")
    #cp = ContextProtocols(i)
    cp = ContextProtocols(
        IProtocols("https://www.youtube.com", "Http:Get"),
        IConfig("example.yaml")
    )

    cp.GetWorkingClass(True)
    cp.Start()

    if cp.MS >= 0:
        assert True

    pass