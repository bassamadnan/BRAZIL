from PyQt5.QtCore import QPointF, QLineF, Qt
from PyQt5.QtGui import QColor

class Line:
    def __init__(self, start_point, end_point, color=QColor(Qt.black)):
        self.start_point = QPointF(start_point)
        self.end_point = QPointF(end_point)
        self.color = color

    def boundingRect(self):
        line = QLineF(self.start_point, self.end_point)
        pen_width = 3  # thickness
        return line.boundingRect().adjusted(-pen_width / 2, -pen_width / 2, pen_width / 2, pen_width / 2)

    def length(self):
        dx = self.end_point.x() - self.start_point.x()
        dy = self.end_point.y() - self.start_point.y()
        return (dx ** 2 + dy ** 2) ** 0.5
    
    def __repr__(self):
        return f"Line(start={self.start_point}, end={self.end_point}, color={self.color.name()})"