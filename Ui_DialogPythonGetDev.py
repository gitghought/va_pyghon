# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gaihao/va_pyghon/DialogPythonGetDev.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        Dialog.setSizeGripEnabled(True)
        self.btn_conn = QtGui.QPushButton(Dialog)
        self.btn_conn.setGeometry(QtCore.QRect(40, 190, 131, 51))
        self.btn_conn.setObjectName(_fromUtf8("btn_conn"))
        self.btn_disconn = QtGui.QPushButton(Dialog)
        self.btn_disconn.setGeometry(QtCore.QRect(220, 190, 131, 51))
        self.btn_disconn.setObjectName(_fromUtf8("btn_disconn"))
        self.le_ip = QtGui.QLineEdit(Dialog)
        self.le_ip.setGeometry(QtCore.QRect(160, 50, 201, 31))
        self.le_ip.setObjectName(_fromUtf8("le_ip"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 60, 72, 15))
        self.label.setObjectName(_fromUtf8("label"))
        self.btn_conn.raise_()
        self.btn_disconn.raise_()
        self.le_ip.raise_()
        self.label.raise_()
        self.le_ip.raise_()
        self.label.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.btn_conn.setText(_translate("Dialog", "连接", None))
        self.btn_disconn.setText(_translate("Dialog", "断开", None))
        self.label.setText(_translate("Dialog", "输入IP", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

