
import pytest
#import sys, os
#sys.path.append("../networkmonitor/")

from networkmonitor.ping import Ping

def test_ProcessIcmpHttp():
    """
    Tests ProcessIcmp() with a http://www address   
    """
    p = Ping()
    res = p.ProcessICMP("http://www.google.com")
    if res == "Offline":
        assert True
    else:
        assert False

def test_ProcessIcmpWww():
    """
    Tests ProcessIcmp() with a www address
    """
    p = Ping()
    res = p.ProcessICMP("www.google.com")
    if res == "Online":
        assert True
    else:
        assert False

def test_PingHostLocalHost():
    """
    Tests PingHost to Localhost address
    """
    p = Ping()
    res = p.PingHost("localhost")
    if res == 0:
        assert True
    else:
        assert False
    pass        

def test_PingHostHttp():
    """
    Tests PingHost with a http://www address
    """
    p = Ping()
    res = p.PingHost("http://www.google.com")
    if res != 0:
        assert True
    else:
        assert False
    pass
