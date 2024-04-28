from PyQt5.QtWidgets import QToolBar, QAction, QActionGroup, QWidget, QHBoxLayout, QPushButton, QWidgetAction
from PyQt5.QtGui import QPainter, QPen, QIcon, QPixmap, QPolygon
from PyQt5.QtCore import Qt, QSize, QPoint
from app.draw.shapeEdit import ShapeEditDialog

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

        # Shape options widget
        self.shape_options_widget = QWidget()
        self.shape_options_layout = QHBoxLayout(self.shape_options_widget)

        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(self.handle_delete_button_click)
        edit_button = QPushButton("Edit")
        edit_button.clicked.connect(self.handle_edit_button_click)
        copy_button = QPushButton("Copy")
        copy_button.clicked.connect(self.handle_copy_button_click)

        self.shape_options_layout.addWidget(delete_button)
        self.shape_options_layout.addWidget(edit_button)
        self.shape_options_layout.addWidget(copy_button)

        shape_options_widget_action = QWidgetAction(self)
        shape_options_widget_action.setDefaultWidget(self.shape_options_widget)
        self.addAction(shape_options_widget_action)

        self.shape_options_widget.hide()
        self.selected_shape = None
        self.canvas = None

    def setup_signals(self, canvas):
        self.canvas = canvas
        canvas.shapeSelected.connect(self.handle_shape_selected)
        canvas.shapeDeselected.connect(self.handle_shape_deselected)

    def show_shape_options_menu(self):
        self.shape_options_widget.show()

    def hide_shape_options_menu(self):
        self.shape_options_widget.hide()

    def handle_shape_selected(self, shape):
        self.selected_shape = shape
        print(f"Selected shape: {self.selected_shape}")
        # Enable the edit/copy/delete buttons here
        pass

    def handle_shape_deselected(self):
        self.selected_shape = None
        # Disable the edit/copy/delete buttons here
        pass

    def handle_delete_button_click(self):
        if self.selected_shape:
            print(f"Delete button clicked for {self.selected_shape}")
            self.canvas.shape_manager.remove_shape(self.selected_shape)
            self.canvas.update()
            self.selected_shape = None
            self.hide_shape_options_menu()
        else:
            print("No shape selected")

    def handle_edit_button_click(self):
        if self.selected_shape:
            print(f"Edit button clicked for {self.selected_shape}")
            edit_dialog = ShapeEditDialog(self.selected_shape, self)
            edit_dialog.exec_()
            # Update the canvas after closing the dialog
            self.canvas.update()
        else:
            print("No shape selected")

    def handle_copy_button_click(self):
        if self.selected_shape:
            print(f"Copy button clicked for {self.selected_shape}")
        else:
            print("No shape selected")
        # Add your copy functionality here