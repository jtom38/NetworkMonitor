
from networkmonitor.src.configuration import IConfig, YamlConfig, ContextConfig

def test_YamlReturnsData():
    i = IConfig("example.yaml")
    cc = ContextConfig(i)
    cc.ReadConfig()

    if cc.Nodes.__len__() >= 1:
        assert True
    pass

def test_YamlContainsSleepInterval():
    i = IConfig("example.yaml")
    c = ContextConfig(i)
    c.ReadConfig()

    if c.SleepInterval >= 0:
        assert True

def test_YamlNodesContainNames():
    # Each node needs to contain a Name:
    i = IConfig("example.yaml")
    c = ContextConfig(i)
    c.ReadConfig()

    for item in c.Nodes:
        if item.name == None:
            # Object is missing Name:
            assert False
        pass
    
    assert True

def test_YamlNodesContainAddress():
    # Each node needs to contain a Name:
    i = IConfig("example.yaml")
    c = ContextConfig(i)
    c.ReadConfig()

    for item in c.Nodes:
        if item.address == None:
            # Object is missing Name:
            assert False
        pass
    
    assert True

def test_YamlNodesContainProtocol():
    # Each node needs to contain a Name:
    i = IConfig("example.yaml")
    c = ContextConfig(i)
    c.ReadConfig()

    for item in c.Nodes:
        if item.protocol == None:
            # Object is missing Name:
            assert False
        pass
    
    assert True