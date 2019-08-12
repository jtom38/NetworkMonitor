
from networkmonitor.src.protocols import IProtocols, ContextProtocols

def test_ProtocolInterfaceType():
    i = IProtocols("localhost", "HTTP:GET")
    cp = ContextProtocols(i)

    if cp.protocols.Type == "HTTP:GET":
        assert True
    
    pass

def test_ProtocolInterfaceAddress():
    i = IProtocols("localhost", "HTTP:GET")
    cp = ContextProtocols(i)

    if cp.protocols.URI == "localhost":
        assert True
    
    pass

def test_ProtocolBadURL():
    i = IProtocols("www.google.com", "HTTP:GET")
    cp = ContextProtocols(i)
    cp.Start()

    if cp.Status == "Online":
        assert True

    pass

def test_ProtocolHttpURL():
    """
    This will test to confirm tht we can accept a normal URI.
    """
    i = IProtocols("http://www.google.com", "HTTP:GET")
    cp = ContextProtocols(i)
    cp.Start()

    if cp.Status == "Online":
        assert True

    pass

def test_ProtocolHttpsURL():
    i = IProtocols("https://www.google.com", "HTTP:GET")
    cp = ContextProtocols(i)
    cp.Start()

    if cp.Status == "Online":
        assert True

    pass


def test_ProtocolMS():
    i = IProtocols("https://www.youtube.com", "HTTP:Get")
    cp = ContextProtocols(i)
    cp.Start()

    if cp.MS >= 0:
        assert True

    pass