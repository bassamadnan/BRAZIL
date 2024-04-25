from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from app.shapes.shape import Rectangle
from app.shapes.line import Line

class Canvas(QWidget):
    def __init__(self, parent=None, toolbar=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: blue;")
        self.shapes = []
        self.start_point = None
        self.dragging = False
        self.toolbar = toolbar  # Store the toolbar instance

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
        elif event.button() == Qt.MidButton:  # Middle mouse button (mouse wheel)
            self.dragging = True
            self.start_point = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.MidButton:  # Middle mouse button (mouse wheel)
            if self.dragging:
                delta = event.pos() - self.start_point
                self.move(self.pos() + delta)
                self.start_point = event.pos()
        else:
            if event.buttons() & Qt.LeftButton and self.start_point is not None:
                end_point = event.pos()
                if self.toolbar.line_tool.isChecked():
                    self.shapes.clear()  # clear previous shapes, TODO: REMOVE
                    new_shape = Line(self.start_point, end_point)
                    self.shapes.append(new_shape)
                elif self.toolbar.rect_tool.isChecked():
                    self.shapes.clear()  # clear previous shapes, TODO: REMOVE
                    new_shape = Rectangle(self.start_point, end_point)
                    self.shapes.append(new_shape)
                self.update()

    def mouseReleaseEvent(self, event):
        self.start_point = None
        if event.button() == Qt.MidButton:  # Middle mouse button (mouse wheel)
            self.dragging = False
            

