
import sqlite3

class SQL:
    def __init__(self):
        con = sqlite3.connect("networkmonitor.db")
        pass

if __name__ == "__main__":
    SQL