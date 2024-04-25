import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtCore import Qt
from app.shapes.shape import Rectangle
from app.shapes.line import Line

class DrawingArea(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(400, 400)
        self.setStyleSheet("background-color: white;")
        self.shapes = [] # stores shapes

    def paintEvent(self, event):
        painter = QPainter(self)
        for shape in self.shapes:
            # Draw each shape using its boundingRect() and paint methods
            shape_rect = shape.boundingRect()
            painter.setPen(QPen(Qt.black, 3))
            painter.drawRect(shape_rect)
    def mousePressEvent(self, event):
        self.start_point = event.pos()  # Store the start position
        print(self.start_point)

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            # dragging the mouse
            end_point = event.pos()
            new_shape = Line(self.start_point, end_point)
            self.shapes.append(new_shape)
            self.update()  # Trigger a repaint

    def mouseReleaseEvent(self, event):
        # TODO ??
        pass    
    
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

