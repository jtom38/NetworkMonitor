
import os.path

from networkmonitor.src.collections import LogsCol
from networkmonitor.src.logs import ContextLogs, ILogs

def test_LogCollection():
    cl = ContextLogs(ILogs('sqlite', 'demo.sqlite'))
    l = LogsCol(level="debug", message="debug", name="Google", address="google.com", protocol="icmp")
    cl.AddLog(l)

    cl.CloseConnection()
    #os.remove('demo.sqlite')
   
    assert False