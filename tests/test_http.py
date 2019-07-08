
import pytest

from networkmonitor.http import Http

def test_HttpGetWww():
    h   = Http()
    url = "http://www.google.com"
    res = h.TestHttpGet(url)
    if res == "Online":
        assert True
    else:
        assert False
