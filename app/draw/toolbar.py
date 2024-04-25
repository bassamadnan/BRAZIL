from PyQt5.QtWidgets import QToolBar, QAction, QActionGroup
from PyQt5.QtGui import QPainter, QPen, QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize

class ToolBar(QToolBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Drawing Tools")
        self.setIconSize(QSize(32, 32))

        # Create an exclusive action group
        self.exclusive_group = QActionGroup(self)
        self.exclusive_group.setExclusive(True)

        # Line tool icon
        line_icon_pixmap = QPixmap(32, 32)
        line_icon_pixmap.fill(Qt.transparent)
        painter = QPainter(line_icon_pixmap)
        painter.setPen(QPen(Qt.black, 2))
        painter.drawLine(5, 25, 25, 5)
        painter.end()

        self.line_tool = QAction(QIcon(line_icon_pixmap), "Line", self)
        self.line_tool.setCheckable(True)
        self.line_tool.setChecked(True)
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