from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt, QRectF, QPointF
from app.shapes.rectangle import Rectangle
from app.shapes.line import Line
from app.utils.highlight import contains_line

class Canvas(QWidget):
    def __init__(self, parent=None, toolbar=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: blue;")
        self.shapes = []
        self.current_shape = None
        self.start_point = None
        self.dragging = False
        self.toolbar = toolbar
        self.selected_shape = None
        self.drag_start_pos = None
        self.shape_start_pos = None

    def paintEvent(self, event):
        painter = QPainter(self)
        for shape in self.shapes:
            if isinstance(shape, Line):
                painter.setPen(QPen(Qt.black, 3))
                painter.drawLine(shape.start_point, shape.end_point)

                # highlight the selected line
                if shape is self.selected_shape:
                    painter.setPen(QPen(Qt.yellow, 5))
                    painter.drawLine(shape.start_point, shape.end_point)
            elif isinstance(shape, Rectangle):
                shape_rect = shape.boundingRect()
                painter.setPen(QPen(Qt.black, 3))
                painter.drawRect(shape_rect)

                # highlight the rectangle
                if shape is self.selected_shape:
                    painter.setPen(QPen(Qt.yellow, 3))
                    painter.drawRect(shape_rect)

        # drawing logic
        if self.current_shape:
            if isinstance(self.current_shape, Line):
                painter.setPen(QPen(Qt.black, 3))
                painter.drawLine(self.current_shape.start_point, self.current_shape.end_point)
            elif isinstance(self.current_shape, Rectangle):
                shape_rect = self.current_shape.boundingRect()
                painter.setPen(QPen(Qt.black, 3))
                painter.drawRect(shape_rect)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.toolbar.mouse_tool.isChecked():
                # Check if the clicked point lies within any shape's bounding rectangle
                for shape in self.shapes:
                    if isinstance(shape, Rectangle) and shape.boundingRect().contains(event.pos()):
                        self.selected_shape = shape
                        self.dragging = True
                        self.drag_start_pos = event.pos()
                        self.shape_start_pos = QPointF(self.selected_shape.start_point)
                        self.update()
                        break
                    elif isinstance(shape, Line):
                        if contains_line(shape, event.pos()):
                            self.selected_shape = shape
                            self.dragging = True
                            self.drag_start_pos = event.pos()
                            self.shape_start_pos = QPointF(self.selected_shape.start_point)
                            self.update()
                            break
                else:
                    self.selected_shape = None
                    self.dragging = False
                    self.update()
            else:
                self.start_point = event.pos()
                if self.toolbar.line_tool.isChecked():
                    self.current_shape = Line(self.start_point, self.start_point)
                elif self.toolbar.rect_tool.isChecked():
                    self.current_shape = Rectangle(self.start_point, self.start_point)

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton and self.dragging:
            delta = event.pos() - self.drag_start_pos
            if isinstance(self.selected_shape, Rectangle):
                self.selected_shape.start_point += delta
                self.selected_shape.end_point += delta
            elif isinstance(self.selected_shape, Line):
                self.selected_shape.start_point += delta
                self.selected_shape.end_point += delta
            self.drag_start_pos = event.pos()
            self.update()
        else:
            if self.current_shape:
                if isinstance(self.current_shape, Line):
                    self.current_shape.end_point = event.pos()
                elif isinstance(self.current_shape, Rectangle):
                    self.current_shape.end_point = event.pos()
                self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.current_shape:
            self.shapes.append(self.current_shape)
            self.current_shape = None
        if event.button() == Qt.LeftButton:
            self.dragging = False
        self.start_point = None