from PyQt5.QtGui import QIcon, QPixmap, QPainter, QPen, QPolygon
from PyQt5.QtCore import Qt, QPoint

def create_mouse_tool_icon():
    mouse_icon_pixmap = QPixmap(32, 32)
    mouse_icon_pixmap.fill(Qt.transparent)
    painter = QPainter(mouse_icon_pixmap)
    painter.setPen(QPen(Qt.black, 2))
    points = [QPoint(6, 6), QPoint(24, 12), QPoint(12, 24), QPoint(6, 6)]
    painter.drawPolyline(QPolygon(points))
    points = [QPoint(18, 18), QPoint(28, 28)]
    painter.drawPolyline(QPolygon(points))
    painter.end()
    return QIcon(mouse_icon_pixmap)

def create_line_tool_icon():
    line_icon_pixmap = QPixmap(32, 32)
    line_icon_pixmap.fill(Qt.transparent)
    painter = QPainter(line_icon_pixmap)
    painter.setPen(QPen(Qt.black, 2))
    painter.drawLine(5, 25, 25, 5)
    painter.end()
    return QIcon(line_icon_pixmap)

def create_rect_tool_icon():
    rect_icon_pixmap = QPixmap(32, 32)
    rect_icon_pixmap.fill(Qt.transparent)
    painter = QPainter(rect_icon_pixmap)
    painter.setPen(QPen(Qt.black, 2))
    painter.drawRect(5, 5, 22, 22)
    painter.end()
    return QIcon(rect_icon_pixmap)
