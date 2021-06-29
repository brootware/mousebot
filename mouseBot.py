from random import *
import win32api
import win32con
import datetime
import time
import tkinter as tk

# Time to stop is set to 6pm by default. Uses 24 hours time
time_to_stop = datetime.time(18, 00, 0)
current_time = datetime.datetime.now().time()


def click(x, y):
    # cursor move
    win32api.SetCursorPos((x, y))
    # click even call
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


while True:
    # get screen size
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # pass random value to axis
    x = randint(screen_height-500, screen_width-500)
    y = randint(screen_height-500, screen_width-500)
    click(x, y)
    print('I am moving to x=', x, ' and y=', y)

    if current_time > time_to_stop:
        print("It's after ", time_to_stop, " now, stopping this script.")
        break
    else:
        # Interval in seconds
        time.sleep(5)
