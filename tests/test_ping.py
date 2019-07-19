
import pytest
#import sys, os
#sys.path.append("../networkmonitor/")

from networkmonitor.ping import Ping

def test_ProcessIcmpHttp():
    """
    Tests ProcessIcmp() with a http://www address   
    """
    p = Ping()
    p.PingHost("http://www.google.com")
    if p.Status == "Online":
        assert True
    else:
        assert False

def test_ProcessIcmpWww():
    """
    Tests ProcessIcmp() with a www address
    """
    p = Ping()
    p.PingHost("www.google.com")
    if p.Status == "Online":
        assert True
    else:
        assert False

def test_PingHostLocalHostMS():
    """
    Tests PingHost to Localhost address
    """
    p = Ping()
    p.PingHost("localhost")
    if p.ms == 0:
        assert True
    else:
        assert False
    pass        

def test_PingHostHttp():
    """
    Tests PingHost with a http://www address
    """
    p = Ping()
    p.PingHost("http://www.google.com")
    if p.ms != -1:
        assert True
    else:
        assert False
    pass
