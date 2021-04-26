import os
from datetime import datetime
import pickle
from pathlib import Path

import mouse
import keyboard


DESKTOP = Path.home() / 'Desktop'

dump_list = os.listdir(DESKTOP / 'dump')
dump_list.sort(key=lambda dump: datetime.strptime(dump, "%Y-%m-%d_%H-%M-%S.pickle"))

all_mouse_events, all_keyboard_events = [], []
for dump in dump_list:
    with open(DESKTOP / 'dump' / f'{dump}', 'rb') as f:
        mouse_events, keyboard_events = pickle.load(f)
        all_mouse_events.append(mouse_events)
        all_keyboard_events.append(keyboard_events)
