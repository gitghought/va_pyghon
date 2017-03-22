# -*- coding: utf-8 -*-

import os
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QDialog
from PyQt4 import QtGui, QtCore
from Ui_pq_get_dev import Ui_Dialog
import sys
from vb_get_dev import Dev

class pq_get_dev_resp(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
        self.dev = Dev()
    
    @pyqtSignature("QString")
    def on_label_linkHovered(self, link):
        pass
    
    @pyqtSignature("")
    def on_btn_Connect_clicked(self):
#         self.ipadd.setText("good luck")
        ipstr = self.ed_ipaddress.text()
        print (type(ipstr))

        rIPStr = str(ipstr)
        if ipstr == '' :
            return
        print(os.path.abspath("."))

        ip = self.dev.dicsUI["connect"](rIPStr)
        if ip != '':
            self.label_connectstatus.setText("Connectted")
        else :
            self.label_connectstatus.setText("未连接，请检查我网络")
    
    @pyqtSignature("")
    def on_btn_disconnect_clicked(self):
        self.dev.dics["disconnect"]()
        pass
       
if __name__ == "__main__" :
    app = QtGui.QApplication(sys.argv)
    widget = pq_get_dev_resp()
    widget.show()
    sys.exit(app.exec_())

