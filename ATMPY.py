# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ATMUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(273, 242)
        self.btnOk = QtWidgets.QPushButton(Dialog)
        self.btnOk.setGeometry(QtCore.QRect(100, 140, 75, 23))
        self.btnOk.setObjectName("btnOk")
        self.txtName = QtWidgets.QLineEdit(Dialog)
        self.txtName.setGeometry(QtCore.QRect(20, 80, 113, 20))
        self.txtName.setText("")
        self.txtName.setObjectName("txtName")
        self.txtPass = QtWidgets.QLineEdit(Dialog)
        self.txtPass.setGeometry(QtCore.QRect(80, 110, 113, 20))
        self.txtPass.setText("")
        self.txtPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPass.setObjectName("txtPass")
        self.lbllogin = QtWidgets.QLabel(Dialog)
        self.lbllogin.setGeometry(QtCore.QRect(20, 20, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbllogin.setFont(font)
        self.lbllogin.setObjectName("lbllogin")
        self.txtID = QtWidgets.QLineEdit(Dialog)
        self.txtID.setGeometry(QtCore.QRect(140, 80, 113, 20))
        self.txtID.setText("")
        self.txtID.setObjectName("txtID")
        self.lblError = QtWidgets.QLabel(Dialog)
        self.lblError.setGeometry(QtCore.QRect(10, 200, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblError.setFont(font)
        self.lblError.setObjectName("lblError")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnOk.setText(_translate("Dialog", "OK"))
        self.txtName.setPlaceholderText(_translate("Dialog", "UserName"))
        self.txtPass.setPlaceholderText(_translate("Dialog", "Password"))
        self.lbllogin.setText(_translate("Dialog", "Login Page"))
        self.txtID.setPlaceholderText(_translate("Dialog", "ID"))
        self.lblError.setText(_translate("Dialog", "Login Page"))
