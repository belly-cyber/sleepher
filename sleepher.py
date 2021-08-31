#!/usr/bin/python3

import time
import sys


sec_in_24    = 86400
current_time =time.strftime('%H:%M:%S',time.localtime())
help_menu = """
sleepher.py [wake-up time] [-e[number of days]]
    example: 'python3 sleepher.py'
             'python3 sleepher.py -e'
             'python3 sleepher.py -e 4'
             python3 sleepher.py 13:00'
    
        'wake-up' default time is 8:00am
        -e(weekEnd) default time is two days
        -h shows this message

"""

if len(sys.argv) >1 and len(sys.argv[1])>=4:
    wakeup_time = sys.argv[1]
else:
    wakeup_time  = '08:00'

def overnight_sleep(c_time=current_time,wake_time=wakeup_time):
    CH,CM,CS = map(int,c_time.split(':'))
    WH,WM = map(int,wake_time.split(':'))
    seconds = sec_in_24 - (CH*60*60+CM*60+CS) + (WH*60*60 + WM*60)
    return seconds

def weekend_sleep(days_off):
    seconds = overnight_sleep() + days_off*sec_in_24
    return seconds

    
try:
    if '-h' in sys.argv:
        print(help_menu)
    elif '-e' in sys.argv:
        if sys.argv.index('-e')+1 <len(sys.argv) :
            num_days=int(sys.argv[sys.argv.index('-e')+1])
        else:
            num_days=2
        print(weekend_sleep(days_off=num_days))
    else:
        print(overnight_sleep())
except:print(help_menu)
