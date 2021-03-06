# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(503, 392)
        self.wsType_text = QtWidgets.QLineEdit(Dialog)
        self.wsType_text.setGeometry(QtCore.QRect(200, 80, 191, 22))
        self.wsType_text.setText("")
        self.wsType_text.setObjectName("wsType_text")
        self.dsp_text = QtWidgets.QLineEdit(Dialog)
        self.dsp_text.setGeometry(QtCore.QRect(200, 150, 191, 22))
        self.dsp_text.setText("")
        self.dsp_text.setObjectName("dsp_text")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 150, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 225, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 75, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(60, 260, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.confirm_button = QtWidgets.QPushButton(Dialog)
        self.confirm_button.setGeometry(QtCore.QRect(270, 340, 93, 28))
        self.confirm_button.setObjectName("confirm_button")
        self.check_button = QtWidgets.QPushButton(Dialog)
        self.check_button.setGeometry(QtCore.QRect(110, 340, 93, 28))
        self.check_button.setObjectName("check_button")
        self.imageV_text = QtWidgets.QLineEdit(Dialog)
        self.imageV_text.setGeometry(QtCore.QRect(200, 190, 191, 22))
        self.imageV_text.setText("")
        self.imageV_text.setObjectName("imageV_text")
        self.SW_text = QtWidgets.QLineEdit(Dialog)
        self.SW_text.setGeometry(QtCore.QRect(200, 115, 191, 22))
        self.SW_text.setText("")
        self.SW_text.setObjectName("SW_text")
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(140, 10, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 190, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.serviceTag_text = QtWidgets.QLineEdit(Dialog)
        self.serviceTag_text.setGeometry(QtCore.QRect(200, 230, 191, 22))
        self.serviceTag_text.setText("")
        self.serviceTag_text.setObjectName("serviceTag_text")
        self.surpoint_checkbox = QtWidgets.QCheckBox(Dialog)
        self.surpoint_checkbox.setGeometry(QtCore.QRect(150, 300, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.surpoint_checkbox.setFont(font)
        self.surpoint_checkbox.setObjectName("surpoint_checkbox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.wsType_text, self.SW_text)
        Dialog.setTabOrder(self.SW_text, self.dsp_text)
        Dialog.setTabOrder(self.dsp_text, self.imageV_text)
        Dialog.setTabOrder(self.imageV_text, self.serviceTag_text)
        Dialog.setTabOrder(self.serviceTag_text, self.surpoint_checkbox)
        Dialog.setTabOrder(self.surpoint_checkbox, self.check_button)
        Dialog.setTabOrder(self.check_button, self.confirm_button)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "DSP Version:"))
        self.label_5.setText(_translate("Dialog", "Service Tag:"))
        self.label.setText(_translate("Dialog", "WS Type:"))
        self.label_6.setText(_translate("Dialog", "All licenses are activated by defualt, did you use:"))
        self.confirm_button.setText(_translate("Dialog", "Confirm"))
        self.check_button.setText(_translate("Dialog", "Verify"))
        self.title.setText(_translate("Dialog", "Demo Laptop"))
        self.label_4.setText(_translate("Dialog", "Image Version:"))
        self.label_2.setText(_translate("Dialog", "SW Version:"))
        self.surpoint_checkbox.setText(_translate("Dialog", "Visitag SurPoint??? With EPU"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
