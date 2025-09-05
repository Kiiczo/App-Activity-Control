# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledABCcYb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.13
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1912, 1080)
        MainWindow.setStyleSheet(u"#central QPushButton {\n"
"    color: rgb(183, 183, 183);\n"
"    background-color: rgba(33, 22, 74,0);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"#central QPushButton:hover {\n"
"    background-color: rgb(56, 52, 132);\n"
"    color: white;\n"
"}\n"
"\n"
"#central QPushButton:pressed {\n"
"    background-color: rgb(57, 63, 189);\n"
"    color: white;\n"
"}\n"
"")
        self.central = QWidget(MainWindow)
        self.central.setObjectName(u"central")
        self.Dashboard = QLabel(self.central)
        self.Dashboard.setObjectName(u"Dashboard")
        self.Dashboard.setGeometry(QRect(0, 0, 1920, 1080))
        self.Dashboard.setPixmap(QPixmap(u"Downloads/Dashboard (2).png"))
        self.reportsBtn = QPushButton(self.central)
        self.reportsBtn.setObjectName(u"reportsBtn")
        self.reportsBtn.setGeometry(QRect(30, 270, 271, 75))
        self.apptimersBtn = QPushButton(self.central)
        self.apptimersBtn.setObjectName(u"apptimersBtn")
        self.apptimersBtn.setGeometry(QRect(30, 350, 271, 75))
        self.label = QLabel(self.central)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(485, 190, 271, 50))
        self.label.setStyleSheet(u"QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"	font-size: 35px;\n"
"    font-family: 'Inter';\n"
"}\n"
"")
        self.label.setLineWidth(2)
        self.Applications = QLabel(self.central)
        self.Applications.setObjectName(u"Applications")
        self.Applications.setGeometry(QRect(440, 390, 884, 31))
        self.Applications.setStyleSheet(u"QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"	font-family: 'Inter';\n"
"    background-color: rgba(33, 22, 74, 0);\n"
"	font-size: 16px\n"
"}\n"
"")
        self.AppScrollArea = QScrollArea(self.central)
        self.AppScrollArea.setObjectName(u"AppScrollArea")
        self.AppScrollArea.setGeometry(QRect(440, 429, 841, 551))
        self.AppScrollArea.setStyleSheet(u"QScrollArea {\n"
"    background-color: rgba(120, 255, 90,0);\n"
"}")
        self.AppScrollArea.setWidgetResizable(True)
        self.AppScrollWidget = QWidget()
        self.AppScrollWidget.setObjectName(u"AppScrollWidget")
        self.AppScrollWidget.setGeometry(QRect(0, 0, 839, 549))
        self.AppScrollWidget.setStyleSheet(u"QWidget {\n"
"    background-color: rgba(0, 0, 0,0);\n"
"}")
        self.AppScrollArea.setWidget(self.AppScrollWidget)
        self.AppsMonitored = QLabel(self.central)
        self.AppsMonitored.setObjectName(u"AppsMonitored")
        self.AppsMonitored.setGeometry(QRect(1000, 190, 271, 50))
        self.AppsMonitored.setStyleSheet(u"QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"	font-size: 35px;\n"
"    font-family: 'Inter';\n"
"}\n"
"")
        self.AppsMonitored.setLineWidth(2)
        self.MostUsedApp = QLabel(self.central)
        self.MostUsedApp.setObjectName(u"MostUsedApp")
        self.MostUsedApp.setGeometry(QRect(1515, 190, 271, 50))
        self.MostUsedApp.setStyleSheet(u"QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"	font-size: 35px;\n"
"    font-family: 'Inter';\n"
"}\n"
"")
        self.MostUsedApp.setLineWidth(2)
        self.MostScrollArea = QScrollArea(self.central)
        self.MostScrollArea.setObjectName(u"MostScrollArea")
        self.MostScrollArea.setGeometry(QRect(1440, 429, 391, 551))
        self.MostScrollArea.setStyleSheet(u"QScrollArea {\n"
"    background-color: rgba(120, 255, 90,0);\n"
"}")
        self.MostScrollArea.setWidgetResizable(True)
        self.AppScrollWidget_2 = QWidget()
        self.AppScrollWidget_2.setObjectName(u"AppScrollWidget_2")
        self.AppScrollWidget_2.setGeometry(QRect(0, 0, 389, 549))
        self.AppScrollWidget_2.setStyleSheet(u"QWidget {\n"
"    background-color: rgba(0, 0, 0,0);\n"
"}")
        self.MostScrollArea.setWidget(self.AppScrollWidget_2)
        self.ApplicationsTime = QLabel(self.central)
        self.ApplicationsTime.setObjectName(u"ApplicationsTime")
        self.ApplicationsTime.setGeometry(QRect(1440, 390, 381, 31))
        self.ApplicationsTime.setStyleSheet(u"QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"	font-family: 'Inter';\n"
"    background-color: rgba(33, 22, 74, 0);\n"
"	font-size: 16px\n"
"}\n"
"")
        self.WidgetDashboard = QWidget(self.central)
        self.WidgetDashboard.setObjectName(u"WidgetDashboard")
        self.WidgetDashboard.setGeometry(QRect(30, 190, 271, 75))
        self.WidgetDashboard.setStyleSheet(u"")
        self.dashboardBtn = QPushButton(self.WidgetDashboard)
        self.dashboardBtn.setObjectName(u"dashboardBtn")
        self.dashboardBtn.setGeometry(QRect(0, 0, 271, 75))
        self.title = QLabel(self.WidgetDashboard)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(50, 20, 111, 19))
        self.title.setStyleSheet(u"QLabel {\n"
"    color: rgb(92, 93, 126);\n"
"	font-size: 18px;\n"
"    font-family: 'Inter';\n"
"}")
        self.subtitle = QLabel(self.WidgetDashboard)
        self.subtitle.setObjectName(u"subtitle")
        self.subtitle.setGeometry(QRect(50, 40, 87, 19))
        self.subtitle.setStyleSheet(u"QLabel {\n"
"    color: rgb(92, 93, 126);\n"
"	font-size: 13px;\n"
"    font-family: 'Inter';\n"
"}")
        self.icon = QLabel(self.WidgetDashboard)
        self.icon.setObjectName(u"icon")
        self.icon.setGeometry(QRect(0, 17, 41, 41))
        self.icon.setStyleSheet(u"")
        self.icon.setPixmap(QPixmap(u"chart-column-solid-full.svg"))
        self.icon.setScaledContents(True)
        MainWindow.setCentralWidget(self.central)
        self.Dashboard.raise_()
        self.reportsBtn.raise_()
        self.apptimersBtn.raise_()
        self.label.raise_()
        self.MostUsedApp.raise_()
        self.MostScrollArea.raise_()
        self.AppScrollArea.raise_()
        self.Applications.raise_()
        self.ApplicationsTime.raise_()
        self.AppsMonitored.raise_()
        self.WidgetDashboard.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Dashboard.setText("")
        self.reportsBtn.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.apptimersBtn.setText(QCoreApplication.translate("MainWindow", u"App Timers", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Loading", None))
        self.Applications.setText(QCoreApplication.translate("MainWindow", u"   Application                                                                                                                       Today", None))
        self.AppsMonitored.setText(QCoreApplication.translate("MainWindow", u"Loading", None))
        self.MostUsedApp.setText(QCoreApplication.translate("MainWindow", u"Loading", None))
        self.ApplicationsTime.setText(QCoreApplication.translate("MainWindow", u"   Application                                         All Time", None))
        self.dashboardBtn.setText("")
        self.title.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.subtitle.setText(QCoreApplication.translate("MainWindow", u"Overview", None))
        self.icon.setText("")
    # retranslateUi

