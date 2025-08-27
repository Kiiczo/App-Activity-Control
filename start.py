import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QSizePolicy
)
from PySide6.QtGui import QPixmap
from datetime import datetime
import pandas as pd

from gui import Ui_MainWindow

def sec_to_time(sec: int) -> str:
    if sec < 60:
        return f"{sec}s"
    minutes = sec // 60
    sec = sec % 60
    if minutes < 60:
        return f"{minutes}m {sec}s"
    hours = minutes // 60
    minutes = minutes % 60
    return f"{hours}h {minutes}m {sec}s"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Dashboard.setPixmap(QPixmap("Dashboard.png"))

        self.scroll_layout = QVBoxLayout(self.ui.AppScrollWidget)
        self.scroll_layout.setSpacing(5)
        self.scroll_layout.setContentsMargins(5, 5, 5, 5)

        self.scroll_most = QVBoxLayout(self.ui.AppScrollWidget_2)
        self.scroll_most.setSpacing(5)
        self.scroll_most.setContentsMargins(5, 5, 5, 5)

        self.timer = self.startTimer(1000)

        self.ui.dashboardBtn.clicked.connect(self.show_dashboard)
        self.ui.reportsBtn.clicked.connect(self.show_reports)
        self.ui.apptimersBtn.clicked.connect(self.show_apptimers)

        self.show_dashboard()

    def show_dashboard(self):
        self.ui.Dashboard.setPixmap(QPixmap("Dashboard.png"))
        self.ui.label.show()
        self.ui.AppScrollArea.show()
        self.update_scroll()
        self.update_apptimers()
        self.ui.AppsMonitored.show()
        self.ui.Applications.show()

    def show_reports(self):
        self.ui.Dashboard.setPixmap(QPixmap("Reports.png"))
        self.ui.label.hide()
        self.ui.AppScrollArea.hide()
        self.ui.AppsMonitored.hide()
        self.ui.Applications.hide()

    def show_apptimers(self):
        self.ui.Dashboard.setPixmap(QPixmap("AppTimers.png"))
        self.ui.label.hide()
        self.ui.AppScrollArea.hide()
        self.ui.AppsMonitored.hide()
        self.ui.Applications.hide()

    def timerEvent(self, event):
        self.update_label()
        if self.ui.AppScrollArea.isVisible():
            self.update_scroll()
            self.update_apptimers()

    def update_label(self):
        df = pd.read_csv("dane.csv", index_col=0)
        today = datetime.today().strftime('%Y-%m-%d')
        if today in df.index:
            value = df.loc[today, "system"]
            value = sec_to_time(value)
            apps = df.loc[today, "apps_amount"]
            maxApp = df.loc[today].idxmax()
            self.ui.label.setText(value)
            self.ui.MostUsedApp.setText(str(maxApp))
            self.ui.AppsMonitored.setText(str(apps))

    def update_scroll(self):
        df = pd.read_csv("dane.csv", index_col=0)
        today = datetime.today().strftime('%Y-%m-%d')
        if today not in df.index:
            return

        for i in reversed(range(self.scroll_layout.count())):
            widget = self.scroll_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        app_times = {
            col: df.loc[today, col]
            for col in df.columns if col != "system" and df.loc[today, col] > 0
        }
        sorted_apps = sorted(app_times.items(), key=lambda x: x[1], reverse=True)

        for col, value in sorted_apps:
            label = QLabel(f"{col}{" "*(80-len(col))}{sec_to_time(value)}")
            label.setStyleSheet("""
                QLabel {
                    color: white;
                    font-family: 'Monospace';
                    background-color: rgba(33, 22, 74, 0);
                    font-size: 16px;
                    padding: 5px;
                    border-top: 1px solid rgb(92, 93, 126);
                }
                QLabel:hover {
                    background-color: rgb(56, 52, 132);
                    color: white;
                    border-top: 1px solid rgb(92, 93, 126);
                }
            """)
            label.setFixedHeight(40)
            label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            self.scroll_layout.addWidget(label)

        self.scroll_layout.addStretch()

    def update_apptimers(self):
        df = pd.read_csv("dane.csv", index_col=0)
        today = datetime.today().strftime('%Y-%m-%d')
        if today not in df.index:
            return

        for i in reversed(range(self.scroll_most.count())):
            widget = self.scroll_most.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        app_times = {
            col: df[col].sum()
            for col in df.columns if col != "system" and df.loc[today, col] > 0
        }
        sorted_apps = sorted(app_times.items(), key=lambda x: x[1], reverse=True)

        for col, value in sorted_apps:
            label = QLabel(f"{col}{" " * (26 - len(col))}{sec_to_time(value)}")
            label.setStyleSheet("""
                        QLabel {
                            color: white;
                            font-family: 'Monospace';
                            background-color: rgba(33, 22, 74, 0);
                            font-size: 16px;
                            padding: 5px;
                            border-top: 1px solid rgb(92, 93, 126);
                        }
                        QLabel:hover {
                            background-color: rgb(56, 52, 132);
                            color: white;
                            border-top: 1px solid rgb(92, 93, 126);
                        }
                    """)
            label.setFixedHeight(40)
            label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            self.scroll_most.addWidget(label)

        self.scroll_most.addStretch()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())