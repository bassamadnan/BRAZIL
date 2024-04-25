from PyQt5.QtWidgets import QToolBar, QAction, QActionGroup
from PyQt5.QtGui import QPainter, QPen, QIcon, QPixmap, QPolygon
from PyQt5.QtCore import Qt, QSize, QPoint

class ToolBar(QToolBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.window = self.window()  # Get the reference to the main window
        self.setWindowTitle("Drawing Tools")
        self.setIconSize(QSize(32, 32))

        # Create an exclusive action group
        self.exclusive_group = QActionGroup(self)
        self.exclusive_group.setExclusive(True)

        # Mouse tool icon
        mouse_icon_pixmap = QPixmap(32, 32)
        mouse_icon_pixmap.fill(Qt.transparent)
        painter = QPainter(mouse_icon_pixmap)
        painter.setPen(QPen(Qt.black, 2))
        points = [QPoint(10, 20), QPoint(25, 16), QPoint(25, 10), QPoint(30, 16), QPoint(30, 20)]
        painter.drawPolyline(QPolygon(points))
        painter.end()

        self.mouse_tool = QAction(QIcon(mouse_icon_pixmap), "Mouse", self)
        self.mouse_tool.setCheckable(True)
        self.mouse_tool.setChecked(True)
        self.exclusive_group.addAction(self.mouse_tool)
        self.addAction(self.mouse_tool)

        # Line tool icon
        line_icon_pixmap = QPixmap(32, 32)
        line_icon_pixmap.fill(Qt.transparent)
        painter = QPainter(line_icon_pixmap)
        painter.setPen(QPen(Qt.black, 2))
        painter.drawLine(5, 25, 25, 5)
        painter.end()

        self.line_tool = QAction(QIcon(line_icon_pixmap), "Line", self)
        self.line_tool.setCheckable(True)
        # self.line_tool.setChecked(True)
        self.exclusive_group.addAction(self.line_tool)
        self.addAction(self.line_tool)

        # Rectangle tool icon
        rect_icon_pixmap = QPixmap(32, 32)
        rect_icon_pixmap.fill(Qt.transparent)
        painter = QPainter(rect_icon_pixmap)
        painter.setPen(QPen(Qt.black, 2))
        painter.drawRect(5, 5, 22, 22)
        painter.end()

        self.rect_tool = QAction(QIcon(rect_icon_pixmap), "Rectangle", self)
        self.rect_tool.setCheckable(True)
        self.exclusive_group.addAction(self.rect_tool)
        self.addAction(self.rect_tool)


        self.addSeparator()