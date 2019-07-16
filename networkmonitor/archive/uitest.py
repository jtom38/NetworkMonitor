
import curses
from networkmonitor import Config, Ping, TerminalOutput

class CursesHelper():

    def __init__(self, stdscr):

        #self.stdscr = curses.initscr()
        #curses.noecho()
        #curses.cbreak()
        #self.stdscr.keypad(True)
        self.stdscr     = stdscr

        curses.start_color()
        height, width   = self.stdscr.getmaxyx()

        self.key:int    = 0
        self.uniKey:chr = ' '
        self.cursor_x   = 0
        self.cursor_y   = 0
        self.height     = int(height)
        self.width      = int(width)

        pass

    def WindowNew(self):
        """
        Generates a new window 
        """
        s = curses.initscr()
        curses.noecho()
        curses.cbreak()
        s.keypad(True)

    def WindowExit(self):
        """
        Closes the active curses window
        """
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()

    def Start(self):
        self.screen = curses.wrapper(draw_main)
        pass

    def WindowClear(self):
        self.stdscr.clear()
        pass

    def WindowRefresh(self):
        self.stdscr.refresh()

    def CursorMove(self):
        # Check if the user entered a arrow key to move the cursor
        if self.key == curses.KEY_DOWN:
            self.cursor_y = self.cursor_y + 1
        elif self.key == curses.KEY_UP:
            self.cursor_y = self.cursor_y - 1
        elif self.key == curses.KEY_RIGHT:
            self.cursor_x = self.cursor_x + 1
        elif self.key == curses.KEY_LEFT:
            self.cursor_x = self.cursor_x - 1

        self.cursor_x = max(0, self.cursor_x)
        self.cursor_x = min(self.width-1, self.cursor_x)
        self.cursor_y = max(0, self.cursor_y)
        self.cursor_y = min(self.height-1, self.cursor_y)

        # If user trys to go outside the bounds, reset to 0,0
        # if they try to go larger then x, reset to max
        
        if self.cursor_x == self.width:
            self.cursor_x = 0

        # if they go smaller then x, reset to 0
        if self.cursor_x <= 0:
            self.cursor_x = self.width-1

        if self.cursor_y >= self.height:
            self.cursor_y = 0

        if self.cursor_y <= 0:
            self.cursor_y = self.height-1
        
        
        self.stdscr.move(self.cursor_y, self.cursor_x)

    def GetCharacter(self):
        """
        Gets the last character that was used
        """
        self.key = self.stdscr.getch()
        #self.uniKey = self.stdscr.getkey()


def draw_main(stdscr):
    ch = CursesHelper(stdscr)
    p = Ping()
    o = TerminalOutput()


    key = 0
    cursor_x = 0
    cursor_y = 0

    # clear the scree and refresh
    ch.WindowClear()
    ch.WindowRefresh()


    #stdscr.clear()
    #stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Checking to see if the last key that was entered was 'F12'
    while (ch.key != curses.KEY_F12):
        
        #ch.WindowClear()
        stdscr.clear()

        # Tells us the screens height and width      
        ch.CursorMove()

        if ch.key == ord('q'):
            # Exit application
            pass
        elif ch.key == ord('l'):
            # Open logs
            pass
        else:
            pass

        res = p.ProcessICMP("http://www.google.com")

        title           = "Network Monitor"
        cur             = f"x:{ch.cursor_x} y:{ch.cursor_y} "
        statusbarstr    = "|F1|Main  |F2|Logs  |F10|Help  |F12|Quit"      
        hName           = o.AdjustColumn("Name", 15)
        hStatus         = o.AdjustColumn("Status", 15)
        hProtocol       = o.AdjustColumn("Protocol", 15)        
        header          = f"{hName}{hStatus}{hProtocol}"

        # Render title
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(0, 0, title, curses.color_pair(1))
        stdscr.attroff(curses.color_pair(3))

        # x and y pos        
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(1,0, cur, curses.color_pair(1))
        stdscr.attroff(curses.color_pair(3))

        # Column header
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(2, 0, header)
        stdscr.addstr(2, len(header), " " * (ch.width - len(header) - 1))
        stdscr.attroff(curses.color_pair(3))

        ## Insert all results
        lName = o.AdjustColumn("Google", 15)
        lStatus = o.AdjustColumn(res, 15)
        lProtocol = o.AdjustColumn("ICMP", 15)
        line:str = f"{lName}{lStatus}{lProtocol}"
        stdscr.addstr(3,0, line)

        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(ch.height-1, 0, statusbarstr)
        stdscr.addstr(ch.height-1, len(statusbarstr), " " * (ch.width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))

        ch.CursorMove()
        # Update the screen
        ch.WindowRefresh()
        #stdscr.move(cursor_y, cursor_x)

        #stdscr.refresh()

        #stdscr = ch.stdscr
        ch.GetCharacter()
        #key = stdscr.getch()

def main():
    curses.wrapper(draw_main)

if __name__ == "__main__":
    main()

