# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'smartablate_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(365, 310)
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(80, 10, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.check_button = QtWidgets.QPushButton(Dialog)
        self.check_button.setGeometry(QtCore.QRect(50, 270, 93, 28))
        self.check_button.setObjectName("check_button")
        self.SN_text = QtWidgets.QLineEdit(Dialog)
        self.SN_text.setGeometry(QtCore.QRect(150, 110, 191, 22))
        self.SN_text.setObjectName("SN_text")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 70, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.software_text = QtWidgets.QLineEdit(Dialog)
        self.software_text.setGeometry(QtCore.QRect(150, 75, 191, 22))
        self.software_text.setObjectName("software_text")
        self.gen_to_piu_text = QtWidgets.QLineEdit(Dialog)
        self.gen_to_piu_text.setGeometry(QtCore.QRect(200, 150, 141, 22))
        self.gen_to_piu_text.setObjectName("gen_to_piu_text")
        self.confirm_button = QtWidgets.QPushButton(Dialog)
        self.confirm_button.setGeometry(QtCore.QRect(210, 270, 93, 28))
        self.confirm_button.setObjectName("confirm_button")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gen_to_ws_text = QtWidgets.QLineEdit(Dialog)
        self.gen_to_ws_text.setGeometry(QtCore.QRect(200, 190, 141, 22))
        self.gen_to_ws_text.setObjectName("gen_to_ws_text")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 190, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.footPedal_text = QtWidgets.QLineEdit(Dialog)
        self.footPedal_text.setGeometry(QtCore.QRect(140, 220, 191, 22))
        self.footPedal_text.setObjectName("footPedal_text")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 220, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.software_text, self.SN_text)
        Dialog.setTabOrder(self.SN_text, self.gen_to_piu_text)
        Dialog.setTabOrder(self.gen_to_piu_text, self.gen_to_ws_text)
        Dialog.setTabOrder(self.gen_to_ws_text, self.footPedal_text)
        Dialog.setTabOrder(self.footPedal_text, self.check_button)
        Dialog.setTabOrder(self.check_button, self.confirm_button)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title.setText(_translate("Dialog", "SmartAblate???"))
        self.check_button.setText(_translate("Dialog", "Verify"))
        self.label.setText(_translate("Dialog", "System SW:"))
        self.confirm_button.setText(_translate("Dialog", "Confirm"))
        self.label_2.setText(_translate("Dialog", "Serial Number:"))
        self.label_3.setText(_translate("Dialog", "Generator to PIU cable:"))
        self.label_4.setText(_translate("Dialog", "Generator to WS cable:"))
        self.label_5.setText(_translate("Dialog", "Foot Pedal:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
