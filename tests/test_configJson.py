
from networkmonitor.src.configuration import *
from networkmonitor.src.collections import Nodes

def test_JsonRead():
    # Add info into interface
    i = IConfig("test.json")

    # Generate our context that will handle the work
    c = ConfigContext(i)
    c.ReadConfig()

    if c.nodes.__len__() >= 1:
        assert True
    

    pass

def test_JsonContainsSleepInterval():
    i = IConfig("test.json")
    c = ConfigContext(i)
    c.ReadConfig()

    if c.SleepInterval >= 0:
        assert True

def test_JsonNodesContainNames():
    # Each node needs to contain a Name:
    i = IConfig("test.json")
    c = ConfigContext(i)
    c.ReadConfig()

    for item in c.nodes:
        if item.name == None:
            # Object is missing Name:
            assert False
        pass
    
    assert True

def test_JsonNodesContainAddress():
    # Each node needs to contain a Name:
    i = IConfig("test.json")
    c = ConfigContext(i)
    c.ReadConfig()

    for item in c.nodes:
        if item.address == None:
            # Object is missing Name:
            assert False
        pass
    
    assert True

def test_JsonNodesContainProtocol():
    # Each node needs to contain a Name:
    i = IConfig("test.json")
    c = ConfigContext(i)
    c.ReadConfig()

    for item in c.nodes:
        if item.protocol == None:
            # Object is missing Name:
            assert False
        pass
    
    assert True