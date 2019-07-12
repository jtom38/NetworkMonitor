import curses
from networkmonitor import CursesHelper

class uiHelp():

    def __init__(self):
        pass

    def Start(self):
        ch = CursesHelper()
        ch.WindowNew()
        self.__RenderWindow(ch.stdscr)
        #curses.wrapper(self.__RenderWindow)
        pass

    def __RenderWindow(self, stdscr):
        ch = CursesHelper()
        ch.stdscr = stdscr

        # clear the scree and refresh
        ch.WindowClear()
        ch.WindowRefresh()

        # Start colors in curses
        curses.start_color()
        curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

        while ch.key != curses.KEY_F12:
            ch.WindowClear()
            ch.CursorMove()

            self.__InsertTitle(stdscr)
            self.__InsertFooter(stdscr, ch)
            ch.WindowRefresh()
            ch.GetCharacter()

        ch.WindowClose()

        pass
 
    def __InsertTitle(self, stdscr):
        title = "Network Monitor"
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(0, 0, title, curses.color_pair(1))
        stdscr.attroff(curses.color_pair(3))
        pass

    def __InsertFooter(self, stdscr, ch: CursesHelper):
        statusbarstr    = "|F12|Quit"
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(ch.height-1, 0, statusbarstr)
        stdscr.addstr(ch.height-1, len(statusbarstr), " " * (ch.width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))
        pass

