
import os
import time
import colorama

class TerminalOutput():

    def __init__(self):
        colorama.init()
        self.output: str = ''
        self.numOfColumns:int = 3
        pass

    def AdjustColumn(self, value:str, Width:int):
        # Get the max width of the terminal size
        #maxTermWidth  = self.GetTerminalWidth()

        # Figure out how large our columns can be
        #colWidth = maxTermWidth / self.numOfColumns

        if value.__len__() < Width:
            while value.__len__() < Width:
                value = f"{value} "

        return value

    def ClearTerminal(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def ClearOutputCache(self):
        self.output = ''

    def InsertHeader(self):
        self.ClearOutputCache()
        self.AddRow("[NetworkMonitor][0.0.1]")
        self.AddRow("")

        hName       = self.AdjustColumn("Name", 20)
        hStatus     = self.AdjustColumn("Status", 10)
        hProtocol   = self.AdjustColumn("Protocol",10)
        self.AddRow(f"{hName}{hStatus}{hProtocol}")

    def InsertFooter(self):
        self.AddRow("")
        self.AddRow("To exit: CTRL+C")

    def AddRow(self, row:str):
        """
        About: Stores all the rows that it has been given.
        """
        if row.__contains__("Online"):
            self.output = f"{self.output}\n{colorama.Fore.GREEN}{row}{colorama.Style.RESET_ALL}"
        elif row.__contains__("Offline"):
            self.output = f"{self.output}\n{colorama.Fore.RED}{row}{colorama.Style.RESET_ALL}"
        else:
            self.output = f"{self.output}\n{row}"

    def StartSleep(self, SleepTimer:int):

        i = 0
        remaining = SleepTimer
        while i < SleepTimer:
            self.ClearTerminal()
            print(self.output)
            msg = f"Checking again in {remaining}..."
            print(f"{colorama.Back.LIGHTBLUE_EX}{msg}{colorama.Style.RESET_ALL}")

            i = i+5
            remaining = remaining-5
            time.sleep(5)
        pass

    def GetTerminalWidth(self):
        """
        Returns the max width of the terminal window.
        """
        # Returns the max width of the console

        rows, columns = os.popen('stty size', 'r').read().split()       
        c = int(columns) - 5
        return c

    def GetTerminalHeight(self):
       rows, columns = os.popen('stty size', 'r').read().split() 
       return int(rows)

#if __name__ == "__main__":
    #TerminalOutput
    #pass