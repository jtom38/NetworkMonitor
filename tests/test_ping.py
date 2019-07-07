
import pytest
#import sys, os
#sys.path.append("../networkmonitor/")

from networkmonitor.ping import Ping

def TestProcessICMP():
    p = Ping()
    res = p.ProcessICMP("http://www.google.com")
    if res == "Online":
        assert True
    else:
        assert False
