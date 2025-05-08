# Project 6: Countdown Timer Python Project

import time

def countdown_timer():
    seconds = int(input("Enter the time in seconds: "))
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = f'{mins:02d}:{secs:02d}'
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

countdown_timer()
