
import os
import time

class TerminalOutput():

    def __init__(self):
        self.output: str = ''
        self.numOfColumns:int = 3
        pass

    def AdjustColumn(self, value:str, Width:int):
        # Get the max width of the terminal size
        maxTermWidth  = self.GetTerminalWidth()

        # Figure out how large our columns can be
        colWidth = maxTermWidth / self.numOfColumns

        if value.__len__() < colWidth:
            while value.__len__() < colWidth:
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
        self.output = f"{self.output}\n{row}"

    def StartSleep(self, SleepTimer:int):

        i = 0
        remaining = SleepTimer
        while i < SleepTimer:
            self.ClearTerminal()
            print(self.output)
            print(f"Checking again in {remaining}...")

            i = i+5
            remaining = remaining-5
            time.sleep(5)
        pass

    def GetTerminalWidth(self):
        rows, columns = os.popen('stty size', 'r').read().split()
        return int(columns)

    def GetTerminalHeight(self):
       rows, columns = os.popen('stty size', 'r').read().split() 
       return int(rows)

#if __name__ == "__main__":
    #TerminalOutput
    #pass