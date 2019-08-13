import time
import datetime

now = datetime.datetime.now()

hour = 0
mins = 2
sec  = 0

last = datetime.datetime.now()
print(last)

newHour = last.hour + hour
if newHour >= 24:
    hour = newHour - 24
    pass

newMin = last.minute + mins
if last.minute + mins >= 60:
    mins = newMin - mins
    pass

newSec = last.second + sec
if last.second + sec >= 60:
    sec = newSec - sec
    pass


last = last.replace(hour=newHour, minute=newMin, second=newSec)
print(last)

if now <= last:
    print("time is diff")
n = time.localtime()
print()