import os
from datetime import datetime
import pickle

import mouse
import keyboard


dump_list = os.listdir('dump')
dump_list.sort(key=lambda dump: datetime.strptime(dump, "%Y-%m-%d_%H-%M-%S.pickle"))

all_mouse_events, all_keyboard_events = [], []
for dump in dump_list:
    with open(f'dump\{dump}', 'rb') as f:
        mouse_events, keyboard_events = pickle.load(f)
        all_mouse_events.append(mouse_events)
        all_keyboard_events.append(keyboard_events)
