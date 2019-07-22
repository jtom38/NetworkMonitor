
import pytest

from networkmonitor.http import Http

def test_GetHttpWww():
    h   = Http()
    url = "http://www.google.com"
    res = h.Get(url)
    if res == True:
        assert True
    else:
        assert False

def test_PostHttpWww():
    pass
