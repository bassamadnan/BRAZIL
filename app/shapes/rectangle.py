from PyQt5.QtCore import QPointF, QRectF, Qt
from app.shapes.shape import Shape
from PyQt5.QtGui import QColor

class Rectangle(Shape):
    def __init__(self, start_point, end_point, rounded=False, color=QColor(Qt.black)):
        self.start_point = QPointF(start_point)
        self.end_point = QPointF(end_point)
        self.rounded = rounded
        self.color = color

    def area(self):
        width = abs(self.end_point.x() - self.start_point.x())
        height = abs(self.end_point.y() - self.start_point.y())
        return width * height

    def perimeter(self):
        width = abs(self.end_point.x() - self.start_point.x())
        height = abs(self.end_point.y() - self.start_point.y())
        return 2 * (width + height)

    def boundingRect(self):
        x1 = min(self.start_point.x(), self.end_point.x())
        y1 = min(self.start_point.y(), self.end_point.y())
        x2 = max(self.start_point.x(), self.end_point.x())
        y2 = max(self.start_point.y(), self.end_point.y())
        return QRectF(x1, y1, x2 - x1, y2 - y1)
    
    def __repr__(self):
        return f"Rectangle(start={self.start_point}, end={self.end_point}, rounded={self.rounded}, color={self.color.name()})"
