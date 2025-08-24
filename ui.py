import customtkinter as ctk
import pandas as pd
from datetime import datetime
from PIL import Image, ImageTk

def sec_to_time(sec):
    if sec < 60:
        return f"{sec}s"
    else:
        min = sec // 60
        sec = sec % 60
        if min < 60:
            return f"{min}m {sec}s"
        else:
            hour = min // 60
            min = min % 60
            return f"{hour}h {min}m {sec}s"

def update_value():
    today = datetime.today().strftime('%Y-%m-%d')

    df = pd.read_csv("dane.csv", index_col=0)
    total = df.loc[today, "system"]
    total = sec_to_time(total)
    apps = df.loc[today, "apps_amount"]

    canvas.itemconfig(total_item, text=total)
    canvas.itemconfig(apps_item, text=apps)

    root.after(1000, update_value)

def reports():
    pass

root = ctk.CTk()

root.title("test")
bg_image = Image.open("Dashboard.png")

bg_photo = ImageTk.PhotoImage(bg_image)
canvas = ctk.CTkCanvas(root, width=bg_image.width, height=bg_image.height)
canvas.pack()

canvas.create_image(0, 0, anchor="nw", image=bg_photo)

dashboard_button = ctk.CTkButton(root, text="Dashboard", fg_color="#21164A", width=250, height=50)
reports_button = ctk.CTkButton(root, text="Reports", fg_color="#21164A", width=250, height=50, command=reports)

canvas.create_window(130,400, window=dashboard_button)
canvas.create_window(130,450, window=reports_button)
total_item = canvas.create_text(485, 195, text="", font=("Arial", 15), fill="white")

apps_item = canvas.create_text(840, 195, text="", font=("Arial", 15), fill="white")

update_value()

root.resizable(False, False)
root.mainloop()
