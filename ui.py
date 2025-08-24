from tkinter import *
import customtkinter
import pandas as pd
from datetime import datetime

root = Tk()
root.title('test')

bg = PhotoImage(file='Dashboard.png')

canvas = Canvas(root, width=bg.width(), height=bg.height())
canvas.pack()
canvas.create_image(0, 0, anchor="nw", image=bg)

today = datetime.today().strftime('%Y-%m-%d')

total_item = canvas.create_text(485, 195, text="", font=("Arial", 15), fill="white")
apps_item =  canvas.create_text(840, 195, text="", font=("Arial", 15), fill="white")

def sec_to_time(sec):
    if sec < 60:
        return str(sec) + "s "
    else:
        min = sec // 60
        sec = sec % 60
        if min < 60:
            return str(min) + "m " + str(sec) + "s"
        else:
            hour = min // 60
            min = min % 60
            return str(hour) + "h " + str(min) + "m " + str(sec) + "s"


def update_value():
    df = pd.read_csv('dane.csv', index_col=0)

    total = df.loc[today, 'system']
    total = sec_to_time(total)

    apps = df.loc[today, 'apps_amount']

    canvas.itemconfig(total_item, text=total)
    canvas.itemconfig(apps_item, text=apps)

    root.after(1000, update_value)

update_value()

root.resizable(False, False)
root.mainloop()
