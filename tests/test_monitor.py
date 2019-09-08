
from networkmonitor import Monitor
from networkmonitor.src.configuration import *

def test_CallMonitor():
    m = Monitor(IConfig("example.yaml"))
    if m.__configuration__.nodes.__len__() == 4:
        assert True

def test_ReportLen():
    m = Monitor(IConfig("example.yaml"))
    m.Start()

    if m.report.__len__() == 4:
        assert True

def test_ReportIcmpStatus():
    m = Monitor(IConfig("example.yaml"))
    m.Start()

    item = m.report[0]

    if item.status == "Online":
        assert True

def test_ReportIcmpMS():
    m = Monitor(IConfig("example.yaml"))
    m.Start()

    item = m.report[0]

    if item.ms == 0:
        assert True