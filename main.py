import sys
from PyQt5.QtWidgets import QApplication
from app.draw.window import MainWindow

def initialize():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

initialize()