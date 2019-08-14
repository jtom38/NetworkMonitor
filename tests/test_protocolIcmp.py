
from networkmonitor.src.protocols import IProtocols, ContextProtocols, Ping

def test_ProtocolInterfaceType():
    i = IProtocols("localhost", "ICMP")
    cp = ContextProtocols(i)

    if cp.protocols.Type == "ICMP":
        assert True
    
    pass

def test_ProtocolInterfaceAddress():
    i = IProtocols("localhost", "ICMP")
    cp = ContextProtocols(i)

    if cp.protocols.URI == "localhost":
        assert True
    
    pass

def test_ProtocolStatus():
    i = IProtocols("localhost", "ICMP")
    cp = ContextProtocols(i)
    cp.GetWorkingClass(True)
    cp.Start()

    if cp.Status == "Online":
        assert True

    pass

def test_ProtocolMS():
    i = IProtocols("localhost", "ICMP")
    cp = ContextProtocols(i)
    cp.GetWorkingClass(True)
    cp.Start()

    if cp.MS >= 0:
        assert True

    pass