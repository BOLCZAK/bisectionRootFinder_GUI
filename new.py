from app import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    with open('style.css', 'r') as f:
        app.setStyleSheet(f.read())
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())