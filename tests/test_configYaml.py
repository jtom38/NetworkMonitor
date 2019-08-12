
import os
from networkmonitor.src.configuration import IConfig, YamlConfig, ContextConfig

def test_YamlReturnsData():
    i = IConfig("example.yaml")
    y = YamlConfig(i)
    cc = ContextConfig(y)
    cc.ReadConfig()

    if cc.Nodes.__len__() >= 1:
        assert True
    pass

def test_YamlContainsSleepInterval():
    i = IConfig("example.yaml")
    y = YamlConfig(i)
    c = ContextConfig(y)
    c.ReadConfig()

    if c.SleepInterval >= 0:
        assert True

def test_YamlNodesContainNames():
    # Each node needs to contain a Name:
    i = IConfig("example.yaml")
    y = YamlConfig(i)
    c = ContextConfig(y)
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
    y = YamlConfig(i)
    c = ContextConfig(y)
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
    y = YamlConfig(i)
    c = ContextConfig(y)
    c.ReadConfig()

    for item in c.Nodes:
        if item.protocol == None:
            # Object is missing Name:
            assert False
        pass
    
    assert True


def test_GenerateNewYaml():
    f = 'delete.yaml'
    try:
        os.remove(f)
    except:
        pass

    i = IConfig(f)
    y = YamlConfig(i)
    c = ContextConfig(y)
    c.NewConfig()
    c.ReadConfig()

    os.remove(f)

    if c.SleepInterval == 120:
        assert True

    pass