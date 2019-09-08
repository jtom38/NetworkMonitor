
import os

from networkmonitor.src.configuration import *
from networkmonitor.src import CLI

def test_NewYamlConfig():
    """
    CLI will generate the new YamlConfig.
    Once the file is made we will import it back into memory and check for values we expect.
    """
    i = IConfig("delete.yaml", True)
    c = CLI(i)
    c.NewConfig()
    if os.path.exists('delete.yaml') == False:
        assert False

    y = YamlConfig(i)
    cc = ContextConfig(y)
    cc.ReadConfig()

    os.remove('delete.yaml')

    if cc.configuration.sleepInterval.minutes == 2:
        assert True