import sys
sys.setrecursionlimit(10**6)

from PyQt5.QtWidgets import QApplication
from app.draw.window import MainWindow

def run():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

run()