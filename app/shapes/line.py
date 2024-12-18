from PyQt5.QtCore import QPointF, QRectF, Qt
from PyQt5.QtGui import QColor
from app.shapes.shape import Shape
from app.utils.colors import get_color_name
from app.utils.highlight import distance_from_edge
from app.utils.xml_indent import indent_xml

class Line(Shape):
    def __init__(self, start_point, end_point, color=QColor(Qt.black)):
        self.start_point = QPointF(start_point)
        self.end_point = QPointF(end_point)
        self.color = color
        self.belonging_group = None

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

    def distance(self, point):
        x = point.x()
        y = point.y()
        x1 = self.start_point.x()
        y1 = self.start_point.y()
        x2 = self.end_point.x()
        y2 = self.end_point.y()
        return distance_from_edge(x1, y1, x2, y2, x, y)

    def export(self):
        xml = indent_xml("<line>", 0)
        xml += indent_xml("<begin>", 1)
        xml += indent_xml(f"<x>{int(self.start_point.x())}</x>", 2)
        xml += indent_xml(f"<y>{int(self.start_point.y())}</y>", 2)
        xml += indent_xml("</begin>", 1)
        xml += indent_xml("<end>", 1)
        xml += indent_xml(f"<x>{int(self.end_point.x())}</x>", 2)
        xml += indent_xml(f"<y>{int(self.end_point.y())}</y>", 2)
        xml += indent_xml("</end>", 1)
        xml += indent_xml(f"<color>{get_color_name(self.color.name())}</color>", 1)
        xml += indent_xml("</line>", 0)
        return xml

    def __repr__(self):
        return f"Line(start={self.start_point}, end={self.end_point}, color={self.color.name()}) addr : {hex(id(self))}"
