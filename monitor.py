import os
import time
from datetime import datetime
import pickle

import mouse
import keyboard
from pathlib import Path


DESKTOP = Path.home() / 'Desktop'
os.mkdir(DESKTOP / 'dump')


def timeStamp(fmt='%Y-%m-%d_%H-%M-%S'):
    return datetime.now().strftime(fmt)


while True:
    mouse_events = []
    mouse.hook(mouse_events.append)
    keyboard.start_recording()

    time.sleep(60*5)

    mouse.unhook(mouse_events.append)
    keyboard_events = keyboard.stop_recording()

    with open(DESKTOP / 'dump' / f'{timeStamp()}.pickle', 'wb') as f:
        pickle.dump((mouse_events, keyboard_events), f)
