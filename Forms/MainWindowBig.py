# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowBig.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(698, 610)
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(220, 20, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(24)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.export_button = QtWidgets.QPushButton(self.centralwidget)
        self.export_button.setGeometry(QtCore.QRect(380, 490, 121, 28))
        self.export_button.setObjectName("export_button")
        self.additional_tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.additional_tabs.setGeometry(QtCore.QRect(10, 90, 671, 371))
        self.additional_tabs.setObjectName("additional_tabs")
        self.sys_tab = QtWidgets.QWidget()
        self.sys_tab.setObjectName("sys_tab")
        self.system_win_1 = QtWidgets.QPushButton(self.sys_tab)
        self.system_win_1.setGeometry(QtCore.QRect(160, 25, 161, 31))
        self.system_win_1.setObjectName("system_win_1")
        self.system_bar_1 = QtWidgets.QProgressBar(self.sys_tab)
        self.system_bar_1.setGeometry(QtCore.QRect(340, 30, 118, 23))
        self.system_bar_1.setMaximum(8)
        self.system_bar_1.setProperty("value", 0)
        self.system_bar_1.setTextVisible(True)
        self.system_bar_1.setInvertedAppearance(False)
        self.system_bar_1.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.system_bar_1.setObjectName("system_bar_1")
        self.system_bar_2 = QtWidgets.QProgressBar(self.sys_tab)
        self.system_bar_2.setGeometry(QtCore.QRect(340, 70, 118, 23))
        self.system_bar_2.setMaximum(8)
        self.system_bar_2.setProperty("value", 0)
        self.system_bar_2.setTextVisible(True)
        self.system_bar_2.setInvertedAppearance(False)
        self.system_bar_2.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.system_bar_2.setObjectName("system_bar_2")
        self.system_win_2 = QtWidgets.QPushButton(self.sys_tab)
        self.system_win_2.setGeometry(QtCore.QRect(160, 65, 161, 31))
        self.system_win_2.setObjectName("system_win_2")
        self.system_bar_3 = QtWidgets.QProgressBar(self.sys_tab)
        self.system_bar_3.setGeometry(QtCore.QRect(340, 110, 118, 23))
        self.system_bar_3.setMaximum(8)
        self.system_bar_3.setProperty("value", 0)
        self.system_bar_3.setTextVisible(True)
        self.system_bar_3.setInvertedAppearance(False)
        self.system_bar_3.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.system_bar_3.setObjectName("system_bar_3")
        self.system_win_3 = QtWidgets.QPushButton(self.sys_tab)
        self.system_win_3.setGeometry(QtCore.QRect(160, 105, 161, 31))
        self.system_win_3.setObjectName("system_win_3")
        self.system_bar_4 = QtWidgets.QProgressBar(self.sys_tab)
        self.system_bar_4.setGeometry(QtCore.QRect(340, 150, 118, 23))
        self.system_bar_4.setMaximum(8)
        self.system_bar_4.setProperty("value", 0)
        self.system_bar_4.setTextVisible(True)
        self.system_bar_4.setInvertedAppearance(False)
        self.system_bar_4.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.system_bar_4.setObjectName("system_bar_4")
        self.system_win_4 = QtWidgets.QPushButton(self.sys_tab)
        self.system_win_4.setGeometry(QtCore.QRect(160, 145, 161, 31))
        self.system_win_4.setObjectName("system_win_4")
        self.system_bar_5 = QtWidgets.QProgressBar(self.sys_tab)
        self.system_bar_5.setGeometry(QtCore.QRect(340, 190, 118, 23))
        self.system_bar_5.setMaximum(8)
        self.system_bar_5.setProperty("value", 0)
        self.system_bar_5.setTextVisible(True)
        self.system_bar_5.setInvertedAppearance(False)
        self.system_bar_5.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.system_bar_5.setObjectName("system_bar_5")
        self.system_win_5 = QtWidgets.QPushButton(self.sys_tab)
        self.system_win_5.setGeometry(QtCore.QRect(160, 185, 161, 31))
        self.system_win_5.setObjectName("system_win_5")
        self.system_bar_6 = QtWidgets.QProgressBar(self.sys_tab)
        self.system_bar_6.setGeometry(QtCore.QRect(340, 230, 118, 23))
        self.system_bar_6.setMaximum(8)
        self.system_bar_6.setProperty("value", 0)
        self.system_bar_6.setTextVisible(True)
        self.system_bar_6.setInvertedAppearance(False)
        self.system_bar_6.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.system_bar_6.setObjectName("system_bar_6")
        self.system_win_6 = QtWidgets.QPushButton(self.sys_tab)
        self.system_win_6.setGeometry(QtCore.QRect(160, 225, 161, 31))
        self.system_win_6.setObjectName("system_win_6")
        self.system_bar_7 = QtWidgets.QProgressBar(self.sys_tab)
        self.system_bar_7.setGeometry(QtCore.QRect(340, 265, 118, 23))
        self.system_bar_7.setMaximum(8)
        self.system_bar_7.setProperty("value", 0)
        self.system_bar_7.setTextVisible(True)
        self.system_bar_7.setInvertedAppearance(False)
        self.system_bar_7.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.system_bar_7.setObjectName("system_bar_7")
        self.system_win_7 = QtWidgets.QPushButton(self.sys_tab)
        self.system_win_7.setGeometry(QtCore.QRect(160, 260, 161, 31))
        self.system_win_7.setObjectName("system_win_7")
        self.system_bar_8 = QtWidgets.QProgressBar(self.sys_tab)
        self.system_bar_8.setGeometry(QtCore.QRect(340, 305, 118, 23))
        self.system_bar_8.setMaximum(8)
        self.system_bar_8.setProperty("value", 0)
        self.system_bar_8.setTextVisible(True)
        self.system_bar_8.setInvertedAppearance(False)
        self.system_bar_8.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.system_bar_8.setObjectName("system_bar_8")
        self.system_win_8 = QtWidgets.QPushButton(self.sys_tab)
        self.system_win_8.setGeometry(QtCore.QRect(160, 300, 161, 31))
        self.system_win_8.setObjectName("system_win_8")
        self.additional_tabs.addTab(self.sys_tab, "")
        self.ws_tab = QtWidgets.QWidget()
        self.ws_tab.setObjectName("ws_tab")
        self.work_bar_1 = QtWidgets.QProgressBar(self.ws_tab)
        self.work_bar_1.setGeometry(QtCore.QRect(370, 30, 141, 23))
        self.work_bar_1.setMaximum(7)
        self.work_bar_1.setProperty("value", 0)
        self.work_bar_1.setTextVisible(True)
        self.work_bar_1.setObjectName("work_bar_1")
        self.workstation_win_1 = QtWidgets.QPushButton(self.ws_tab)
        self.workstation_win_1.setGeometry(QtCore.QRect(170, 30, 191, 28))
        self.workstation_win_1.setObjectName("workstation_win_1")
        self.work_bar_2 = QtWidgets.QProgressBar(self.ws_tab)
        self.work_bar_2.setGeometry(QtCore.QRect(370, 70, 141, 23))
        self.work_bar_2.setMaximum(7)
        self.work_bar_2.setProperty("value", 0)
        self.work_bar_2.setTextVisible(True)
        self.work_bar_2.setObjectName("work_bar_2")
        self.workstation_win_2 = QtWidgets.QPushButton(self.ws_tab)
        self.workstation_win_2.setGeometry(QtCore.QRect(170, 70, 191, 28))
        self.workstation_win_2.setObjectName("workstation_win_2")
        self.workstation_win_4 = QtWidgets.QPushButton(self.ws_tab)
        self.workstation_win_4.setGeometry(QtCore.QRect(170, 150, 191, 28))
        self.workstation_win_4.setObjectName("workstation_win_4")
        self.work_bar_4 = QtWidgets.QProgressBar(self.ws_tab)
        self.work_bar_4.setGeometry(QtCore.QRect(370, 150, 141, 23))
        self.work_bar_4.setMaximum(7)
        self.work_bar_4.setProperty("value", 0)
        self.work_bar_4.setTextVisible(True)
        self.work_bar_4.setObjectName("work_bar_4")
        self.work_bar_3 = QtWidgets.QProgressBar(self.ws_tab)
        self.work_bar_3.setGeometry(QtCore.QRect(370, 110, 141, 23))
        self.work_bar_3.setMaximum(7)
        self.work_bar_3.setProperty("value", 0)
        self.work_bar_3.setTextVisible(True)
        self.work_bar_3.setObjectName("work_bar_3")
        self.workstation_win_3 = QtWidgets.QPushButton(self.ws_tab)
        self.workstation_win_3.setGeometry(QtCore.QRect(170, 110, 191, 28))
        self.workstation_win_3.setObjectName("workstation_win_3")
        self.workstation_win_7 = QtWidgets.QPushButton(self.ws_tab)
        self.workstation_win_7.setGeometry(QtCore.QRect(170, 270, 191, 28))
        self.workstation_win_7.setObjectName("workstation_win_7")
        self.work_bar_7 = QtWidgets.QProgressBar(self.ws_tab)
        self.work_bar_7.setGeometry(QtCore.QRect(370, 270, 141, 23))
        self.work_bar_7.setMaximum(7)
        self.work_bar_7.setProperty("value", 0)
        self.work_bar_7.setTextVisible(True)
        self.work_bar_7.setObjectName("work_bar_7")
        self.workstation_win_6 = QtWidgets.QPushButton(self.ws_tab)
        self.workstation_win_6.setGeometry(QtCore.QRect(170, 230, 191, 28))
        self.workstation_win_6.setObjectName("workstation_win_6")
        self.work_bar_8 = QtWidgets.QProgressBar(self.ws_tab)
        self.work_bar_8.setGeometry(QtCore.QRect(370, 310, 141, 23))
        self.work_bar_8.setMaximum(7)
        self.work_bar_8.setProperty("value", 0)
        self.work_bar_8.setTextVisible(True)
        self.work_bar_8.setObjectName("work_bar_8")
        self.work_bar_6 = QtWidgets.QProgressBar(self.ws_tab)
        self.work_bar_6.setGeometry(QtCore.QRect(370, 230, 141, 23))
        self.work_bar_6.setMaximum(7)
        self.work_bar_6.setProperty("value", 0)
        self.work_bar_6.setTextVisible(True)
        self.work_bar_6.setObjectName("work_bar_6")
        self.workstation_win_8 = QtWidgets.QPushButton(self.ws_tab)
        self.workstation_win_8.setGeometry(QtCore.QRect(170, 310, 191, 28))
        self.workstation_win_8.setObjectName("workstation_win_8")
        self.work_bar_5 = QtWidgets.QProgressBar(self.ws_tab)
        self.work_bar_5.setGeometry(QtCore.QRect(370, 190, 141, 23))
        self.work_bar_5.setMaximum(7)
        self.work_bar_5.setProperty("value", 0)
        self.work_bar_5.setTextVisible(True)
        self.work_bar_5.setObjectName("work_bar_5")
        self.workstation_win_5 = QtWidgets.QPushButton(self.ws_tab)
        self.workstation_win_5.setGeometry(QtCore.QRect(170, 190, 191, 28))
        self.workstation_win_5.setObjectName("workstation_win_5")
        self.additional_tabs.addTab(self.ws_tab, "")
        self.generator_tab = QtWidgets.QWidget()
        self.generator_tab.setObjectName("generator_tab")
        self.stockert_bar_1 = QtWidgets.QProgressBar(self.generator_tab)
        self.stockert_bar_1.setGeometry(QtCore.QRect(370, 20, 141, 23))
        self.stockert_bar_1.setMaximum(6)
        self.stockert_bar_1.setProperty("value", 0)
        self.stockert_bar_1.setTextVisible(True)
        self.stockert_bar_1.setObjectName("stockert_bar_1")
        self.stockert_win_1 = QtWidgets.QPushButton(self.generator_tab)
        self.stockert_win_1.setGeometry(QtCore.QRect(170, 20, 191, 28))
        self.stockert_win_1.setObjectName("stockert_win_1")
        self.stockert_bar_2 = QtWidgets.QProgressBar(self.generator_tab)
        self.stockert_bar_2.setGeometry(QtCore.QRect(370, 50, 141, 23))
        self.stockert_bar_2.setMaximum(6)
        self.stockert_bar_2.setProperty("value", 0)
        self.stockert_bar_2.setTextVisible(True)
        self.stockert_bar_2.setObjectName("stockert_bar_2")
        self.stockert_win_2 = QtWidgets.QPushButton(self.generator_tab)
        self.stockert_win_2.setGeometry(QtCore.QRect(170, 50, 191, 28))
        self.stockert_win_2.setObjectName("stockert_win_2")
        self.smartablate_win_1 = QtWidgets.QPushButton(self.generator_tab)
        self.smartablate_win_1.setGeometry(QtCore.QRect(170, 80, 191, 28))
        self.smartablate_win_1.setObjectName("smartablate_win_1")
        self.smartablate_bar_1 = QtWidgets.QProgressBar(self.generator_tab)
        self.smartablate_bar_1.setGeometry(QtCore.QRect(370, 80, 141, 23))
        self.smartablate_bar_1.setMaximum(3)
        self.smartablate_bar_1.setProperty("value", 0)
        self.smartablate_bar_1.setTextVisible(True)
        self.smartablate_bar_1.setObjectName("smartablate_bar_1")
        self.smartablate_win_2 = QtWidgets.QPushButton(self.generator_tab)
        self.smartablate_win_2.setGeometry(QtCore.QRect(170, 110, 191, 28))
        self.smartablate_win_2.setObjectName("smartablate_win_2")
        self.smartablate_bar_2 = QtWidgets.QProgressBar(self.generator_tab)
        self.smartablate_bar_2.setGeometry(QtCore.QRect(370, 110, 141, 23))
        self.smartablate_bar_2.setMaximum(3)
        self.smartablate_bar_2.setProperty("value", 0)
        self.smartablate_bar_2.setTextVisible(True)
        self.smartablate_bar_2.setObjectName("smartablate_bar_2")
        self.smartablate_win_3 = QtWidgets.QPushButton(self.generator_tab)
        self.smartablate_win_3.setGeometry(QtCore.QRect(170, 140, 191, 28))
        self.smartablate_win_3.setObjectName("smartablate_win_3")
        self.smartablate_bar_3 = QtWidgets.QProgressBar(self.generator_tab)
        self.smartablate_bar_3.setGeometry(QtCore.QRect(370, 140, 141, 23))
        self.smartablate_bar_3.setMaximum(3)
        self.smartablate_bar_3.setProperty("value", 0)
        self.smartablate_bar_3.setTextVisible(True)
        self.smartablate_bar_3.setObjectName("smartablate_bar_3")
        self.ngen_win_1 = QtWidgets.QPushButton(self.generator_tab)
        self.ngen_win_1.setGeometry(QtCore.QRect(170, 170, 191, 28))
        self.ngen_win_1.setObjectName("ngen_win_1")
        self.ngen_bar_1 = QtWidgets.QProgressBar(self.generator_tab)
        self.ngen_bar_1.setGeometry(QtCore.QRect(370, 170, 141, 23))
        self.ngen_bar_1.setMaximum(25)
        self.ngen_bar_1.setProperty("value", 0)
        self.ngen_bar_1.setTextVisible(True)
        self.ngen_bar_1.setObjectName("ngen_bar_1")
        self.ngen_win_2 = QtWidgets.QPushButton(self.generator_tab)
        self.ngen_win_2.setGeometry(QtCore.QRect(170, 200, 191, 28))
        self.ngen_win_2.setObjectName("ngen_win_2")
        self.ngen_bar_2 = QtWidgets.QProgressBar(self.generator_tab)
        self.ngen_bar_2.setGeometry(QtCore.QRect(370, 200, 141, 23))
        self.ngen_bar_2.setMaximum(25)
        self.ngen_bar_2.setProperty("value", 0)
        self.ngen_bar_2.setTextVisible(True)
        self.ngen_bar_2.setObjectName("ngen_bar_2")
        self.ngen_win_3 = QtWidgets.QPushButton(self.generator_tab)
        self.ngen_win_3.setGeometry(QtCore.QRect(170, 230, 191, 28))
        self.ngen_win_3.setObjectName("ngen_win_3")
        self.ngen_bar_3 = QtWidgets.QProgressBar(self.generator_tab)
        self.ngen_bar_3.setGeometry(QtCore.QRect(370, 230, 141, 23))
        self.ngen_bar_3.setMaximum(25)
        self.ngen_bar_3.setProperty("value", 0)
        self.ngen_bar_3.setTextVisible(True)
        self.ngen_bar_3.setObjectName("ngen_bar_3")
        self.nmark_win_1 = QtWidgets.QPushButton(self.generator_tab)
        self.nmark_win_1.setGeometry(QtCore.QRect(170, 260, 191, 28))
        self.nmark_win_1.setObjectName("nmark_win_1")
        self.nmark_bar_1 = QtWidgets.QProgressBar(self.generator_tab)
        self.nmark_bar_1.setGeometry(QtCore.QRect(370, 260, 141, 23))
        self.nmark_bar_1.setMaximum(9)
        self.nmark_bar_1.setProperty("value", 0)
        self.nmark_bar_1.setTextVisible(True)
        self.nmark_bar_1.setObjectName("nmark_bar_1")
        self.nmark_bar_2 = QtWidgets.QProgressBar(self.generator_tab)
        self.nmark_bar_2.setGeometry(QtCore.QRect(370, 290, 141, 23))
        self.nmark_bar_2.setMaximum(9)
        self.nmark_bar_2.setProperty("value", 0)
        self.nmark_bar_2.setTextVisible(True)
        self.nmark_bar_2.setObjectName("nmark_bar_2")
        self.nmark_win_2 = QtWidgets.QPushButton(self.generator_tab)
        self.nmark_win_2.setGeometry(QtCore.QRect(170, 290, 191, 28))
        self.nmark_win_2.setObjectName("nmark_win_2")
        self.additional_tabs.addTab(self.generator_tab, "")
        self.ultra_tab = QtWidgets.QWidget()
        self.ultra_tab.setObjectName("ultra_tab")
        self.ultra_win_1 = QtWidgets.QPushButton(self.ultra_tab)
        self.ultra_win_1.setGeometry(QtCore.QRect(160, 15, 171, 31))
        self.ultra_win_1.setObjectName("ultra_win_1")
        self.ultra_bar_1 = QtWidgets.QProgressBar(self.ultra_tab)
        self.ultra_bar_1.setGeometry(QtCore.QRect(350, 20, 141, 23))
        self.ultra_bar_1.setMaximum(6)
        self.ultra_bar_1.setProperty("value", 0)
        self.ultra_bar_1.setTextVisible(True)
        self.ultra_bar_1.setObjectName("ultra_bar_1")
        self.ultra_win_2 = QtWidgets.QPushButton(self.ultra_tab)
        self.ultra_win_2.setGeometry(QtCore.QRect(160, 55, 171, 31))
        self.ultra_win_2.setObjectName("ultra_win_2")
        self.ultra_bar_2 = QtWidgets.QProgressBar(self.ultra_tab)
        self.ultra_bar_2.setGeometry(QtCore.QRect(350, 60, 141, 23))
        self.ultra_bar_2.setMaximum(6)
        self.ultra_bar_2.setProperty("value", 0)
        self.ultra_bar_2.setTextVisible(True)
        self.ultra_bar_2.setObjectName("ultra_bar_2")
        self.ultra_win_3 = QtWidgets.QPushButton(self.ultra_tab)
        self.ultra_win_3.setGeometry(QtCore.QRect(160, 95, 171, 31))
        self.ultra_win_3.setObjectName("ultra_win_3")
        self.ultra_bar_3 = QtWidgets.QProgressBar(self.ultra_tab)
        self.ultra_bar_3.setGeometry(QtCore.QRect(350, 100, 141, 23))
        self.ultra_bar_3.setMaximum(6)
        self.ultra_bar_3.setProperty("value", 0)
        self.ultra_bar_3.setTextVisible(True)
        self.ultra_bar_3.setObjectName("ultra_bar_3")
        self.ultra_win_5 = QtWidgets.QPushButton(self.ultra_tab)
        self.ultra_win_5.setGeometry(QtCore.QRect(160, 175, 171, 31))
        self.ultra_win_5.setObjectName("ultra_win_5")
        self.ultra_win_4 = QtWidgets.QPushButton(self.ultra_tab)
        self.ultra_win_4.setGeometry(QtCore.QRect(160, 135, 171, 31))
        self.ultra_win_4.setObjectName("ultra_win_4")
        self.ultra_bar_5 = QtWidgets.QProgressBar(self.ultra_tab)
        self.ultra_bar_5.setGeometry(QtCore.QRect(350, 180, 141, 23))
        self.ultra_bar_5.setMaximum(6)
        self.ultra_bar_5.setProperty("value", 0)
        self.ultra_bar_5.setTextVisible(True)
        self.ultra_bar_5.setObjectName("ultra_bar_5")
        self.ultra_bar_4 = QtWidgets.QProgressBar(self.ultra_tab)
        self.ultra_bar_4.setGeometry(QtCore.QRect(350, 140, 141, 23))
        self.ultra_bar_4.setMaximum(6)
        self.ultra_bar_4.setProperty("value", 0)
        self.ultra_bar_4.setTextVisible(True)
        self.ultra_bar_4.setObjectName("ultra_bar_4")
        self.ultra_win_6 = QtWidgets.QPushButton(self.ultra_tab)
        self.ultra_win_6.setGeometry(QtCore.QRect(160, 215, 171, 31))
        self.ultra_win_6.setObjectName("ultra_win_6")
        self.ultra_bar_6 = QtWidgets.QProgressBar(self.ultra_tab)
        self.ultra_bar_6.setGeometry(QtCore.QRect(350, 220, 141, 23))
        self.ultra_bar_6.setMaximum(6)
        self.ultra_bar_6.setProperty("value", 0)
        self.ultra_bar_6.setTextVisible(True)
        self.ultra_bar_6.setObjectName("ultra_bar_6")
        self.ultra_bar_7 = QtWidgets.QProgressBar(self.ultra_tab)
        self.ultra_bar_7.setGeometry(QtCore.QRect(350, 260, 141, 23))
        self.ultra_bar_7.setMaximum(6)
        self.ultra_bar_7.setProperty("value", 0)
        self.ultra_bar_7.setTextVisible(True)
        self.ultra_bar_7.setObjectName("ultra_bar_7")
        self.ultra_win_7 = QtWidgets.QPushButton(self.ultra_tab)
        self.ultra_win_7.setGeometry(QtCore.QRect(160, 255, 171, 31))
        self.ultra_win_7.setObjectName("ultra_win_7")
        self.ultra_win_8 = QtWidgets.QPushButton(self.ultra_tab)
        self.ultra_win_8.setGeometry(QtCore.QRect(160, 295, 171, 31))
        self.ultra_win_8.setObjectName("ultra_win_8")
        self.ultra_bar_8 = QtWidgets.QProgressBar(self.ultra_tab)
        self.ultra_bar_8.setGeometry(QtCore.QRect(350, 300, 141, 23))
        self.ultra_bar_8.setMaximum(6)
        self.ultra_bar_8.setProperty("value", 0)
        self.ultra_bar_8.setTextVisible(True)
        self.ultra_bar_8.setObjectName("ultra_bar_8")
        self.additional_tabs.addTab(self.ultra_tab, "")
        self.catheters_tab = QtWidgets.QWidget()
        self.catheters_tab.setObjectName("catheters_tab")
        self.catheter_1 = QtWidgets.QPushButton(self.catheters_tab)
        self.catheter_1.setGeometry(QtCore.QRect(170, 10, 141, 28))
        self.catheter_1.setObjectName("catheter_1")
        self.catheter_list = QtWidgets.QListWidget(self.catheters_tab)
        self.catheter_list.setGeometry(QtCore.QRect(170, 40, 291, 291))
        self.catheter_list.setObjectName("catheter_list")
        self.catheter_2 = QtWidgets.QPushButton(self.catheters_tab)
        self.catheter_2.setGeometry(QtCore.QRect(320, 10, 141, 28))
        self.catheter_2.setObjectName("catheter_2")
        self.additional_tabs.addTab(self.catheters_tab, "")
        self.extra_tab = QtWidgets.QWidget()
        self.extra_tab.setObjectName("extra_tab")
        self.pacer_bar = QtWidgets.QProgressBar(self.extra_tab)
        self.pacer_bar.setGeometry(QtCore.QRect(20, 70, 118, 23))
        self.pacer_bar.setMaximum(2)
        self.pacer_bar.setProperty("value", 0)
        self.pacer_bar.setTextVisible(True)
        self.pacer_bar.setInvertedAppearance(False)
        self.pacer_bar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.pacer_bar.setObjectName("pacer_bar")
        self.pacer_win = QtWidgets.QPushButton(self.extra_tab)
        self.pacer_win.setGeometry(QtCore.QRect(15, 30, 131, 31))
        self.pacer_win.setObjectName("pacer_win")
        self.qdot_bar = QtWidgets.QProgressBar(self.extra_tab)
        self.qdot_bar.setGeometry(QtCore.QRect(190, 70, 118, 23))
        self.qdot_bar.setMaximum(3)
        self.qdot_bar.setProperty("value", 0)
        self.qdot_bar.setTextVisible(True)
        self.qdot_bar.setInvertedAppearance(False)
        self.qdot_bar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.qdot_bar.setObjectName("qdot_bar")
        self.qdot_win = QtWidgets.QPushButton(self.extra_tab)
        self.qdot_win.setGeometry(QtCore.QRect(185, 30, 131, 31))
        self.qdot_win.setObjectName("qdot_win")
        self.printer_bar = QtWidgets.QProgressBar(self.extra_tab)
        self.printer_bar.setGeometry(QtCore.QRect(360, 70, 118, 23))
        self.printer_bar.setMaximum(2)
        self.printer_bar.setProperty("value", 0)
        self.printer_bar.setTextVisible(True)
        self.printer_bar.setInvertedAppearance(False)
        self.printer_bar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.printer_bar.setObjectName("printer_bar")
        self.printer_win = QtWidgets.QPushButton(self.extra_tab)
        self.printer_win.setGeometry(QtCore.QRect(355, 30, 131, 31))
        self.printer_win.setObjectName("printer_win")
        self.epu_bar = QtWidgets.QProgressBar(self.extra_tab)
        self.epu_bar.setGeometry(QtCore.QRect(520, 70, 118, 23))
        self.epu_bar.setMaximum(2)
        self.epu_bar.setProperty("value", 0)
        self.epu_bar.setTextVisible(True)
        self.epu_bar.setInvertedAppearance(False)
        self.epu_bar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.epu_bar.setObjectName("epu_bar")
        self.epu_win = QtWidgets.QPushButton(self.extra_tab)
        self.epu_win.setGeometry(QtCore.QRect(515, 30, 131, 31))
        self.epu_win.setObjectName("epu_win")
        self.demo_bar = QtWidgets.QProgressBar(self.extra_tab)
        self.demo_bar.setGeometry(QtCore.QRect(30, 300, 118, 23))
        self.demo_bar.setMaximum(5)
        self.demo_bar.setProperty("value", 0)
        self.demo_bar.setTextVisible(True)
        self.demo_bar.setInvertedAppearance(False)
        self.demo_bar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.demo_bar.setObjectName("demo_bar")
        self.demo_win = QtWidgets.QPushButton(self.extra_tab)
        self.demo_win.setGeometry(QtCore.QRect(25, 260, 131, 31))
        self.demo_win.setObjectName("demo_win")
        self.demo_bar_2 = QtWidgets.QProgressBar(self.extra_tab)
        self.demo_bar_2.setGeometry(QtCore.QRect(190, 300, 118, 23))
        self.demo_bar_2.setMaximum(5)
        self.demo_bar_2.setProperty("value", 0)
        self.demo_bar_2.setTextVisible(True)
        self.demo_bar_2.setInvertedAppearance(False)
        self.demo_bar_2.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.demo_bar_2.setObjectName("demo_bar_2")
        self.demo_win_2 = QtWidgets.QPushButton(self.extra_tab)
        self.demo_win_2.setGeometry(QtCore.QRect(185, 260, 131, 31))
        self.demo_win_2.setObjectName("demo_win_2")
        self.demo_bar_3 = QtWidgets.QProgressBar(self.extra_tab)
        self.demo_bar_3.setGeometry(QtCore.QRect(350, 300, 118, 23))
        self.demo_bar_3.setMaximum(5)
        self.demo_bar_3.setProperty("value", 0)
        self.demo_bar_3.setTextVisible(True)
        self.demo_bar_3.setInvertedAppearance(False)
        self.demo_bar_3.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.demo_bar_3.setObjectName("demo_bar_3")
        self.demo_win_3 = QtWidgets.QPushButton(self.extra_tab)
        self.demo_win_3.setGeometry(QtCore.QRect(345, 260, 131, 31))
        self.demo_win_3.setObjectName("demo_win_3")
        self.additional_tabs.addTab(self.extra_tab, "")
        self.import_button = QtWidgets.QPushButton(self.centralwidget)
        self.import_button.setGeometry(QtCore.QRect(170, 490, 121, 28))
        self.import_button.setObjectName("import_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 698, 26))
        self.menubar.setObjectName("menubar")
        self.menuAdd_Device = QtWidgets.QMenu(self.menubar)
        self.menuAdd_Device.setObjectName("menuAdd_Device")
        self.toolsMenu = QtWidgets.QMenu(self.menubar)
        self.toolsMenu.setObjectName("toolsMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSystem = QtWidgets.QAction(MainWindow)
        self.actionSystem.setObjectName("actionSystem")
        self.actionUltraSound = QtWidgets.QAction(MainWindow)
        self.actionUltraSound.setObjectName("actionUltraSound")
        self.actionWork_Station = QtWidgets.QAction(MainWindow)
        self.actionWork_Station.setObjectName("actionWork_Station")
        self.actionCatheters = QtWidgets.QAction(MainWindow)
        self.actionCatheters.setObjectName("actionCatheters")
        self.actionRF_Generator_Stockert = QtWidgets.QAction(MainWindow)
        self.actionRF_Generator_Stockert.setObjectName("actionRF_Generator_Stockert")
        self.actionRF_Generator_Smart_Ablate = QtWidgets.QAction(MainWindow)
        self.actionRF_Generator_Smart_Ablate.setObjectName("actionRF_Generator_Smart_Ablate")
        self.actionRF_Generator_nGen = QtWidgets.QAction(MainWindow)
        self.actionRF_Generator_nGen.setObjectName("actionRF_Generator_nGen")
        self.actionRF_Generator_nMARQ = QtWidgets.QAction(MainWindow)
        self.actionRF_Generator_nMARQ.setObjectName("actionRF_Generator_nMARQ")
        self.actionQDOT = QtWidgets.QAction(MainWindow)
        self.actionQDOT.setObjectName("actionQDOT")
        self.actionPacer = QtWidgets.QAction(MainWindow)
        self.actionPacer.setObjectName("actionPacer")
        self.actionQDOT_Dongle = QtWidgets.QAction(MainWindow)
        self.actionQDOT_Dongle.setObjectName("actionQDOT_Dongle")
        self.actionPrinter = QtWidgets.QAction(MainWindow)
        self.actionPrinter.setObjectName("actionPrinter")
        self.actionEPU_Device = QtWidgets.QAction(MainWindow)
        self.actionEPU_Device.setObjectName("actionEPU_Device")
        self.actionDemo_Laptop = QtWidgets.QAction(MainWindow)
        self.actionDemo_Laptop.setObjectName("actionDemo_Laptop")
        self.actionCatalog_Helper = QtWidgets.QAction(MainWindow)
        self.actionCatalog_Helper.setObjectName("actionCatalog_Helper")
        self.menuAdd_Device.addAction(self.actionSystem)
        self.menuAdd_Device.addAction(self.actionUltraSound)
        self.menuAdd_Device.addAction(self.actionWork_Station)
        self.menuAdd_Device.addSeparator()
        self.menuAdd_Device.addSeparator()
        self.menuAdd_Device.addAction(self.actionRF_Generator_Stockert)
        self.menuAdd_Device.addAction(self.actionRF_Generator_Smart_Ablate)
        self.menuAdd_Device.addAction(self.actionRF_Generator_nGen)
        self.menuAdd_Device.addAction(self.actionRF_Generator_nMARQ)
        self.menuAdd_Device.addSeparator()
        self.menuAdd_Device.addAction(self.actionPacer)
        self.menuAdd_Device.addAction(self.actionQDOT_Dongle)
        self.menuAdd_Device.addAction(self.actionPrinter)
        self.menuAdd_Device.addAction(self.actionEPU_Device)
        self.menuAdd_Device.addAction(self.actionDemo_Laptop)
        self.toolsMenu.addAction(self.actionCatalog_Helper)
        self.menubar.addAction(self.menuAdd_Device.menuAction())
        self.menubar.addAction(self.toolsMenu.menuAction())

        self.retranslateUi(MainWindow)
        self.additional_tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Auto Baseline "))
        self.title.setText(_translate("MainWindow", "Auto Baseline"))
        self.export_button.setText(_translate("MainWindow", "Export"))
        self.system_win_1.setText(_translate("MainWindow", "System #1 Information"))
        self.system_win_2.setText(_translate("MainWindow", "System #2 Information"))
        self.system_win_3.setText(_translate("MainWindow", "System #3 Information"))
        self.system_win_4.setText(_translate("MainWindow", "System #4 Information"))
        self.system_win_5.setText(_translate("MainWindow", "System #5 Information"))
        self.system_win_6.setText(_translate("MainWindow", "System #6 Information"))
        self.system_win_7.setText(_translate("MainWindow", "System #7 Information"))
        self.system_win_8.setText(_translate("MainWindow", "System #8 Information"))
        self.additional_tabs.setTabText(self.additional_tabs.indexOf(self.sys_tab), _translate("MainWindow", "Systems"))
        self.workstation_win_1.setText(_translate("MainWindow", "WorkStation #1 Information"))
        self.workstation_win_2.setText(_translate("MainWindow", "WorkStation #2 Information"))
        self.workstation_win_4.setText(_translate("MainWindow", "WorkStation #4 Information"))
        self.workstation_win_3.setText(_translate("MainWindow", "WorkStation #3 Information"))
        self.workstation_win_7.setText(_translate("MainWindow", "WorkStation #7 Information"))
        self.workstation_win_6.setText(_translate("MainWindow", "WorkStation #6 Information"))
        self.workstation_win_8.setText(_translate("MainWindow", "WorkStation #8 Information"))
        self.workstation_win_5.setText(_translate("MainWindow", "WorkStation #5 Information"))
        self.additional_tabs.setTabText(self.additional_tabs.indexOf(self.ws_tab), _translate("MainWindow", "Workstations"))
        self.stockert_win_1.setText(_translate("MainWindow", "Stockert "))
        self.stockert_win_2.setText(_translate("MainWindow", "Stockert "))
        self.smartablate_win_1.setText(_translate("MainWindow", "SmartAblate™"))
        self.smartablate_win_2.setText(_translate("MainWindow", "SmartAblate™"))
        self.smartablate_win_3.setText(_translate("MainWindow", "SmartAblate™"))
        self.ngen_win_1.setText(_translate("MainWindow", "nGEN™"))
        self.ngen_win_2.setText(_translate("MainWindow", "nGEN™"))
        self.ngen_win_3.setText(_translate("MainWindow", "nGEN™"))
        self.nmark_win_1.setText(_translate("MainWindow", "nMARQ™"))
        self.nmark_win_2.setText(_translate("MainWindow", "nMARQ™"))
        self.additional_tabs.setTabText(self.additional_tabs.indexOf(self.generator_tab), _translate("MainWindow", "RF Generators"))
        self.ultra_win_1.setText(_translate("MainWindow", "Ultrasound #1 Information"))
        self.ultra_win_2.setText(_translate("MainWindow", "Ultrasound #2 Information"))
        self.ultra_win_3.setText(_translate("MainWindow", "Ultrasound #3 Information"))
        self.ultra_win_5.setText(_translate("MainWindow", "Ultrasound #5 Information"))
        self.ultra_win_4.setText(_translate("MainWindow", "Ultrasound #4 Information"))
        self.ultra_win_6.setText(_translate("MainWindow", "Ultrasound #6 Information"))
        self.ultra_win_7.setText(_translate("MainWindow", "Ultrasound #7 Information"))
        self.ultra_win_8.setText(_translate("MainWindow", "Ultrasound #8 Information"))
        self.additional_tabs.setTabText(self.additional_tabs.indexOf(self.ultra_tab), _translate("MainWindow", "Ultrasounds"))
        self.catheter_1.setText(_translate("MainWindow", "Add Catheter"))
        self.catheter_2.setText(_translate("MainWindow", "Remove Catheter"))
        self.additional_tabs.setTabText(self.additional_tabs.indexOf(self.catheters_tab), _translate("MainWindow", "Catheters"))
        self.pacer_win.setText(_translate("MainWindow", "Pacer"))
        self.qdot_win.setText(_translate("MainWindow", "Qdot™ Dongle"))
        self.printer_win.setText(_translate("MainWindow", "Printer"))
        self.epu_win.setText(_translate("MainWindow", "EPU Device"))
        self.demo_win.setText(_translate("MainWindow", "Demo Laptop"))
        self.demo_win_2.setText(_translate("MainWindow", "Demo Laptop #2"))
        self.demo_win_3.setText(_translate("MainWindow", "Demo Laptop #3"))
        self.additional_tabs.setTabText(self.additional_tabs.indexOf(self.extra_tab), _translate("MainWindow", "Extra"))
        self.import_button.setText(_translate("MainWindow", "Import"))
        self.menuAdd_Device.setTitle(_translate("MainWindow", "Add Device"))
        self.toolsMenu.setTitle(_translate("MainWindow", "Tools"))
        self.actionSystem.setText(_translate("MainWindow", "System"))
        self.actionUltraSound.setText(_translate("MainWindow", "Ultrasound"))
        self.actionWork_Station.setText(_translate("MainWindow", "Work Station"))
        self.actionCatheters.setText(_translate("MainWindow", "Catheters"))
        self.actionRF_Generator_Stockert.setText(_translate("MainWindow", "RF Generator - Stockert"))
        self.actionRF_Generator_Smart_Ablate.setText(_translate("MainWindow", "RF Generator - Smart Ablate"))
        self.actionRF_Generator_nGen.setText(_translate("MainWindow", "RF Generator - nGen"))
        self.actionRF_Generator_nMARQ.setText(_translate("MainWindow", "RF Generator - nMARQ™"))
        self.actionQDOT.setText(_translate("MainWindow", "QDOT"))
        self.actionPacer.setText(_translate("MainWindow", "Pacer"))
        self.actionQDOT_Dongle.setText(_translate("MainWindow", "QDOT Dongle"))
        self.actionPrinter.setText(_translate("MainWindow", "Printer"))
        self.actionEPU_Device.setText(_translate("MainWindow", "EPU Device"))
        self.actionDemo_Laptop.setText(_translate("MainWindow", "Demo Laptop"))
        self.actionCatalog_Helper.setText(_translate("MainWindow", "Catalog Helper"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
