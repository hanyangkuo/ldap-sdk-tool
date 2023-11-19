from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

class CompareWindow(QDialog):
    def __init__(self, appctxt):
        super().__init__()
        uic.loadUi(appctxt.get_resource('./ui/compare.ui'), self)
        