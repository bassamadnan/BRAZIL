from PyQt5.QtWidgets import QToolBar, QAction, QActionGroup, QWidgetAction
from PyQt5.QtCore import QSize
from app.draw.shapeOptions import ShapeOptionsWidget
from app.utils.tools import create_line_tool_icon, create_mouse_tool_icon, create_rect_tool_icon

class ToolBar(QToolBar):
    """
    The acutal toolbar class, which initializes the icons of shapes and the mouse and other options
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.window = self.window()  # Get the reference to the main window
        self.setWindowTitle("Drawing Tools")
        self.setIconSize(QSize(32, 32))

        self.exclusive_group = QActionGroup(self)
        self.exclusive_group.setExclusive(True)

        self.mouse_tool = QAction(create_mouse_tool_icon(), "Mouse", self)
        self.mouse_tool.setCheckable(True)
        self.mouse_tool.setChecked(True)
        self.exclusive_group.addAction(self.mouse_tool)
        self.addAction(self.mouse_tool)

        self.line_tool = QAction(create_line_tool_icon(), "Line", self)
        self.line_tool.setCheckable(True)
        self.exclusive_group.addAction(self.line_tool)
        self.addAction(self.line_tool)

        self.rect_tool = QAction(create_rect_tool_icon(), "Rectangle", self)
        self.rect_tool.setCheckable(True)
        self.exclusive_group.addAction(self.rect_tool)
        self.addAction(self.rect_tool)

        self.addSeparator()

        self.shape_options_widget = ShapeOptionsWidget(self)
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
        self.show_shape_options_menu()

    def handle_shape_deselected(self):
        self.selected_shape = None
        self.hide_shape_options_menu()

    def setup_signals(self, canvas):
        self.canvas = canvas
        canvas.shapeSelected.connect(self.handle_shape_selected)
        canvas.shapeDeselected.connect(self.handle_shape_deselected)
        canvas.shape_options_widget = self.shape_options_widget