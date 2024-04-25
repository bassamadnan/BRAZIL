from abc import ABC, abstractmethod
from PyQt5.QtCore import QPointF, QRectF

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def boundingRect(self):
        pass


class Rectangle(Shape):
    def __init__(self, top_left, bottom_right):
        self.top_left = QPointF(top_left)
        self.bottom_right = QPointF(bottom_right)

    def area(self):
        width = self.bottom_right.x() - self.top_left.x()
        height = self.bottom_right.y() - self.top_left.y()
        return width * height

    def perimeter(self):
        width = self.bottom_right.x() - self.top_left.x()
        height = self.bottom_right.y() - self.top_left.y()
        return 2 * (width + height)

    def boundingRect(self):
        x1, y1 = self.top_left.x(), self.top_left.y()
        x2, y2 = self.bottom_right.x(), self.bottom_right.y()
        return QRectF(x1, y1, x2 - x1, y2 - y1)