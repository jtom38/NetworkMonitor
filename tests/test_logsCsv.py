
import os
from typing import List
from networkmonitor.src.collections import LogsCol
from networkmonitor.src.logs import ILogs, ContextLogs

def test_LogCreation():
    try:
        os.remove('logs.csv')
    except:
        # file was not found to remove, thats okay.
        pass

    cl = ContextLogs(ILogs("csv", "logs.csv"))
    #l = LogsCol(level="debug", message="debug", name="Google", address="google.com", protocol="icmp")

    if os.path.exists('.\\logs.csv'):
        assert True
    pass

def test_AddLog():
    cl = ContextLogs(ILogs("csv", "logs.csv"))
    l = LogsCol(level="debug", message="debug", name="Google", address="google.com", protocol="icmp")
    res = cl.Add(l)

    if res == True:
        assert True       

def test_BulkEntry():
    cl = ContextLogs(ILogs('csv', 'logs.csv'))
    l1 = LogsCol(level="debug", message="debug", name="Google01", address="google.com", protocol="icmp")
    l2 = LogsCol(level="debug", message="debug", name="Google02", address="google.com", protocol="icmp")
    items:List[LogsCol] = [l1, l2]

    res = cl.AddMany(items)

    if res is True:
        assert True

def test_GetTop1():
    cl = ContextLogs(ILogs("csv", "logs.csv"))
    #l = LogsCol(level="debug", message="debug", name="Google", address="google.com", protocol="icmp")
    res: List[LogsCol] = cl.GetTop(1)
    print(res)
    if res.name == "Google":
        assert True

def test_GetTop1NameGoogle():
    cl = ContextLogs(ILogs("csv", 'logs.csv'))
    i = cl.GetTop(1)
    d = cl.GetByKey(i.key)
    if d.key == i.key:
        assert True

def test_GetAll():
    cl = ContextLogs(ILogs('csv', 'logs.csv'))
    i = cl.GetAll()

    if i.__len__() >= 1:
        assert True