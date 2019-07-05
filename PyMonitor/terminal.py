
import os
import time

class TerminalOutput():

    def __init__(self):
        self.output: str = ''
        pass

    def AdjustColumn(self, value:str, Width:int):

        idk = value.__len__()

        if value.__len__() < Width:
            while value.__len__() < Width:
                value = f"{value} "

        return value

    def ClearTerminal(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

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
        

if __name__ == "__main__":
    TerminalOutput
    pass