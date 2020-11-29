# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'system_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_system_dialog(object):
    def setupUi(self, system_dialog):
        system_dialog.setObjectName("system_dialog")
        system_dialog.resize(402, 516)
        self.check_button = QtWidgets.QPushButton(system_dialog)
        self.check_button.setGeometry(QtCore.QRect(80, 470, 93, 28))
        self.check_button.setObjectName("check_button")
        self.lp_text = QtWidgets.QLineEdit(system_dialog)
        self.lp_text.setGeometry(QtCore.QRect(190, 170, 191, 22))
        self.lp_text.setObjectName("lp_text")
        self.label_7 = QtWidgets.QLabel(system_dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 350, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(system_dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 215, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.title = QtWidgets.QLabel(system_dialog)
        self.title.setGeometry(QtCore.QRect(150, 10, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.label_6 = QtWidgets.QLabel(system_dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 305, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.aquanum_text = QtWidgets.QLineEdit(system_dialog)
        self.aquanum_text.setGeometry(QtCore.QRect(190, 350, 191, 22))
        self.aquanum_text.setObjectName("aquanum_text")
        self.aquamax_text = QtWidgets.QLineEdit(system_dialog)
        self.aquamax_text.setGeometry(QtCore.QRect(190, 395, 191, 22))
        self.aquamax_text.setObjectName("aquamax_text")
        self.label_5 = QtWidgets.QLabel(system_dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 260, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(system_dialog)
        self.label_8.setGeometry(QtCore.QRect(10, 395, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(system_dialog)
        self.label.setGeometry(QtCore.QRect(10, 80, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.piu_text = QtWidgets.QLineEdit(system_dialog)
        self.piu_text.setGeometry(QtCore.QRect(190, 125, 191, 22))
        self.piu_text.setObjectName("piu_text")
        self.label_3 = QtWidgets.QLabel(system_dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.confirm_button = QtWidgets.QPushButton(system_dialog)
        self.confirm_button.setGeometry(QtCore.QRect(240, 470, 93, 28))
        self.confirm_button.setObjectName("confirm_button")
        self.ecg_text = QtWidgets.QLineEdit(system_dialog)
        self.ecg_text.setGeometry(QtCore.QRect(190, 305, 191, 22))
        self.ecg_text.setObjectName("ecg_text")
        self.patchunit_text = QtWidgets.QLineEdit(system_dialog)
        self.patchunit_text.setGeometry(QtCore.QRect(190, 215, 191, 22))
        self.patchunit_text.setObjectName("patchunit_text")
        self.label_2 = QtWidgets.QLabel(system_dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 125, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.system_text = QtWidgets.QLineEdit(system_dialog)
        self.system_text.setGeometry(QtCore.QRect(190, 80, 191, 22))
        self.system_text.setObjectName("system_text")
        self.mm_text = QtWidgets.QLineEdit(system_dialog)
        self.mm_text.setGeometry(QtCore.QRect(190, 260, 191, 22))
        self.mm_text.setObjectName("mm_text")

        self.retranslateUi(system_dialog)
        QtCore.QMetaObject.connectSlotsByName(system_dialog)
        system_dialog.setTabOrder(self.system_text, self.piu_text)
        system_dialog.setTabOrder(self.piu_text, self.lp_text)
        system_dialog.setTabOrder(self.lp_text, self.patchunit_text)
        system_dialog.setTabOrder(self.patchunit_text, self.mm_text)
        system_dialog.setTabOrder(self.mm_text, self.ecg_text)
        system_dialog.setTabOrder(self.ecg_text, self.aquanum_text)
        system_dialog.setTabOrder(self.aquanum_text, self.aquamax_text)
        system_dialog.setTabOrder(self.aquamax_text, self.check_button)
        system_dialog.setTabOrder(self.check_button, self.confirm_button)

    def retranslateUi(self, system_dialog):
        _translate = QtCore.QCoreApplication.translate
        system_dialog.setWindowTitle(_translate("system_dialog", "Dialog"))
        self.check_button.setText(_translate("system_dialog", "Verify"))
        self.label_7.setText(_translate("system_dialog", "Aquarium number:"))
        self.label_4.setText(_translate("system_dialog", "Patch Unit number:"))
        self.title.setText(_translate("system_dialog", "System"))
        self.label_6.setText(_translate("system_dialog", "ECG Phantom number:"))
        self.label_5.setText(_translate("system_dialog", "Monitors model:"))
        self.label_8.setText(_translate("system_dialog", "Aquarium maximo:"))
        self.label.setText(_translate("system_dialog", "System Number:"))
        self.label_3.setText(_translate("system_dialog", "Location Pad number:"))
        self.confirm_button.setText(_translate("system_dialog", "Confirm"))
        self.label_2.setText(_translate("system_dialog", "PIU Configuration:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    system_dialog = QtWidgets.QDialog()
    ui = Ui_system_dialog()
    ui.setupUi(system_dialog)
    system_dialog.show()
    sys.exit(app.exec_())
