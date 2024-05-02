from PyQt5.QtCore import QPointF, QRectF, Qt
from PyQt5.QtGui import QColor
from app.utils.tools import get_color_name

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

    def export(self):
        xml = "<line>\n"
        xml += "<begin>\n"
        xml += f"<x>{int(self.start_point.x())}</x>\n"
        xml += f"<y>{int(self.start_point.y())}</y>\n"
        xml += "</begin>\n"
        xml += "<end>\n"
        xml += f"<x>{int(self.end_point.x())}</x>\n"
        xml += f"<y>{int(self.end_point.y())}</y>\n"
        xml += "</end>\n"
        xml += f"<color>{get_color_name(self.color.name())}</color>\n"
        xml += "</line>\n"
        return xml

    def __repr__(self):
        return f"Line(start={self.start_point}, end={self.end_point}, color={self.color.name()})"