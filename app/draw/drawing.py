from PyQt5.QtWidgets import QWidget, QVBoxLayout
from app.draw.toolbar import ToolBar
from app.draw.canvas import Canvas

class DrawingArea(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(400, 400)

        self.toolbar = ToolBar(self)
        self.canvas = Canvas(self, self.toolbar)  # Pass the toolbar instance
        self.toolbar.setup_signals(self.canvas)  # Setup signals after canvas is initialized

        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)