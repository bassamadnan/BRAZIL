import sys
sys.setrecursionlimit(10**6)

from PyQt5.QtWidgets import QApplication
from app.draw.window import MainWindow
from  app.utils import window_instance

def run():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window_instance.set_window(window)
    sys.exit(app.exec_())

run()