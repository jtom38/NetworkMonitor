
import datetime
from networkmonitor.src.configuration import *
from networkmonitor.src import RefreshTimer

def test_HourNoRemainder():
    i = IConfig("example.yaml")
    r = RefreshTimer(i)
    now = datetime.datetime.now()
    now = now.replace(hour=1)
    res = r.GetHour(now, 2)

    if res[0] == 3:
        assert True

def test_HourRemainder():
    r = RefreshTimer(IConfig("example.yaml"))
    now = datetime.datetime.now()
    now = now.replace(hour=23)
    res = r.GetHour(now, 2)

    if res[0] == 1 and res[1] == 1:
        assert True

def test_MinuteNoRemainder():
    r = RefreshTimer(IConfig("example.yaml"))
    now = datetime.datetime.now()
    now = now.replace(minute=1)
    res = r.GetMin(now, 2)

    if res[0] == 3:
        assert True

def test_MinuteRemainder():
    r = RefreshTimer(IConfig("example.yaml"))
    now = datetime.datetime.now()
    now = now.replace(minute=23)
    res = r.GetMin(now, 2)

    if res[0] == 1 and res[1] == 1:
        assert True

def test_SecondNoRemainder():
    r = RefreshTimer(IConfig("example.yaml"))
    now = datetime.datetime.now()
    now = now.replace(second=1)
    res = r.GetSec(now, 2)

    if res[0] == 3:
        assert True

def test_SecondRemainder():
    r = RefreshTimer(IConfig("example.yaml"))
    now = datetime.datetime.now()
    now = now.replace(second=23)
    res = r.GetSec(now, 2)

    if res[0] == 1 and res[1] == 1:
        assert True


def test_GetNextRefresh():
    r = RefreshTimer(IConfig("example.yaml"))
    c = f"{r.NextRefresh.hour}:{r.NextRefresh.minute}"
    res = r.GetNextRefresh()

    if res == c:
        assert True

def test_SetNextRefreshRollOverMin():
    # Set it so we roll it over at the exact min 
    # hour +1
    # mins 00
    r = RefreshTimer(IConfig("example.yaml"))
    r.LastRefresh = r.LastRefresh.replace(hour=12,minute=58)

    r.SetNextRefresh()
    n = r.NextRefresh
    if r.NextRefresh.hour == 13 and r.NextRefresh.minute == 00:
        assert True


def test_SetNextRefreshRollOverMin02():
    # This test checks if mins where to be 61 rather then 60

    r = RefreshTimer(IConfig("example.yaml"))
    r.LastRefresh = r.LastRefresh.replace(hour=12, minute=59)
    r.SetNextRefresh()
    if r.NextRefresh.hour == 13 and r.NextRefresh.minute == 1:
        assert True

def test_CheckRefreshTimer():
    r = RefreshTimer(IConfig("example.yaml"))
    res = r.CheckRefreshTimer()

    if res == True:
        assert True
        
def test_CheckRefreshTimer01():
    # Checking for False as the timer has not lapsed yet
    r = RefreshTimer(IConfig("example.yaml"))
    r.LastRefresh = r.LastRefresh.replace(minute=r.LastRefresh.minute-1)
    res = r.CheckRefreshTimer()

    if res == False:
        assert True

def test_CheckRefreshTwice():
    r = RefreshTimer(IConfig("example.yaml"))
    res = r.CheckRefreshTimer()
    res = r.CheckRefreshTimer()

    # should return false as its not time to refresh yet
    if res == False:
        assert True

