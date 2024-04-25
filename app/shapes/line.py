from PyQt5.QtCore import QPointF, QRectF


class Line:
    def __init__(self, start_point, end_point):
        self.start_point = QPointF(start_point)
        self.end_point = QPointF(end_point)

    def boundingRect(self):
        x1, y1 = self.start_point.x(), self.start_point.y()
        x2, y2 = self.end_point.x(), self.end_point.y()
        left = min(x1, x2)
        top = min(y1, y2)
        right = max(x1, x2)
        bottom = max(y1, y2)
        return QRectF(left, top, right - left, bottom - top)

    def length(self):
        dx = self.end_point.x() - self.start_point.x()
        dy = self.end_point.y() - self.start_point.y()
        return (dx ** 2 + dy ** 2) ** 0.5

