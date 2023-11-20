from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
import os

appdataPath = os.path.join(os.getenv('LOCALAPPDATA'), 'LDAPAdmin')

class CompareWindow(QDialog):
    def __init__(self, appctxt):
        super().__init__()
        uic.loadUi(appctxt.get_resource('./ui/compare.ui'), self)
        connectionsPath = os.path.join(appdataPath,'Connections')
        cfg = [f for f in os.listdir(connectionsPath) 
               if os.path.isfile(os.path.join(connectionsPath, f)) and f.endswith(".cfg")]
        self.comboBox_source.addItems(cfg)
        self.comboBox_target.addItems(cfg)