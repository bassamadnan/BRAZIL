from PyQt5.QtGui import QPen
from PyQt5.QtCore import Qt, QPointF
from app.shapes.rectangle import Rectangle
from app.shapes.line import Line
from app.utils.highlight import contains_line

class ShapeManager:
    def __init__(self):
        self.shapes = []
        self.current_shape = None
        self.selected_shape = None
        self.dragging = False
        self.drag_start_pos = None
        self.shape_start_pos = None

    def add_shape(self, shape):
        self.shapes.append(shape)

    def remove_shape(self, shape):
        if shape in self.shapes:
            self.shapes.remove(shape)
            if self.selected_shape == shape:
                self.selected_shape = None
        # print(self.shapes)

    def select_shape(self, pos):
        for shape in self.shapes:
            if isinstance(shape, Rectangle) and shape.boundingRect().contains(pos):
                self.selected_shape = shape
                self.dragging = True
                self.drag_start_pos = pos
                self.shape_start_pos = QPointF(self.selected_shape.start_point)
                return
            elif isinstance(shape, Line):
                if contains_line(shape, pos):
                    self.selected_shape = shape
                    self.dragging = True
                    self.drag_start_pos = pos
                    self.shape_start_pos = QPointF(self.selected_shape.start_point)
                    return
        self.selected_shape = None
        self.dragging = False

    def update_shape_position(self, pos):
        if self.dragging:
            delta = pos - self.drag_start_pos
            if isinstance(self.selected_shape, Rectangle):
                self.selected_shape.start_point += delta
                self.selected_shape.end_point += delta
            elif isinstance(self.selected_shape, Line):
                self.selected_shape.start_point += delta
                self.selected_shape.end_point += delta
            self.drag_start_pos = pos

    def draw_shapes(self, painter):
        for shape in self.shapes:
            if isinstance(shape, Line):
                painter.setPen(QPen(shape.color, 3))
                painter.drawLine(shape.start_point, shape.end_point)

                # highlight the selected line
                if shape is self.selected_shape:
                    painter.setPen(QPen(Qt.yellow, 5))
                    painter.drawLine(shape.start_point, shape.end_point)
            elif isinstance(shape, Rectangle):
                shape_rect = shape.boundingRect()
                painter.setPen(QPen(shape.color, 3))
                if shape.rounded:
                    painter.drawRoundedRect(shape_rect, 10, 10)  # Adjust the radius as needed
                else:
                    painter.drawRect(shape_rect)

                # highlight the rectangle
                if shape is self.selected_shape:
                    painter.setPen(QPen(Qt.yellow, 3))
                    if shape.rounded:
                        painter.drawRoundedRect(shape_rect, 10, 10)
                    else:
                        painter.drawRect(shape_rect)

        # drawing logic
        if self.current_shape:
            if isinstance(self.current_shape, Line):
                painter.setPen(QPen(Qt.black, 3))
                painter.drawLine(self.current_shape.start_point, self.current_shape.end_point)
            elif isinstance(self.current_shape, Rectangle):
                shape_rect = self.current_shape.boundingRect()
                painter.setPen(QPen(Qt.black, 3))
                if self.current_shape.rounded:
                    painter.drawRoundedRect(shape_rect, 10, 10)
                else:
                    painter.drawRect(shape_rect)