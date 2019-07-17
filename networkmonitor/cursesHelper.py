
import curses

class CursesHelper():
    
    def __init__(self):

        #self.stdscr = curses.initscr()
        #curses.noecho()
        #curses.cbreak()
        #self.stdscr.keypad(True)
        self.stdscr = self.WindowNew()
        self.stdscr.nodelay(True)
        #self.stdscr     = stdscr

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
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)
        return stdscr

    def WindowClose(self):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()

    def WindowClear(self):
        self.stdscr.clear()
        pass

    def WindowRefresh(self):
        height, width   = self.stdscr.getmaxyx()
        self.height     = int(height)
        self.width      = int(width)
        self.stdscr.refresh()

    def WindowHeight(self):
        return

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
        
        try:
            self.stdscr.move(self.cursor_y, self.cursor_x)
        except:
            # keep going
            pass

    def GetCharacter(self):
        """
        Gets the last character that was used
        """
        self.key = self.stdscr.getch()
        #self.uniKey = self.stdscr.getkey()