import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from datetime import datetime
import pandas as pd

from gui import Ui_MainWindow

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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.df = pd.read_csv("dane.csv", index_col=0)

        self.today = datetime.today().strftime('%Y-%m-%d')

        self.update_label()

        self.timer = self.startTimer(1000)

    def timerEvent(self, event):
        self.update_label()

    def update_label(self):
        df = pd.read_csv("dane.csv", index_col=0)
        value = df.loc[self.today, "system"]
        value = sec_to_time(value)
        self.ui.label.setText(str(value))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
