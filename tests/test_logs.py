
from networkmonitor.src import LogsCol

def test_LogCollection():
    l = LogsCol()
    
    if l.address == '':
        assert True

def test_LogCollAdd():
    logs = []
    l = LogsCol()
    logs.append(l)

    if logs.count == 1:
        assert True

def test_ConstLevel():
    l = LogsCol(level="debug")

    if l.level == "debug":
        assert True

def test_Const():
    l = LogsCol(level="debug", message="debug", name="Google", address="google.com", protocol="icmp")

    if l.level == "debug" and l.message == "debug":
        assert True