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
        self.Dashboard.setPixmap(QPixmap(u"Dashboard.png"))
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
"}\n"
"")
        self.label.setLineWidth(2)
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
    # retranslateUi

