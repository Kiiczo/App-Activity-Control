import subprocess

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

    return list(apps)

print(current_procces())