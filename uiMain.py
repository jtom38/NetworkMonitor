
import curses
from networkmonitor import CursesHelper, Ping, TerminalOutput
from uiLogs import uiLogs

class uiMain():

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

        p = Ping()
        o = TerminalOutput()
        l = uiLogs()

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
            elif ch.key == ord('l'):
                # Open logs
                pass
            elif ch.key == curses.KEY_F2:
                l.Start()          
                #ch = CursesHelper()

                ch.WindowClear()
                ch.WindowRefresh()
                ch.key = 0 
            else:
                pass

            # Render title
            self.__InsertTitle(stdscr)

            # x and y pos        
            #stdscr.attron(curses.color_pair(3))
            #stdscr.addstr(1,0, cur, curses.color_pair(1))
            #stdscr.attroff(curses.color_pair(3))
            self.__InsertColHeader(stdscr, ch, o)
            self.__InsertLine(stdscr, o, 3)
            self.__InsertFooter(stdscr, ch)

            ch.CursorMove()
            # Update the screen
            ch.WindowRefresh()
            
            ch.GetCharacter()
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

    def __InsertColHeader(self, stdscr, ch:CursesHelper, o:TerminalOutput):
        hName           = o.AdjustColumn("Name", 15)
        hStatus         = o.AdjustColumn("Status", 15)
        hProtocol       = o.AdjustColumn("Protocol", 15)        
        header          = f"{hName}{hStatus}{hProtocol}"
        
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(2, 0, header)
        stdscr.addstr(2, len(header), " " * (ch.width - len(header) - 1))
        stdscr.attroff(curses.color_pair(3))
        pass

    def __InsertLine(self, stdscr, o: TerminalOutput, yCord):
        res = "Online"
        lName = o.AdjustColumn("Google", 15)
        lStatus = o.AdjustColumn(res, 15)
        lProtocol = o.AdjustColumn("ICMP", 15)
        line:str = f"{lName}{lStatus}{lProtocol}"
        stdscr.addstr(yCord,0, line)
        pass

if __name__ == "__main__":
    main = uiMain()
    main.Start()
    pass