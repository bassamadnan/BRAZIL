from PyQt5.QtCore import QPointF, QRectF, Qt
from PyQt5.QtGui import QColor
from app.shapes.shape import Shape
from app.utils.colors import get_color_name
from app.utils.highlight import distance_from_edge

class Rectangle(Shape):
    def __init__(self, start_point, end_point, rounded=False, color=QColor(Qt.black)):
        self.start_point = QPointF(start_point)
        self.end_point = QPointF(end_point)
        self.rounded = rounded
        self.color = color
        self.belonging_group = None

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

    def distance(self, point):
        x = point.x()
        y = point.y()
        x_min = self.start_point.x()
        y_min = self.start_point.y()
        x_max = self.end_point.x()
        y_max = self.end_point.y()
        dist = []
        dist.append(distance_from_edge(x_min, y_min, x_max, y_min, x, y))
        dist.append(distance_from_edge(x_max, y_min, x_max, y_max, x, y))
        dist.append(distance_from_edge(x_max, y_max, x_min, y_max, x, y))
        dist.append(distance_from_edge(x_min, y_max, x_min, y_min, x, y))
        return min(dist)

    def export(self):
        xml = "<rectangle>\n"
        xml += "<upper-left>\n"
        xml += f"<x>{int(self.start_point.x())}</x>\n"
        xml += f"<y>{int(self.start_point.y())}</y>\n"
        xml += "</upper-left>\n"
        xml += "<lower-right>\n"
        xml += f"<x>{int(self.end_point.x())}</x>\n"
        xml += f"<y>{int(self.end_point.y())}</y>\n"
        xml += "</lower-right>\n"
        xml += f"<color>{get_color_name(self.color.name())}</color>\n"
        if (self.rounded):
            xml += "<corner>rounded</corner>\n"
        else:
            xml += "<corner>square</corner>\n"
        xml += "</rectangle>\n"
        return xml

    def __repr__(self):
        return f"Rectangle(start={self.start_point}, end={self.end_point}, rounded={self.rounded}, color={self.color.name()} addr : {hex(id(self))})"
