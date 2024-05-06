from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent
from app.draw.toolbar import ToolBar
from app.draw.canvas import Canvas

class DrawingArea(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(400, 400) #  minimum size, 400 by 400
        self.setFocusPolicy(Qt.StrongFocus)  # Enable keyboard focus

        self.toolbar = ToolBar(self)
        self.canvas = Canvas(self, self.toolbar)
        self.toolbar.setup_signals(self.canvas)

        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)


    # The Qt functions for control modifiers , and key functions allow cross platform
    # https://doc.qt.io/qt-5/qt.html#Key-enum
    def keyPressEvent(self, event):
        if isinstance(event, QKeyEvent):
            # print(f"event text: {event.text()}") # -> Cant listen to modifiers, use .key()
            print(f"event key: {event.key()}, modifiers: {event.modifiers()}")
            # LISTEN TO CONTROL KEY (CTRL)
            if event.modifiers() & Qt.ControlModifier:
                # CTRL + C
                if event.key() == Qt.Key_C:
                    print("ctrl+c / copy")
                    self.canvas.handle_copy_shortcut()
               
            # LISTEN TO DELETE KEY
            if event.key() == Qt.Key_Delete:
                print("del pressed")
                self.canvas.handle_delete_shortcut()