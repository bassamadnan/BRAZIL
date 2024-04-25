from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMainWindow
from app.draw.drawing import DrawingArea

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Drawing App")
        central_widget = QWidget()
        layout = QVBoxLayout()
        self.drawing_area = DrawingArea()
        layout.addWidget(self.drawing_area)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

