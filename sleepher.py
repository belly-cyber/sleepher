#!/usr/bin/python3
import time
import sys

sec_in_24    = 86400
current_time =time.strftime('%H:%M',time.localtime())

help_menu = """
sleepher.py [wake-up time] [-e[number of days off]]

    example: 'python3 sleepher.py 08:00'
    'wake-up' default time is 08:00
    -e(weekEnd) default time is two days
    -h shows this message
"""
for argv in sys.argv:
    if ':' in argv:
        wakeup_time=argv
        sys.argv.remove(argv)
        break 
    else:
        wakeup_time  = '08:00'

def to_seconds(t):
    '''input = time in 00:00 format
       outputs into seconds
    '''
    return sum([(60**i) * int(seg) for i,seg in enumerate(t.split(':')[::-1],start=1)])

def overnight_sleep():
    return sec_in_24 + to_seconds(wakeup_time) - to_seconds(current_time)

def weekend_sleep(days_off):
    return overnight_sleep() + (sec_in_24 * days_off)
    
try:
    if '-h' in sys.argv:
        print(help_menu)
    elif '-e' in sys.argv:
        if sys.argv.index('-e') + 1 < len(sys.argv):
            num_days = int(sys.argv[sys.argv.index('-e')+1])
        else:
            num_days = 2
        print(weekend_sleep(num_days))
    else:
        print(overnight_sleep())
except:print(help_menu)
