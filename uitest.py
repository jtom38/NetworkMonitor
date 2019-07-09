
import curses

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

        cursor_x = max(0, cursor_x)
        cursor_x = min(width-1, cursor_x)
        cursor_y = max(0, cursor_y)
        cursor_y = min(height-1, cursor_y)

        # If user trys to go outside the bounds, reset to 0,0
        # if they try to go larger then x, reset to max
        #if self.cursor_x >= self.width:
        #    self.cursor_x = 0

        # if they go smaller then x, reset to 0
        #if self.cursor_x <= 0:
        #    self.cursor_x = self.width-1

        #if self.cursor_y >= self.height:
        #    self.cursor_y = 0

        #if self.cursor_y <= 0:
        #    self.cursor_y = self.height-1
        
        self.stdscr.move(self.cursor_y, self.cursor_x)

    def GetCharacter(self):
        """
        Gets the last character that was used
        """
        self.key = self.stdscr.getch()
        self.uniKey = self.stdscr.getkey()




def draw_main(stdscr):
    ch = CursesHelper(stdscr)

    key = 0
    cursor_x = 0
    cursor_y = 0

    # clear the scree and refresh
    #ch.WindowClear()
    #ch.WindowRefresh()

    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Checking to see if the last key that was entered was 'q'
    #while (key != ord('F12')):
    while (key != curses.KEY_F12):
        
        #ch.WindowClear()
        stdscr.clear()

        # Tells us the screens height and width
        height, width = stdscr.getmaxyx()
        #ch.CursorMove()

        ## Cursor
        # Check if the user entered a arrow key to move the cursor
        if key == curses.KEY_DOWN:
            cursor_y = cursor_y + 1
        elif key == curses.KEY_UP:
            cursor_y = cursor_y - 1
        elif key == curses.KEY_RIGHT:
            cursor_x = cursor_x + 1
        elif key == curses.KEY_LEFT:
            cursor_x = cursor_x - 1

        cursor_x = max(0, cursor_x)
        cursor_x = min(width-1, cursor_x)
        cursor_y = max(0, cursor_y)
        cursor_y = min(height-1, cursor_y)

        # If user trys to go outside the bounds, reset to 0,0
        # if they try to go larger then x, reset to max
        if cursor_x >= width:
            cursor_x = width-1

        # if they go smaller then x, reset to 0
        if cursor_x <= 0:
            cursor_x = 0

        if cursor_y >= height:
            cursor_y = height-1

        if cursor_y <= 0:
            cursor_y = 0
        
        stdscr.move(cursor_y, cursor_x)
        ## End Cursor

        if key == ord('q'):
            # Exit application
            pass
        elif key == ord('l'):
            # Open logs
            pass
        else:
            pass

        title = "Network Monitor"
        statusbarstr = "|F1|Main  |F2|Logs  |F10|Help  |F12|Quit"
       
        # Render title
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(0, 0, title, curses.color_pair(1))
        stdscr.attroff(curses.color_pair(3))

        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(ch.height-1, 0, statusbarstr)
        stdscr.addstr(ch.height-1, len(statusbarstr), " " * (ch.width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))


        # Update the screen
        #ch.WindowRefresh()
        stdscr.move(cursor_y, cursor_x)

        stdscr.refresh()

        #stdscr = ch.stdscr
        #ch.GetCharacter()
        key = stdscr.getch()

def main():
    curses.wrapper(draw_main)

if __name__ == "__main__":
    main()

