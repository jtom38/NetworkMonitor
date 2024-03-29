
import curses
import threading
import datetime
from datetime import datetime
from networkmonitor import CursesHelper, TerminalOutput, LogsCol, Monitor, Helper

from uiLogs import uiLogs
from uiHelp import uiHelp

class uiMain():
    def __init__(self):
        self.logs = []
        self.monitor = Monitor("config.json")
        self.o = TerminalOutput()

        #self.tMonitor = threading.Thread(target=self.monitor.Start, daemon=True)
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

        #th = threading.Thread(target=self.monitor.Start, daemon=True)
        #th.start()

        self.monitor.Start(True)

        self.__GenLogData()

        # clear the scree and refresh
        ch.WindowClear()
        ch.WindowRefresh()

        # Start colors in curses
        curses.start_color()
        curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

        # Refresh the screen with new data every 5 seconds
        
        dtRefresh = datetime.now()

        # Checking to see if the last key that was entered was 'F12'
        while (ch.key != curses.KEY_F12):
            ch.WindowClear()
            #stdscr.clear()

            # Tells us the screens height and width      
            ch.CursorMove()

            if ch.key == curses.KEY_F2:
                self.monitor.Start(force=True)
                ch.WindowClear()
                ch.WindowRefresh()
                ch.key = 0
            elif ch.key == curses.KEY_F10:
                ch = self.__TuiHelp(stdscr)
            elif ch.key == curses.KEY_F9:                
                ch = self.__TuiLogs(stdscr)
            else:
                # Render title
                self.monitor.Start()
                self.__InsertTitle(stdscr)                
                self.__InsertColHeader(stdscr, ch)
                self.__InsertLine(stdscr, ch, 2)
                self.__InsertFooter(stdscr, ch)

                ch.CursorMove()
                # Update the screen
                ch.WindowRefresh()

                ch.GetCharacter()
                pass
        # Close key was pressed
        ch.WindowClose()           

    def __GenLogData(self):
        i = 0
        while i < 10:
            self.logs.insert(self.logs.__len__()+1 ,LogsCol(level='debug', message='Unable to reach service.', name='Google', address="www.google.com", protocol='ICMP') )
            i = i+1

    def __TuiHelp(self, stdscr):
        h = uiHelp()
        h.Start()

        ch = CursesHelper()
        ch.stdscr = stdscr
        ch.WindowClear()
        ch.WindowRefresh()
        ch.key = 0
        return ch

    def __TuiLogs(self, stdscr):
        l = uiLogs()
        l.logs = self.logs
        l.Start()        

        # Once we come back here, update ch with the current stdscr
        # Helps to make the window accept input again
        ch = CursesHelper()
        ch.stdscr = stdscr  
        ch.WindowClear()
        ch.WindowRefresh()
        ch.key = 0 
        return ch

    def __InsertTitle(self, stdscr):
        h = Helper()
        res = h.GetNextNodeRefreshTime(self.monitor.c.SleepTimer, self.monitor.LastRefresh)
        title           = f"NetworkMonitor - Refresh@{res}"
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(0, 0, title, curses.color_pair(1))
        stdscr.attroff(curses.color_pair(3))
        pass

    def __InsertFooter(self, stdscr, ch: CursesHelper):
        statusbarstr    = "|F2|Refresh |F9|Logs  |F10|Help  |F12|Quit"
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(ch.height-1, 0, statusbarstr)
        stdscr.addstr(ch.height-1, len(statusbarstr), " " * (ch.width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))
        pass

    def __InsertColHeader(self, stdscr, ch:CursesHelper):
        o = TerminalOutput()
        hName           = o.AdjustColumn("Name", ch.width/3)
        hStatus         = o.AdjustColumn("Status", ch.width/3)
        hProtocol       = o.AdjustColumn("Protocol", ch.width/3)        
        header          = f"{hName}{hStatus}{hProtocol}"
        
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(1, 0, header)
        #stdscr.addstr(2, len(header), " " * (ch.width - len(header) - 1))
        stdscr.attroff(curses.color_pair(3))
        pass

    def __InsertLine(self, stdscr, ch: CursesHelper ,yCord):
        o = TerminalOutput()
        reports = self.monitor.report
        for i in reports:
            lName       = o.AdjustColumn(i.name, ch.width/3)
            lStatus     = o.AdjustColumn(i.status, ch.width/3)
            lProtocol   = o.AdjustColumn(i.protocol.upper(), ch.width/3)
            line:str    = f"{lName}{lStatus}{lProtocol}"
            stdscr.addstr(yCord,0, line)
            yCord = yCord+1
        pass

if __name__ == "__main__":
    main = uiMain()
    main.Start()
    pass