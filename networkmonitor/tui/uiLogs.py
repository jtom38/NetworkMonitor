
import curses
import typing
from networkmonitor import CursesHelper
from networkmonitor.src import LogsCol

class uiLogs():
    logs = []

    def __init__(self):
        #self.logs = []
        pass

    def Start(self) -> None:
        ch = CursesHelper()
        ch.WindowNew()
        #curses.wrapper(self.__RenderWindow)
        self.__RenderWindow(ch.stdscr)

    def __RenderWindow(self, stdscr):
        ch = CursesHelper()
        ch.stdscr = stdscr
        ch.SetCharacterBlockingMode(False)

        ch.WindowClear()
        ch.WindowRefresh()

        curses.start_color()
        curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
        while ch.key != curses.KEY_F12:
            ch.WindowClear()
            ch.CursorMove() 

            self.__InsertHeader(stdscr)
            self.__InsertColHeader(stdscr, ch.width)
            self.__InsertLines(stdscr, ch.height, ch.width)
            self.__InsertFooter(stdscr, ch)

            ch.WindowRefresh()
            ch.GetCharacter()

        ch.WindowClose()
    
    def __InsertHeader(self, stdscr):
        title = "NetworkMonitor - Logs"
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(0, 0, title, curses.color_pair(1))
        stdscr.attroff(curses.color_pair(3))
        pass

    def __InsertColHeader(self, stdscr, width):
        o = CursesHelper()
        col = 4
        #level   = o.AdjustColumn("Level", 6)
        dt      = o.AdjustColumn("DateTime", 19)
        name    = o.AdjustColumn('Name', 10)
        address = o.AdjustColumn('Address', 16)
        msg     = o.AdjustColumn('Message', width-6-10-16)

        line = f'{dt} {name}{address}{msg}'
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(1, 0, line)
        stdscr.attroff(curses.color_pair(3))
        pass

    def __InsertLines(self, stdscr, height:int, width:int):
        o = CursesHelper()
        x = 2        
        col = 4

        for line in self.logs:
            if x <= height:
                #level   = o.AdjustColumn(line.level, 6)
                name    = o.AdjustColumn(line.name, 10)
                address = o.AdjustColumn(line.address, 16)
                msg     = o.AdjustColumn(line.message, width-6-10-16)
                dt      = o.AdjustColumn(str(line.time), 19)
                line = f"{dt} {name}{address}{msg}"

                #stdscr.attron(curses.color_pair(3))
                stdscr.addstr(x, 0, line)
                #stdscr.attroff(curses.color_pair(3))
                x = x+1
            


    def __InsertFooter(self, stdscr, ch: CursesHelper):
        statusbarstr    = "|F12|Close"
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(ch.height-1, 0, statusbarstr)
        stdscr.addstr(ch.height-1, len(statusbarstr), " " * (ch.width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))
        pass


if __name__ == "__main__":
    l = uiLogs()
    l.Start()
    pass