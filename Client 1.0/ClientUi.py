# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import socket
import random
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Client(object):
    def setupUi(self, Client):
        Client.setObjectName("Client")
        Client.resize(845, 480)
        Client.setMinimumSize(QtCore.QSize(845, 480))
        Client.setMaximumSize(QtCore.QSize(845, 480))
        Client.setDocumentMode(False)
        self.MainWindow = QtWidgets.QWidget(Client)
        self.MainWindow.setObjectName("MainWindow")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.MainWindow)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(550, 10, 291, 381))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.Rmenu = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.Rmenu.setContentsMargins(0, 0, 0, 0)
        self.Rmenu.setObjectName("Rmenu")
        self.SettingsBox = QtWidgets.QTabWidget(self.verticalLayoutWidget_3)
        self.SettingsBox.setObjectName("SettingsBox")
        self.ClientTab = QtWidgets.QWidget()
        self.ClientTab.setObjectName("ClientTab")
        self.cSettings = QtWidgets.QGroupBox(self.ClientTab)
        self.cSettings.setGeometry(QtCore.QRect(10, 10, 261, 331))
        self.cSettings.setObjectName("cSettings")
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.cSettings)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(10, 20, 241, 61))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.cNameLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.cNameLayout.setContentsMargins(0, 0, 0, 0)
        self.cNameLayout.setObjectName("cNameLayout")
        self.cNameGroup = QtWidgets.QGroupBox(self.verticalLayoutWidget_10)
        self.cNameGroup.setObjectName("cNameGroup")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.cNameGroup)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(10, 20, 221, 31))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.cCustomName = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.cCustomName.setContentsMargins(0, 0, 0, 0)
        self.cCustomName.setObjectName("cCustomName")
        self.cNameLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.cNameLabel.setObjectName("cNameLabel")
        self.cCustomName.addWidget(self.cNameLabel)
        self.cName = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.cName.setClearButtonEnabled(True)
        self.cName.setObjectName("cName")
        self.cCustomName.addWidget(self.cName)
        self.cNameLayout.addWidget(self.cNameGroup)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.cSettings)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(10, 160, 241, 91))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.cConnectLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.cConnectLayout.setContentsMargins(0, 0, 0, 0)
        self.cConnectLayout.setObjectName("cConnectLayout")
        self.cConnectGroup = QtWidgets.QGroupBox(self.verticalLayoutWidget_8)
        self.cConnectGroup.setObjectName("cConnectGroup")
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(self.cConnectGroup)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(10, 20, 221, 61))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.cConnectToLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.cConnectToLayout.setContentsMargins(0, 0, 0, 0)
        self.cConnectToLayout.setObjectName("cConnectToLayout")
        self.cIpLayout = QtWidgets.QHBoxLayout()
        self.cIpLayout.setObjectName("cIpLayout")
        self.cIPv4Label = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        self.cIPv4Label.setObjectName("cIPv4Label")
        self.cIpLayout.addWidget(self.cIPv4Label)
        self.cIPv4 = QtWidgets.QLineEdit(self.verticalLayoutWidget_11)
        self.cIPv4.setMaxLength(16)
        self.cIPv4.setClearButtonEnabled(True)
        self.cIPv4.setObjectName("cIPv4")
        self.cIpLayout.addWidget(self.cIPv4)
        self.cConnectToLayout.addLayout(self.cIpLayout)
        self.cDecorLine = QtWidgets.QFrame(self.verticalLayoutWidget_11)
        self.cDecorLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.cDecorLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.cDecorLine.setObjectName("cDecorLine")
        self.cConnectToLayout.addWidget(self.cDecorLine)
        self.CPortLayout = QtWidgets.QHBoxLayout()
        self.CPortLayout.setObjectName("CPortLayout")
        self.cPortLabel = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        self.cPortLabel.setObjectName("cPortLabel")
        self.CPortLayout.addWidget(self.cPortLabel)
        self.cPort = QtWidgets.QLineEdit(self.verticalLayoutWidget_11)
        self.cPort.setMaxLength(5)
        self.cPort.setFrame(True)
        self.cPort.setClearButtonEnabled(True)
        self.cPort.setObjectName("cPort")
        self.CPortLayout.addWidget(self.cPort)
        self.cConnectToLayout.addLayout(self.CPortLayout)
        self.cConnectLayout.addWidget(self.cConnectGroup)
        self.verticalLayoutWidget_12 = QtWidgets.QWidget(self.cSettings)
        self.verticalLayoutWidget_12.setGeometry(QtCore.QRect(10, 260, 241, 61))
        self.verticalLayoutWidget_12.setObjectName("verticalLayoutWidget_12")
        self.cControlLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_12)
        self.cControlLayout.setContentsMargins(0, 0, 0, 0)
        self.cControlLayout.setObjectName("cControlLayout")
        self.cControlGroup = QtWidgets.QGroupBox(self.verticalLayoutWidget_12)
        self.cControlGroup.setObjectName("cControlGroup")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.cControlGroup)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 20, 221, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.cControlButton = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.cControlButton.setContentsMargins(0, 0, 0, 0)
        self.cControlButton.setObjectName("cControlButton")
        self.JoinButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.JoinButton.setObjectName("JoinButton")
        self.cControlButton.addWidget(self.JoinButton)
        self.LeaveButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.LeaveButton.setObjectName("LeaveButton")
        self.cControlButton.addWidget(self.LeaveButton)
        self.cControlLayout.addWidget(self.cControlGroup)
        self.verticalLayoutWidget_13 = QtWidgets.QWidget(self.cSettings)
        self.verticalLayoutWidget_13.setGeometry(QtCore.QRect(10, 90, 241, 61))
        self.verticalLayoutWidget_13.setObjectName("verticalLayoutWidget_13")
        self.cLocalPortLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_13)
        self.cLocalPortLayout.setContentsMargins(0, 0, 0, 0)
        self.cLocalPortLayout.setObjectName("cLocalPortLayout")
        self.cLocalPortGroup = QtWidgets.QGroupBox(self.verticalLayoutWidget_13)
        self.cLocalPortGroup.setObjectName("cLocalPortGroup")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.cLocalPortGroup)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 221, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.cLocalPortEdit = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.cLocalPortEdit.setContentsMargins(0, 0, 0, 0)
        self.cLocalPortEdit.setObjectName("cLocalPortEdit")
        self.cLocalPort = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.cLocalPort.setObjectName("cLocalPort")
        self.cLocalPortEdit.addWidget(self.cLocalPort)
        self.RandomButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.RandomButton.setObjectName("RandomButton")
        self.cLocalPortEdit.addWidget(self.RandomButton)
        self.cLocalPortLayout.addWidget(self.cLocalPortGroup)
        self.SettingsBox.addTab(self.ClientTab, "")
        self.ServerTab = QtWidgets.QWidget()
        self.ServerTab.setObjectName("ServerTab")
        self.sSettings = QtWidgets.QGroupBox(self.ServerTab)
        self.sSettings.setGeometry(QtCore.QRect(10, 10, 261, 331))
        self.sSettings.setObjectName("sSettings")
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.sSettings)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(10, 20, 241, 61))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.sNameLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.sNameLayout.setContentsMargins(0, 0, 0, 0)
        self.sNameLayout.setObjectName("sNameLayout")
        self.sNameGroup = QtWidgets.QGroupBox(self.verticalLayoutWidget_9)
        self.sNameGroup.setObjectName("sNameGroup")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.sNameGroup)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 20, 221, 31))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.sCustomName = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.sCustomName.setContentsMargins(0, 0, 0, 0)
        self.sCustomName.setObjectName("sCustomName")
        self.sNameLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.sNameLabel.setObjectName("sNameLabel")
        self.sCustomName.addWidget(self.sNameLabel)
        self.sName = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        self.sName.setClearButtonEnabled(True)
        self.sName.setObjectName("sName")
        self.sCustomName.addWidget(self.sName)
        self.sNameLayout.addWidget(self.sNameGroup)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.sSettings)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 90, 241, 91))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.sConnectLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.sConnectLayout.setContentsMargins(0, 0, 0, 0)
        self.sConnectLayout.setObjectName("sConnectLayout")
        self.sConnectGroup = QtWidgets.QGroupBox(self.verticalLayoutWidget_5)
        self.sConnectGroup.setObjectName("sConnectGroup")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.sConnectGroup)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 221, 61))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.sConnectToLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.sConnectToLayout.setContentsMargins(0, 0, 0, 0)
        self.sConnectToLayout.setObjectName("sConnectToLayout")
        self.sIpLayout = QtWidgets.QHBoxLayout()
        self.sIpLayout.setObjectName("sIpLayout")
        self.sIPv4Label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.sIPv4Label.setObjectName("sIPv4Label")
        self.sIpLayout.addWidget(self.sIPv4Label)
        self.sIPv4 = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.sIPv4.setMaxLength(16)
        self.sIPv4.setClearButtonEnabled(True)
        self.sIPv4.setObjectName("sIPv4")
        self.sIpLayout.addWidget(self.sIPv4)
        self.sConnectToLayout.addLayout(self.sIpLayout)
        self.sDercorLine = QtWidgets.QFrame(self.verticalLayoutWidget_4)
        self.sDercorLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.sDercorLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.sDercorLine.setObjectName("sDercorLine")
        self.sConnectToLayout.addWidget(self.sDercorLine)
        self.sPortLayout = QtWidgets.QHBoxLayout()
        self.sPortLayout.setObjectName("sPortLayout")
        self.sPortLabel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.sPortLabel.setObjectName("sPortLabel")
        self.sPortLayout.addWidget(self.sPortLabel)
        self.sPort = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.sPort.setMaxLength(5)
        self.sPort.setFrame(True)
        self.sPort.setClearButtonEnabled(True)
        self.sPort.setObjectName("sPort")
        self.sPortLayout.addWidget(self.sPort)
        self.sConnectToLayout.addLayout(self.sPortLayout)
        self.sConnectLayout.addWidget(self.sConnectGroup)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.sSettings)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(10, 190, 241, 61))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.sMaxConnectionLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.sMaxConnectionLayout.setContentsMargins(0, 0, 0, 0)
        self.sMaxConnectionLayout.setObjectName("sMaxConnectionLayout")
        self.sMaxConnectGroup = QtWidgets.QGroupBox(self.verticalLayoutWidget_6)
        self.sMaxConnectGroup.setObjectName("sMaxConnectGroup")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.sMaxConnectGroup)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 221, 33))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.sNumberLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.sNumberLayout.setContentsMargins(0, 0, 0, 0)
        self.sNumberLayout.setObjectName("sNumberLayout")
        self.sMinusButton = QtWidgets.QToolButton(self.horizontalLayoutWidget_3)
        self.sMinusButton.setMinimumSize(QtCore.QSize(31, 31))
        self.sMinusButton.setObjectName("sMinusButton")
        self.sNumberLayout.addWidget(self.sMinusButton)
        self.sNumber = QtWidgets.QLCDNumber(self.horizontalLayoutWidget_3)
        self.sNumber.setDigitCount(2)
        self.sNumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.sNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.sNumber.setProperty("intValue", 1)
        self.sNumber.setObjectName("sNumber")
        self.sNumberLayout.addWidget(self.sNumber)
        self.sPlusButton = QtWidgets.QToolButton(self.horizontalLayoutWidget_3)
        self.sPlusButton.setMinimumSize(QtCore.QSize(31, 31))
        self.sPlusButton.setObjectName("sPlusButton")
        self.sNumberLayout.addWidget(self.sPlusButton)
        self.sMaxConnectionLayout.addWidget(self.sMaxConnectGroup)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.sSettings)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(10, 260, 241, 61))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.sControlLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.sControlLayout.setContentsMargins(0, 0, 0, 0)
        self.sControlLayout.setObjectName("sControlLayout")
        self.sControlButton = QtWidgets.QGroupBox(self.verticalLayoutWidget_7)
        self.sControlButton.setObjectName("sControlButton")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.sControlButton)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 221, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.sControlButtons = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.sControlButtons.setContentsMargins(0, 0, 0, 0)
        self.sControlButtons.setObjectName("sControlButtons")
        self.StartButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.StartButton.setObjectName("StartButton")
        self.sControlButtons.addWidget(self.StartButton)
        self.StopButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.StopButton.setObjectName("StopButton")
        self.sControlButtons.addWidget(self.StopButton)
        self.sControlLayout.addWidget(self.sControlButton)
        self.SettingsBox.addTab(self.ServerTab, "")
        self.Rmenu.addWidget(self.SettingsBox)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.MainWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 531, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.Lmenu = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.Lmenu.setContentsMargins(0, 0, 0, 0)
        self.Lmenu.setObjectName("Lmenu")
        self.Chat = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.Chat.setAcceptDrops(False)
        self.Chat.setObjectName("Chat")
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.Chat)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(10, 390, 511, 41))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.SendingBox = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.SendingBox.setContentsMargins(0, 0, 0, 0)
        self.SendingBox.setObjectName("SendingBox")
        self.SendLine = QtWidgets.QLineEdit(self.horizontalLayoutWidget_8)
        self.SendLine.setObjectName("SendLine")
        self.SendingBox.addWidget(self.SendLine)
        self.SendButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_8)
        self.SendButton.setObjectName("SendButton")
        self.SendingBox.addWidget(self.SendButton)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Chat)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 511, 361))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.DisplayBox = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.DisplayBox.setContentsMargins(0, 0, 0, 0)
        self.DisplayBox.setObjectName("DisplayBox")
        self.Display = QtWidgets.QTextBrowser(self.verticalLayoutWidget_2)
        self.Display.setObjectName("Display")
        self.DisplayBox.addWidget(self.Display)
        self.Lmenu.addWidget(self.Chat)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.MainWindow)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(550, 400, 291, 51))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.Dmenu = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.Dmenu.setContentsMargins(0, 0, 0, 0)
        self.Dmenu.setObjectName("Dmenu")
        self.SelectLanguage = QtWidgets.QGroupBox(self.horizontalLayoutWidget_9)
        self.SelectLanguage.setObjectName("SelectLanguage")
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.SelectLanguage)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(10, 20, 271, 25))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.ButtonBox = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.ButtonBox.setContentsMargins(0, 0, 0, 0)
        self.ButtonBox.setObjectName("ButtonBox")
        self.SelectRussian = QtWidgets.QPushButton(self.horizontalLayoutWidget_10)
        self.SelectRussian.setObjectName("SelectRussian")
        self.ButtonBox.addWidget(self.SelectRussian)
        self.SelectEnglish = QtWidgets.QPushButton(self.horizontalLayoutWidget_10)
        self.SelectEnglish.setObjectName("SelectEnglish")
        self.ButtonBox.addWidget(self.SelectEnglish)
        self.Dmenu.addWidget(self.SelectLanguage)
        Client.setCentralWidget(self.MainWindow)
        self.statusbar = QtWidgets.QStatusBar(Client)
        self.statusbar.setEnabled(False)
        self.statusbar.setObjectName("statusbar")
        Client.setStatusBar(self.statusbar)
        self.retranslateUi(Client)
        self.SettingsBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Client)

    def retranslateUi(self, Client):
        _translate = QtCore.QCoreApplication.translate
        Client.setWindowTitle(_translate("Client", "PyChat"))
        self.cSettings.setTitle(_translate("Client", "Client settings"))
        self.cNameGroup.setTitle(_translate("Client", "Your name"))
        self.cNameLabel.setText(_translate("Client", "Name:"))
        self.cName.setText(_translate("Client", "User"))
        self.cConnectGroup.setTitle(_translate("Client", "Connect to"))
        self.cIPv4Label.setText(_translate("Client", "IPv4:"))
        self.cIPv4.setText(_translate("Client", "{}".format(socket.gethostbyname(socket.gethostname()))))
        self.cPortLabel.setText(_translate("Client", "PORT:"))
        self.cPort.setText(_translate("Client", "9090"))
        self.cLocalPort.setText(_translate("Client", "{}".format(random.randint(10000, 30000))))
        self.cControlGroup.setTitle(_translate("Client", "Control Buttons"))
        self.JoinButton.setText(_translate("Client", "Join"))
        self.LeaveButton.setText(_translate("Client", "Leave"))
        self.cLocalPortGroup.setTitle(_translate("Client", "Your ID"))
        self.RandomButton.setText(_translate("Client", "Random"))
        self.SettingsBox.setTabText(self.SettingsBox.indexOf(self.ClientTab), _translate("Client", "Client"))
        self.sSettings.setTitle(_translate("Client", "Server settings"))
        self.sNameGroup.setTitle(_translate("Client", "Your name"))
        self.sNameLabel.setText(_translate("Client", "Name:"))
        self.sName.setText(_translate("Client", "User"))
        self.sConnectGroup.setTitle(_translate("Client", "Host"))
        self.sIPv4Label.setText(_translate("Client", "IPv4:"))
        self.sIPv4.setText(_translate("Client", "{}".format(socket.gethostbyname(socket.gethostname()))))
        self.sPortLabel.setText(_translate("Client", "PORT:"))
        self.sPort.setText(_translate("Client", "9090"))
        self.sMaxConnectGroup.setTitle(_translate("Client", "Max connections"))
        self.sMinusButton.setText(_translate("Client", "<"))
        self.sPlusButton.setText(_translate("Client", ">"))
        self.sControlButton.setTitle(_translate("Client", "Control Buttons"))
        self.StartButton.setText(_translate("Client", "Start"))
        self.StopButton.setText(_translate("Client", "Stop"))
        self.SettingsBox.setTabText(self.SettingsBox.indexOf(self.ServerTab), _translate("Client", "Server"))
        self.Chat.setTitle(_translate("Client", "Chat"))
        self.SendButton.setText(_translate("Client", "Send"))
        self.SelectLanguage.setTitle(_translate("Client", "Select language"))
        self.SelectRussian.setText(_translate("Client", "Русский"))
        self.SelectEnglish.setText(_translate("Client", "English"))

    def ru_translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.cSettings.setTitle(_translate("Client", "Настройки клиента"))
        self.cNameGroup.setTitle(_translate("Client", "Твоё имя"))
        self.cNameLabel.setText(_translate("Client", "Имя:"))
        self.cName.setText(_translate("Client", "Пользователь"))
        self.cConnectGroup.setTitle(_translate("Client", "Подключиться к"))
        self.cControlGroup.setTitle(_translate("Client", "Кнопки управления"))
        self.JoinButton.setText(_translate("Client", "Присоединиться"))
        self.LeaveButton.setText(_translate("Client", "Покинуть"))
        self.cLocalPortGroup.setTitle(_translate("Client", "Твой ID"))
        self.RandomButton.setText(_translate("Client", "Случайно"))
        self.SettingsBox.setTabText(self.SettingsBox.indexOf(self.ClientTab), _translate("Client", "Клиент"))
        self.sSettings.setTitle(_translate("Client", "Настройки сервера"))
        self.sNameGroup.setTitle(_translate("Client", "Твоё имя"))
        self.sNameLabel.setText(_translate("Client", "Имя:"))
        self.sName.setText(_translate("Client", "Пользователь"))
        self.sConnectGroup.setTitle(_translate("Client", "Сервер"))
        self.sMaxConnectGroup.setTitle(_translate("Client", "Кол-во людей"))
        self.sControlButton.setTitle(_translate("Client", "Кнопки управления"))
        self.StartButton.setText(_translate("Client", "ВКЛ"))
        self.StopButton.setText(_translate("Client", "ВЫКЛ"))
        self.SettingsBox.setTabText(self.SettingsBox.indexOf(self.ServerTab), _translate("Client", "Сервер"))
        self.Chat.setTitle(_translate("Client", "Чат"))
        self.SendButton.setText(_translate("Client", "Отправить"))
        self.SelectLanguage.setTitle(_translate("Client", "Выбор языка"))

    def en_translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.cSettings.setTitle(_translate("Client", "Client settings"))
        self.cNameGroup.setTitle(_translate("Client", "Your name"))
        self.cNameLabel.setText(_translate("Client", "Name:"))
        self.cName.setText(_translate("Client", "User"))
        self.cConnectGroup.setTitle(_translate("Client", "Connect to"))
        self.cControlGroup.setTitle(_translate("Client", "Control Buttons"))
        self.JoinButton.setText(_translate("Client", "Join"))
        self.LeaveButton.setText(_translate("Client", "Leave"))
        self.cLocalPortGroup.setTitle(_translate("Client", "Your ID"))
        self.RandomButton.setText(_translate("Client", "Random"))
        self.SettingsBox.setTabText(self.SettingsBox.indexOf(self.ClientTab), _translate("Client", "Client"))
        self.sSettings.setTitle(_translate("Client", "Server settings"))
        self.sNameGroup.setTitle(_translate("Client", "Your name"))
        self.sNameLabel.setText(_translate("Client", "Name:"))
        self.sName.setText(_translate("Client", "User"))
        self.sConnectGroup.setTitle(_translate("Client", "Host"))
        self.sMaxConnectGroup.setTitle(_translate("Client", "Max connections"))
        self.sControlButton.setTitle(_translate("Client", "Control Buttons"))
        self.StartButton.setText(_translate("Client", "Start"))
        self.StopButton.setText(_translate("Client", "Stop"))
        self.SettingsBox.setTabText(self.SettingsBox.indexOf(self.ServerTab), _translate("Client", "Server"))
        self.Chat.setTitle(_translate("Client", "Chat"))
        self.SendButton.setText(_translate("Client", "Send"))
        self.SelectLanguage.setTitle(_translate("Client", "Select language"))
