# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nmarq_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(517, 479)
        self.software_text = QtWidgets.QLineEdit(Dialog)
        self.software_text.setGeometry(QtCore.QRect(260, 70, 191, 22))
        self.software_text.setText("")
        self.software_text.setObjectName("software_text")
        self.GtoCable_text = QtWidgets.QLineEdit(Dialog)
        self.GtoCable_text.setGeometry(QtCore.QRect(260, 140, 191, 22))
        self.GtoCable_text.setText("")
        self.GtoCable_text.setObjectName("GtoCable_text")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 215, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 60, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gToM_text = QtWidgets.QLineEdit(Dialog)
        self.gToM_text.setGeometry(QtCore.QRect(260, 260, 191, 22))
        self.gToM_text.setText("")
        self.gToM_text.setObjectName("gToM_text")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 255, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.confirm_button = QtWidgets.QPushButton(Dialog)
        self.confirm_button.setGeometry(QtCore.QRect(290, 430, 93, 28))
        self.confirm_button.setObjectName("confirm_button")
        self.check_button = QtWidgets.QPushButton(Dialog)
        self.check_button.setGeometry(QtCore.QRect(130, 430, 93, 28))
        self.check_button.setObjectName("check_button")
        self.ethernetCable_text = QtWidgets.QLineEdit(Dialog)
        self.ethernetCable_text.setGeometry(QtCore.QRect(260, 180, 191, 22))
        self.ethernetCable_text.setText("")
        self.ethernetCable_text.setObjectName("ethernetCable_text")
        self.SN_text = QtWidgets.QLineEdit(Dialog)
        self.SN_text.setGeometry(QtCore.QRect(260, 105, 191, 22))
        self.SN_text.setText("")
        self.SN_text.setObjectName("SN_text")
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(200, 10, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 180, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gToPumpCable_text = QtWidgets.QLineEdit(Dialog)
        self.gToPumpCable_text.setGeometry(QtCore.QRect(260, 220, 191, 22))
        self.gToPumpCable_text.setText("")
        self.gToPumpCable_text.setObjectName("gToPumpCable_text")
        self.pumpSN_text = QtWidgets.QLineEdit(Dialog)
        self.pumpSN_text.setGeometry(QtCore.QRect(260, 290, 191, 22))
        self.pumpSN_text.setText("")
        self.pumpSN_text.setObjectName("pumpSN_text")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(40, 325, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(40, 365, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(40, 290, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pumpModel_text = QtWidgets.QLineEdit(Dialog)
        self.pumpModel_text.setGeometry(QtCore.QRect(260, 330, 191, 22))
        self.pumpModel_text.setText("")
        self.pumpModel_text.setObjectName("pumpModel_text")
        self.footPadel_text = QtWidgets.QLineEdit(Dialog)
        self.footPadel_text.setGeometry(QtCore.QRect(260, 370, 191, 22))
        self.footPadel_text.setText("")
        self.footPadel_text.setObjectName("footPadel_text")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Generator to Carto Cable:"))
        self.label_5.setText(_translate("Dialog", "Generator to CoolFlow cable:"))
        self.label.setText(_translate("Dialog", "System SW:"))
        self.label_6.setText(_translate("Dialog", "Generator to Monitor:"))
        self.confirm_button.setText(_translate("Dialog", "Confirm"))
        self.check_button.setText(_translate("Dialog", "Verify"))
        self.title.setText(_translate("Dialog", "nMARQ™"))
        self.label_4.setText(_translate("Dialog", "Ethernet Cable:"))
        self.label_2.setText(_translate("Dialog", "Serial Number:"))
        self.label_7.setText(_translate("Dialog", "CoolFlow pump Model:"))
        self.label_8.setText(_translate("Dialog", "Foot Pedal:"))
        self.label_9.setText(_translate("Dialog", "CoolFlow pump SN:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
