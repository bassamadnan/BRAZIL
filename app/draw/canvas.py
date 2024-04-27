from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
from app.shapes.rectangle import Rectangle
from app.shapes.line import Line
from app.shapes.shapeManager import ShapeManager

class Canvas(QWidget):
    def __init__(self, parent=None, toolbar=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: blue;")
        self.shape_manager = ShapeManager()
        self.start_point = None
        self.toolbar = toolbar

    def paintEvent(self, event):
        painter = QPainter(self)
        self.shape_manager.draw_shapes(painter)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.toolbar.mouse_tool.isChecked():
                self.shape_manager.select_shape(event.pos())
            else:
                self.start_point = event.pos()
                if self.toolbar.line_tool.isChecked():
                    self.shape_manager.current_shape = Line(self.start_point, self.start_point)
                elif self.toolbar.rect_tool.isChecked():
                    self.shape_manager.current_shape = Rectangle(self.start_point, self.start_point)
        self.update()

    def mouseMoveEvent(self, event):
        if self.shape_manager.current_shape:
            if isinstance(self.shape_manager.current_shape, Line):
                self.shape_manager.current_shape.end_point = event.pos()
            elif isinstance(self.shape_manager.current_shape, Rectangle):
                self.shape_manager.current_shape.end_point = event.pos()
        self.shape_manager.update_shape_position(event.pos())
        self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.shape_manager.current_shape:
            self.shape_manager.add_shape(self.shape_manager.current_shape)
            self.shape_manager.current_shape = None
        if event.button() == Qt.LeftButton:
            self.shape_manager.dragging = False
        self.start_point = None
        self.update()