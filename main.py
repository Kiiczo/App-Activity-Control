import subprocess
import pandas as pd
from datetime import datetime
import time

def current_procces():
    output = subprocess.check_output(['wmctrl', '-lp'], text=True)

    apps = set()

    for line in output.splitlines():
        proc = line.split()
        window_id = proc[0]

        wm_class = subprocess.check_output(
            ['xprop', '-id', window_id, 'WM_CLASS'],
            text=True, stderr=subprocess.DEVNULL
        ).strip()

        wm_class = wm_class.split('=')[1].strip()
        wm_class = wm_class.split(',')[1].strip().strip('"')
        apps.add(wm_class)

    return sorted(list(apps))


def time_counting():
    apps = current_procces()
    for i in apps:
        if i not in df.columns:
            df[i] = 0

        if today not in df.index:
            df.loc[today] = 0

        df.loc[today, i] += 1

    if 'system' not in df.columns:
        df['system'] = 0
    else:
        df.loc[today, 'system'] += 1

    if 'apps_amount' not in df.columns:
        df['apps_amount'] = 0
    else:
        df.loc[today, 'apps_amount'] = len(apps)

def save_data():
    df.to_csv("dane.csv")

today = datetime.today().strftime('%Y-%m-%d')

try:
    df = pd.read_csv("dane.csv", index_col=0)
except FileNotFoundError:
    df = pd.DataFrame()

counter = 0
save_time = 1

while True:
    today = datetime.today().strftime('%Y-%m-%d')
    time_counting()
    counter += 1
    if counter == save_time:
        counter = 0
        save_data()
    time.sleep(1)