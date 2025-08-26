import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPixmap
from datetime import datetime
import pandas as pd

from gui import Ui_MainWindow

def sec_to_time(sec):
    if sec < 60:
        return f"{sec}s"
    else:
        minutes = sec // 60
        sec = sec % 60
        if minutes < 60:
            return f"{minutes}m {sec}s"
        else:
            hours = minutes // 60
            minutes = minutes % 60
            return f"{hours}h {minutes}m {sec}s"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Dashboard.setPixmap(QPixmap("Dashboard.png"))

        self.timer = self.startTimer(1000)

        self.ui.dashboardBtn.clicked.connect(self.show_dashboard)
        self.ui.reportsBtn.clicked.connect(self.show_reports)
        self.ui.apptimersBtn.clicked.connect(self.show_apptimers)

    def show_dashboard(self):
        self.ui.Dashboard.setPixmap(QPixmap("Dashboard.png"))
        self.ui.label.show()

    def show_reports(self):
        self.ui.Dashboard.setPixmap(QPixmap("Reports.png"))
        self.ui.label.hide()

    def show_apptimers(self):
        self.ui.Dashboard.setPixmap(QPixmap("AppTimers.png"))
        self.ui.label.hide()

    def timerEvent(self, event):
        self.update_label()

    def update_label(self):
        df = pd.read_csv("dane.csv", index_col=0)
        today = datetime.today().strftime('%Y-%m-%d')
        value = df.loc[today, "system"]
        value = sec_to_time(value)
        self.ui.label.setText(value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
