
import curses
import threading
import datetime
import time
import typing
from datetime import datetime
from networkmonitor import CursesHelper, Monitor
from networkmonitor.src import LogsCol
from networkmonitor.tui import uiLogs, uiHelp
#from uiLogs import uiLogs
#from uiHelp import uiHelp

class uiMain():
    def __init__(self, config):
        self.logs = []
        self.monitor = Monitor(config=config)
        #self.o = TerminalOutput()
        

        #self.tMonitor = threading.Thread(target=self.monitor.Start, daemon=True)
        pass

    def Start(self) -> None:
        ch = CursesHelper()
        ch.WindowNew()
        self.__RenderWindow(ch.stdscr)
        #curses.wrapper(self.__RenderWindow)
        pass
    
    def __RenderWindow(self, stdscr) -> None:

        ch = CursesHelper()

        # Make this window not block.
        # Lets the window keep looping but at the same time watches for key strokes
        #stdscr.nodelay(True)

        curses.halfdelay(10)
        ch.stdscr = stdscr

        self.monitor.Start(True)

        self.__GenLogData()

        # clear the scree and refresh
        ch.WindowClear()
        ch.WindowRefresh()

        # Start colors in curses
        curses.start_color()
        curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)


        # Refresh the screen with new data every 5 seconds
        
        dtRefresh = datetime.now()

        # Checking to see if the last key that was entered was 'F12'
        while (ch.key != curses.KEY_F12):
            #ch.WindowClear()
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
                ch.WindowRefresh()
            elif ch.key == curses.KEY_F9:                
                ch = self.__TuiLogs(stdscr)
                ch.WindowRefresh()
            else:
                # Render title
                self.monitor.Start()
                #ch.WindowRefresh()
                ch.UpdateScreenSize()
                self.__InsertTitle(stdscr)                
                self.__InsertColHeader(stdscr, ch)
                self.__InsertLine(stdscr, ch, 2)
                self.__InsertFooter(stdscr, ch)

                #ch.CursorMove()
                # Update the screen
            #ch.WindowRefresh()
            ch.GetCharacter()
            #time.sleep(.1)             
            
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
        curses.halfdelay(10)
        ch.stdscr = stdscr
        ch.SetCharacterBlockingMode(True)
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
        curses.halfdelay(10)
        ch.stdscr = stdscr  
        ch.SetCharacterBlockingMode(True)
        ch.WindowClear()
        ch.WindowRefresh()
        ch.key = 0 
        return ch

    def __InsertTitle(self, stdscr):
        
        res = self.GetNextNodeRefreshTime(self.monitor.c.SleepTimer, self.monitor.LastRefresh)
        title           = f"|NetworkMonitor |Refresh@{res} | "
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
        #o = TerminalOutput()
        hName           = ch.AdjustColumn("Name", ch.width/4)
        hStatus         = ch.AdjustColumn("Status", ch.width/4)
        hProtocol       = ch.AdjustColumn("Protocol", ch.width/4)        
        hMs             = ch.AdjustColumn("MS", ch.width/4)
        header          = f"{hName}{hStatus}{hProtocol}{hMs}"
        
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(1, 0, header)
        #stdscr.addstr(2, len(header), " " * (ch.width - len(header) - 1))
        stdscr.attroff(curses.color_pair(3))
        pass

    def __InsertLine(self, stdscr, ch: CursesHelper ,yCord):
        #o = TerminalOutput()
        reports = self.monitor.report
        for i in reports:
            lName       = ch.AdjustColumn(i.name, ch.width/4)
            lStatus     = ch.AdjustColumn(i.status, ch.width/4)
            lProtocol   = ch.AdjustColumn(i.protocol.upper(), ch.width/4)
            lMs         = ch.AdjustColumn(str(i.ms), ch.width/4)
            line:str    = f"{lName}{lStatus}{lProtocol}{lMs}"
            if i.status == "Offline":
                stdscr.attron(curses.color_pair(2))
                stdscr.addstr(yCord,0, line)
                stdscr.attroff(curses.color_pair(2))
            elif i.status == "Online":
                stdscr.attron(curses.color_pair(4))
                stdscr.addstr(yCord,0, line)
                stdscr.attroff(curses.color_pair(4))
            else:
                stdscr.addstr(yCord,0, line)
            yCord = yCord+1
        pass

    def GetNextNodeRefreshTime(self, sleepTimer:int, lastRefresh:datetime):
        """
        Returns the second value before nodes are checked again
        :param sleepTimer   = Contains the sleep timer value from config
        :param lastRefresh  = Contains the datetime value of the last refresh
        """
        
        # Convert lastRefresh into long seconds based off sleepTimer value
        a:float = sleepTimer / 60
        s:str = str(a)
        arr = s.split('.')

        if arr.__len__() == 3:
            hour        = self.CleanHourValue(lastRefresh.hour    + int(arr[0]))
            if hour >= 24:
                i = hour - 24

            minute      = self.CleanMinuteValue(lastRefresh.minute  + int(arr[1]))
            sec         = self.CleanMinuteValue(lastRefresh.second  + int(arr[2]))
        elif arr.__len__() == 2:
            hour        = lastRefresh.hour
            minute      = self.CleanMinuteValue(lastRefresh.minute + int(arr[0]))
            sec         = self.CleanMinuteValue(lastRefresh.second + int(arr[1]))
        elif arr.__len__() == 1:
            hour        = lastRefresh.hour
            minute      = lastRefresh.minute
            sec         = self.CleanMinuteValue(lastRefresh.second + int(arr[1]))

        return f"{hour}:{minute}:{sec}"

    def CleanHourValue(self, hour:int):
        if hour >= 24:
            i = hour - 24
            hour = 0
            hour = hour + i
        
        return hour

    def CleanMinuteValue(self, minute:int):
        if minute >= 60:
            i = minute - 60
            minute = 0
            minute = minute + i

        return minute

