
import curses
from networkmonitor import CursesHelper, Ping, TerminalOutput, LogsCol
from uiLogs import uiLogs
from uiHelp import uiHelp

class uiMain():

    def __init__(self):
        self.logs = []
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

        p = Ping()
        o = TerminalOutput()
        l = uiLogs()
        h = uiHelp()
        
        i = 0
        while i < 10:
            self.logs.insert(self.logs.__len__()+1 ,LogsCol(level='debug', message='Unable to reach service.', name='Google', address="www.google.com", protocol='ICMP') )
            i = i+1

        # clear the scree and refresh
        ch.WindowClear()
        ch.WindowRefresh()

        # Start colors in curses
        curses.start_color()
        curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

        # Checking to see if the last key that was entered was 'F12'
        while (ch.key != curses.KEY_F12):
            
            ch.WindowClear()
            #stdscr.clear()

            # Tells us the screens height and width      
            ch.CursorMove()

            if ch.key == ord('q'):
                # Exit application
                pass

            elif ch.key == curses.KEY_F10:
                h.Start()

                ch = CursesHelper()
                ch.stdscr = stdscr
                ch.WindowClear()
                ch.WindowRefresh()
                ch.key = 0

            elif ch.key == curses.KEY_F2:                
                l.logs = self.logs
                l.Start()        

                # Once we come back here, update ch with the current stdscr
                # Helps to make the window accept input again
                ch = CursesHelper()
                ch.stdscr = stdscr  
                ch.WindowClear()
                ch.WindowRefresh()
                ch.key = 0 
            else:
                # Render title
                self.__InsertTitle(stdscr)                
                self.__InsertColHeader(stdscr, ch)
                self.__InsertLine(stdscr, o, ch, 3)
                self.__InsertFooter(stdscr, ch)

                ch.CursorMove()
                # Update the screen
                ch.WindowRefresh()

                ch.GetCharacter()
                pass

           #key = stdscr.getch()
        
        # Close key was pressed
        ch.WindowClose()            


    def __InsertTitle(self, stdscr):
        title = "Network Monitor"
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(0, 0, title, curses.color_pair(1))
        stdscr.attroff(curses.color_pair(3))
        pass

    def __InsertFooter(self, stdscr, ch: CursesHelper):
        statusbarstr    = "|F1|Main  |F2|Logs  |F10|Help  |F12|Quit"
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
        stdscr.addstr(2, 0, header)
        #stdscr.addstr(2, len(header), " " * (ch.width - len(header) - 1))
        stdscr.attroff(curses.color_pair(3))
        pass

    def __InsertLine(self, stdscr, o: TerminalOutput, ch: CursesHelper ,yCord):
        res         = "Online"
        lName       = o.AdjustColumn("Google", ch.width/3)
        lStatus     = o.AdjustColumn(res, ch.width/3)
        lProtocol   = o.AdjustColumn("ICMP", ch.width/3)
        line:str    = f"{lName}{lStatus}{lProtocol}"
        stdscr.addstr(yCord,0, line)
        pass

if __name__ == "__main__":
    main = uiMain()
    main.Start()
    pass