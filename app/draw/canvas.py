from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from app.shapes.shape import Rectangle
from app.shapes.line import Line
from app.draw.toolbar import ToolBar


class DrawingArea(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(400, 400)
        self.setStyleSheet("background-color: blue;")
        self.shapes = []
        self.current_tool = "line"
        self.start_point = None

        self.toolbar = ToolBar(self)

        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addStretch()
        self.setLayout(layout)

    def paintEvent(self, event):
        painter = QPainter(self)
        for shape in self.shapes:
            if isinstance(shape, Line):
                painter.setPen(QPen(Qt.black, 3))
                painter.drawLine(shape.start_point, shape.end_point)
            elif isinstance(shape, Rectangle):
                shape_rect = shape.boundingRect()
                painter.setPen(QPen(Qt.black, 3))
                painter.drawRect(shape_rect)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start_point = event.pos()

    def mouseMoveEvent(self, event): 
        if event.buttons() & Qt.LeftButton and self.start_point is not None:
            end_point = event.pos()
            if self.toolbar.line_tool.isChecked():
                self.shapes.clear()  # clear previous shapes , TDOO REMOVE
                new_shape = Line(self.start_point, end_point)
                self.shapes.append(new_shape)
            elif self.toolbar.rect_tool.isChecked():
                self.shapes.clear()  # clear previous shapes, TODO REMOVE
                new_shape = Rectangle(self.start_point, end_point)
                self.shapes.append(new_shape)
            self.update()

    def mouseReleaseEvent(self, event):
        self.start_point = None

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
