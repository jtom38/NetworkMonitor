
import os
from networkmonitor.src.configuration import IConfig, JsonConfig, ContextConfig
from networkmonitor.src.collections import Nodes

def test_JsonRead():
    # Add info into interface
    i = IConfig("example.json")
    j = JsonConfig(i)

    # Generate our context that will handle the work
    c = ContextConfig(j)
    c.ReadConfig()

    if c.configuration.nodes.__len__() >= 1:
        assert True
    pass

def test_JsonContainsSleepInterval():
    i = IConfig("example.json")
    j = JsonConfig(i)
    c = ContextConfig(j)
    c.ReadConfig()

    if c.configuration.sleepInterval.minutes >= 2:
        assert True

def test_JsonNodesContainNames():
    # Each node needs to contain a Name:
    i = IConfig("example.json")
    j = JsonConfig(i)
    c = ContextConfig(j)
    c.ReadConfig()

    for item in c.configuration.nodes:
        if item.name == None:
            # Object is missing Name:
            assert False
        pass
    
    assert True

def test_JsonNodesContainAddress():
    # Each node needs to contain a Name:
    i = IConfig("example.json")
    j = JsonConfig(i)
    c = ContextConfig(j)
    c.ReadConfig()

    for item in c.configuration.nodes:
        if item.address == None:
            # Object is missing Name:
            assert False
        pass
    
    assert True

def test_JsonNodesContainProtocol():
    # Each node needs to contain a Name:
    i = IConfig("example.json")
    j = JsonConfig(i)
    c = ContextConfig(j)
    c.ReadConfig()

    for item in c.configuration.nodes:
        if item.protocol == None:
            # Object is missing Name:
            assert False
        pass
    
    assert True

def test_LoadConfigTwice():
    c = ContextConfig(IConfig('example.json'))
    c.GetWorkingConfigClass(True)
    c.ReadConfig()
    c.ReadConfig()

    if c.configuration.nodes.__len__() == 4:
        assert True

def test_NewConfig():

    j = JsonConfig(IConfig("delete.json"))
    c = ContextConfig(j)
    c.NewConfig()
    c.ReadConfig()

    os.remove("delete.json")

    if c.configuration.sleepInterval.minutes == 2:
        assert True
    
    pass


def test_FindValidClassToInject():
    c = ContextConfig(IConfig("example.json"))
    c.GetWorkingConfigClass(True)
    c.ReadConfig()

    if c.configuration.sleepInterval.minutes == 2:
        assert True
    
    pass

def test_ProtocolsIcmpTimeout():
    c = ContextConfig(IConfig("example.json"))
    c.GetWorkingConfigClass(True)
    c.ReadConfig()
    
    if c.configuration.protocols.icmp.timeout == 0:
        assert True

def test_ProtocolsIcmpTimeoutNewConfig():
    f = 'delete.json'

    try:
        os.remove(f)
    except:
        pass

    c = ContextConfig(IConfig(f))
    c.GetWorkingConfigClass(True)
    c.NewConfig()
    c.ReadConfig()

    os.remove(f)

    if c.configuration.protocols.icmp.timeout == 0:
        assert True

def test_LoggingType():
    c = ContextConfig(IConfig("example.json"))
    c.GetWorkingConfigClass(True)
    c.ReadConfig()

    if c.configuration.logging.type == 'csv':
        assert True

def test_LoggingFileName():
    c = ContextConfig(IConfig("example.json"))
    c.GetWorkingConfigClass(True)
    c.ReadConfig()

    if c.configuration.logging.filename == 'log.csv':
        assert True

def test_LoggingTypeNewConfig():
    f = 'delete.json'
    try:
        os.remove(f)
    except:
        pass

    c = ContextConfig(IConfig(f))
    c.GetWorkingConfigClass(True)
    c.NewConfig()
    c.ReadConfig()

    os.remove(f)
    if c.configuration.logging.type == "csv":
        assert True

def test_LoggingFilenameNewConfig():
    f = 'delete.json'
    try:
        os.remove(f)
    except:
        pass

    c = ContextConfig(IConfig(f))
    c.GetWorkingConfigClass(True)
    c.NewConfig()
    c.ReadConfig()

    os.remove(f)
    if c.configuration.logging.filename == 'log.csv':
        assert True

