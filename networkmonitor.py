
from networkmonitor.tui import uiMain

def init():
    """
    Init is the applications start point.  From here we will call in what we need.

    """
    main = uiMain()
    main.Start()

init()