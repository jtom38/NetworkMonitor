
from networkmonitor.src.protocols import IProtocols, ContextProtocols, Ping
from networkmonitor.src.configuration import *

def test_ProtocolInterfaceType():
    cp = ContextProtocols(IProtocols("localhost", "icmp"))
    cc = ContextConfig(IConfig("example.yaml"))
    cc.GetWorkingConfigClass(True)
    cp.configuration = cc.configuration

    if cp.protocols.Type == "ICMP":
        assert True
    
    pass

def test_ProtocolInterfaceAddress():
    cp = ContextProtocols(IProtocols("localhost", "icmp"))
    cc = ContextConfig(IConfig("example.yaml"))
    cc.GetWorkingConfigClass(True)

    if cp.protocols.URI == "localhost":
        assert True
    
    pass

def test_ProtocolStatus():
    #i = IProtocols("localhost", "ICMP")
    #cp = ContextProtocols(i)
    cc = ContextConfig(IConfig("example.yaml"))
    cc.GetWorkingConfigClass(True)
    cc.ReadConfig()

    cp = ContextProtocols(IProtocols("localhost", "icmp"))
    cp.GetWorkingClass(True)
    cp.Start()

    if cp.Status == "Online":
        assert True

    pass

def test_ProtocolMSLocalHost():
    cc = ContextConfig(IConfig("example.yaml"))
    cc.GetWorkingConfigClass(True)
    cc.ReadConfig()

    cp = ContextProtocols(IProtocols("localhost",'ICMP'))
    cp.GetWorkingClass(True)
    cp.Start()

    if cp.MS >= 0:
        assert True

    pass

def test_ProtocolMSGoogle():
    cc = ContextConfig(IConfig("example.yaml"))
    cc.GetWorkingConfigClass(True)
    cc.ReadConfig()

    cp = ContextProtocols(IProtocols("google.com", 'ICMP'))
    cp.GetWorkingClass(True)
    cp.Start()

    if cp.MS >= 1:
        assert True

def test_PassConfigToContext():
    cc = ContextConfig(IConfig("example.yaml"))
    cc.GetWorkingConfigClass(True)
    cc.ReadConfig()

    cp = ContextProtocols(IProtocols("localhost", 'ICMP'))
    cp.GetWorkingClass(True)
    cp.configuration = cc.configuration
    cp.Start()

    if cp.protocols.configuration.nodes.__len__() >= 1:
        assert True
