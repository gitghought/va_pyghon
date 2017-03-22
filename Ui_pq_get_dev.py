# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gaihao/va_pyghon/pq_get_dev.ui'
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
        self.label_connectstatus = QtGui.QLabel(Dialog)
        self.label_connectstatus.setGeometry(QtCore.QRect(170, 130, 67, 17))
        self.label_connectstatus.setObjectName(_fromUtf8("label_connectstatus"))
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(60, 50, 291, 61))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ipadd = QtGui.QLabel(self.widget)
        self.ipadd.setObjectName(_fromUtf8("ipadd"))
        self.horizontalLayout.addWidget(self.ipadd)
        self.ed_ipaddress = QtGui.QLineEdit(self.widget)
        self.ed_ipaddress.setObjectName(_fromUtf8("ed_ipaddress"))
        self.horizontalLayout.addWidget(self.ed_ipaddress)
        self.widget1 = QtGui.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(60, 160, 291, 91))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btn_Connect = QtGui.QPushButton(self.widget1)
        self.btn_Connect.setObjectName(_fromUtf8("btn_Connect"))
        self.horizontalLayout_2.addWidget(self.btn_Connect)
        self.btn_disconnect = QtGui.QPushButton(self.widget1)
        self.btn_disconnect.setObjectName(_fromUtf8("btn_disconnect"))
        self.horizontalLayout_2.addWidget(self.btn_disconnect)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_connectstatus.setText(_translate("Dialog", "未连接", None))
        self.ipadd.setText(_translate("Dialog", "IPAddress", None))
        self.btn_Connect.setText(_translate("Dialog", "连接", None))
        self.btn_disconnect.setText(_translate("Dialog", "断开", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

