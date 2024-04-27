from PyQt5.QtCore import QPointF, QRectF
from app.shapes.shape import Shape

class Rectangle(Shape):
    def __init__(self, start_point, end_point):
        self.start_point = QPointF(start_point)
        self.end_point = QPointF(end_point)

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