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
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet(u"#central QPushButton {\n"
"    color: rgb(183, 183, 183);\n"
"    background-color: rgb(33, 22, 74);\n"
"    border: 1px solid rgb(33, 22, 74);\n"
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
        self.Dashboard.setPixmap(QPixmap(u"Downloads/Dashboard.png"))
        self.dashboardBtn = QPushButton(self.central)
        self.dashboardBtn.setObjectName(u"dashboardBtn")
        self.dashboardBtn.setGeometry(QRect(30, 190, 271, 75))
        self.reportsBtn = QPushButton(self.central)
        self.reportsBtn.setObjectName(u"reportsBtn")
        self.reportsBtn.setGeometry(QRect(30, 270, 271, 75))
        self.apptimersBtn = QPushButton(self.central)
        self.apptimersBtn.setObjectName(u"apptimersBtn")
        self.apptimersBtn.setGeometry(QRect(30, 350, 271, 75))
        self.label = QLabel(self.central)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(485, 185, 271, 50))
        self.label.setStyleSheet(u"QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"	font-size: 35px;\n"
"    font-family: 'Inter';\n"
"}\n"
"")
        self.label.setLineWidth(2)
        self.Applications = QLabel(self.central)
        self.Applications.setObjectName(u"Applications")
        self.Applications.setGeometry(QRect(407, 330, 884, 31))
        self.Applications.setStyleSheet(u"QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"	font-family: 'Inter';\n"
"    background-color: rgba(33, 22, 74, 0);\n"
"	font-size: 16px\n"
"}\n"
"")
        self.AppScrollArea = QScrollArea(self.central)
        self.AppScrollArea.setObjectName(u"AppScrollArea")
        self.AppScrollArea.setGeometry(QRect(400, 360, 911, 621))
        self.AppScrollArea.setStyleSheet(u"QScrollArea {\n"
"    background-color: rgba(120, 255, 90,0);\n"
"}")
        self.AppScrollArea.setWidgetResizable(True)
        self.AppScrollWidget = QWidget()
        self.AppScrollWidget.setObjectName(u"AppScrollWidget")
        self.AppScrollWidget.setGeometry(QRect(0, 0, 909, 619))
        self.AppScrollWidget.setStyleSheet(u"QWidget {\n"
"    background-color: rgba(0, 0, 0,0);\n"
"}")
        self.AppScrollArea.setWidget(self.AppScrollWidget)
        self.AppsMonitored = QLabel(self.central)
        self.AppsMonitored.setObjectName(u"AppsMonitored")
        self.AppsMonitored.setGeometry(QRect(1000, 185, 271, 50))
        self.AppsMonitored.setStyleSheet(u"QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"	font-size: 35px;\n"
"    font-family: 'Inter';\n"
"}\n"
"")
        self.AppsMonitored.setLineWidth(2)
        self.MostUsedApp = QLabel(self.central)
        self.MostUsedApp.setObjectName(u"MostUsedApp")
        self.MostUsedApp.setGeometry(QRect(1515, 185, 271, 50))
        self.MostUsedApp.setStyleSheet(u"QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"	font-size: 35px;\n"
"    font-family: 'Inter';\n"
"}\n"
"")
        self.MostUsedApp.setLineWidth(2)
        self.MostScrollArea = QScrollArea(self.central)
        self.MostScrollArea.setObjectName(u"MostScrollArea")
        self.MostScrollArea.setGeometry(QRect(1440, 360, 391, 621))
        self.MostScrollArea.setStyleSheet(u"QScrollArea {\n"
"    background-color: rgba(120, 255, 90,0);\n"
"}")
        self.MostScrollArea.setWidgetResizable(True)
        self.AppScrollWidget_2 = QWidget()
        self.AppScrollWidget_2.setObjectName(u"AppScrollWidget_2")
        self.AppScrollWidget_2.setGeometry(QRect(0, 0, 389, 619))
        self.AppScrollWidget_2.setStyleSheet(u"QWidget {\n"
"    background-color: rgba(0, 0, 0,0);\n"
"}")
        self.MostScrollArea.setWidget(self.AppScrollWidget_2)
        self.ApplicationsTime = QLabel(self.central)
        self.ApplicationsTime.setObjectName(u"ApplicationsTime")
        self.ApplicationsTime.setGeometry(QRect(1440, 330, 381, 31))
        self.ApplicationsTime.setStyleSheet(u"QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"	font-family: 'Inter';\n"
"    background-color: rgba(33, 22, 74, 0);\n"
"	font-size: 16px\n"
"}\n"
"")
        MainWindow.setCentralWidget(self.central)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Dashboard.setText("")
        self.dashboardBtn.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.reportsBtn.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.apptimersBtn.setText(QCoreApplication.translate("MainWindow", u"App Timers", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Loading", None))
        self.Applications.setText(QCoreApplication.translate("MainWindow", u"   Application                                                                                                                                                                    Today", None))
        self.AppsMonitored.setText(QCoreApplication.translate("MainWindow", u"Loading", None))
        self.MostUsedApp.setText(QCoreApplication.translate("MainWindow", u"Loading", None))
        self.ApplicationsTime.setText(QCoreApplication.translate("MainWindow", u"Application                                           All Time", None))
    # retranslateUi

