from PyQt5.QtCore import QPointF, QRectF, Qt
from PyQt5.QtGui import QColor

class Line:
    def __init__(self, start_point, end_point, color=QColor(Qt.black)):
        self.start_point = QPointF(start_point)
        self.end_point = QPointF(end_point)
        self.color = color

    def boundingRect(self):
        x1 = min(self.start_point.x(), self.end_point.x())
        y1 = min(self.start_point.y(), self.end_point.y())
        x2 = max(self.start_point.x(), self.end_point.x())
        y2 = max(self.start_point.y(), self.end_point.y())
        return QRectF(x1, y1, x2 - x1, y2 - y1)
    
    def length(self):
        dx = self.end_point.x() - self.start_point.x()
        dy = self.end_point.y() - self.start_point.y()
        return (dx ** 2 + dy ** 2) ** 0.5
    
    def __repr__(self):
        return f"Line(start={self.start_point}, end={self.end_point}, color={self.color.name()})"