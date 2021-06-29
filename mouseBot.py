from random import *
import win32api
import win32con
import datetime
import time
import tkinter as tk

# Time to stop is set to 6pm by default. Uses 24 hours time
time_to_stop = datetime.time(18, 00, 0)
condition_to_run = True


def moveClick(x, y):
    # cursor move
    win32api.SetCursorPos((x, y))
    # click even call. Optional
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


while condition_to_run:
    # get current time
    current_time = datetime.datetime.now().time()
    # get screen size
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # pass random value to axis
    x = randint(screen_height, screen_width)
    y = randint(screen_height, screen_width)
    moveClick(x, y)
    print('Mouse moved to x=', x, ' and y=', y)

    if current_time > time_to_stop:
        print("It's after ", time_to_stop, " now, stopping this script.")
        condition_to_run = False

    # Interval in seconds
    time.sleep(10)
