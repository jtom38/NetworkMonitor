
import curses
from networkmonitor import CursesHelper, TerminalOutput

class uiLogs():

    def __init__(self):
        pass

    def Start(self):
        ch = CursesHelper()
        ch.WindowNew()
        #curses.wrapper(self.__RenderWindow)
        self.__RenderWindow(ch.stdscr)

    def __RenderWindow(self, stdscr):
        ch = CursesHelper()
        ch.stdscr = stdscr

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