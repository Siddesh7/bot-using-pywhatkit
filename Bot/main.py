from os import close
import pywhatkit as py
import pyautogui as pg
import time
import pydirectinput as pd
from typing import NoReturn, Optional


numbers = [num1, num2]


mg = '''message to be sent'''


def close_tab(wait_time: int = 6) -> NoReturn:
    time.sleep(wait_time)

    pg.hotkey("ctrl", "w")
    pg.press("enter")


for i in range(len(numbers)):
    py.sendwhatmsg_instantly(f'+91{numbers[i]}', mg)
    pg.press("enter")
    pd.press("enter")
    time.sleep(1)
    close_tab()
