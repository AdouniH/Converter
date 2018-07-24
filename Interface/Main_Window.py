# -*- coding: utf-8 -*-
"""
@author: Houssem ADOUNI
"""

import sys
from PyQt4.QtGui  import *
from Interface import Conversion_Layout

class fenetre_de_base(QMainWindow):

    def __init__(self, parent=None):
        super(fenetre_de_base, self).__init__(parent)
        self.setGeometry(300,100,300,200)
        self.setMaximumSize(300,200)
        self.inside = Conversion_Layout.Layout_conv(self)
        self.setCentralWidget(self.inside)


if __name__=="__main__":
    app = QApplication([])
    converter = fenetre_de_base()
    converter.show()
    sys.exit(app.exec_())