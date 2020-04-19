# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Timer_Window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(830, 502)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.widget = AnalogGaugeWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(350, 350))
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 75))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 1, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(1, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setMinimumSize(QtCore.QSize(200, 40))
        self.label.setMaximumSize(QtCore.QSize(200, 40))
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.names = QtWidgets.QWidget()
        self.names.setObjectName("names")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.names)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_openfile = QtWidgets.QPushButton(self.names)
        self.pushButton_openfile.setObjectName("pushButton_openfile")
        self.gridLayout_3.addWidget(self.pushButton_openfile, 1, 0, 1, 1)
        self.pushButton_clear = QtWidgets.QPushButton(self.names)
        self.pushButton_clear.setMaximumSize(QtCore.QSize(16000000, 16777215))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.gridLayout_3.addWidget(self.pushButton_clear, 1, 1, 1, 1)
        self.name_list = QtWidgets.QListWidget(self.names)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.name_list.setFont(font)
        self.name_list.setObjectName("name_list")
        self.gridLayout_3.addWidget(self.name_list, 0, 0, 1, 2)
        self.tabWidget.addTab(self.names, "")
        self.clear = QtWidgets.QWidget()
        self.clear.setObjectName("clear")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.clear)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget.addTab(self.clear, "")
        self.gridLayout_4.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 830, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.label.setText(_translate("MainWindow", "label"))
        self.pushButton_openfile.setText(_translate("MainWindow", "Open File"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear List"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.names), _translate("MainWindow", "Names"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.clear), _translate("MainWindow", "Clear"))

from analoggaugewidget import AnalogGaugeWidget
