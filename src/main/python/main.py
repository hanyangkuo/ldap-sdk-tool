from fbs_runtime.application_context.PyQt5 import ApplicationContext
import PyQt5.QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5 import uic
from ui.compare import CompareWindow
import sys
import os
absFilePath = os.path.abspath(__file__)
appdataPath = os.path.join(os.getenv('LOCALAPPDATA'), 'LDAPAdmin')


class MainWindow(QMainWindow):
    def __init__(self, appctxt):
        super().__init__()
        self.context = appctxt
        uic.loadUi(self.context.get_resource('./ui/main.ui'), self)
        self.actionConnection.triggered.connect(self.openConnections)
        self.actionCompare.triggered.connect(self.compareLdaps)

    def openConnections(self):
        ConnectionsForm, ConnectionsWindow = uic.loadUiType(appctxt.get_resource('./ui/connections.ui'))
        connectionsWindow = ConnectionsWindow()
        connectionsForm = ConnectionsForm()
        connectionsForm.setupUi(connectionsWindow)
        connectionsWindow.setModal(True)
        connectionsWindow.show()
        connectionsWindow.exec_()
        return
    
    def compareLdaps(self):
        compareWindow = CompareWindow(self.context)
        compareWindow.setModal(True)
        compareWindow.show()
        if compareWindow.exec_() == QDialog.Accepted:
            sourceCfg = compareWindow.comboBox_source.currentText()
            targetCfg = compareWindow.comboBox_target.currentText()
            basedn = compareWindow.lineEdit_basedn.text()
            filter = compareWindow.lineEdit_filter.text()
            attributes = compareWindow.lineEdit_attributes.text()
            scope = compareWindow.comboBox_scope.currentText()
            return
        print("Cancel")


if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    mainWindow = MainWindow(appctxt)
    mainWindow.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)