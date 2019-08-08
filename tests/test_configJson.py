
from networkmonitor.src.configuration import *

def test_JsonRead():
    # Add info into interface
    i = IConfig("/tests/test.json")

    # Generate our context that will handle the work
    c = ConfigContext(i)
    c.ReadConfig()        

    pass