from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt, pyqtSignal
from app.shapes.rectangle import Rectangle
from app.shapes.line import Line
from app.shapes.shapeManager import ShapeManager

class Canvas(QWidget):
    """
    Canvas relaetd functions, responsible for how user interacts with the GUI
    """
    shapeSelected = pyqtSignal(object)  # signal to emit the selected shape
    shapeDeselected = pyqtSignal()  #  signal to emit when no shape is selected

    def __init__(self, parent=None, toolbar=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: blue;")
        self.shape_manager = ShapeManager()
        self.start_point = None
        self.toolbar = toolbar
        self.toolbar.hide_shape_options_menu()

    def paintEvent(self, event):
        painter = QPainter(self)
        self.shape_manager.draw_shapes(painter)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if event.modifiers() & Qt.ControlModifier:
                # Toggle selection for the shape at the clicked position
                self.toggle_selection(event.pos())
            else:
                # Deselect previously selected shapes and select a new one
                self.shape_manager.selected_shapes.clear()
                if self.toolbar.mouse_tool.isChecked():
                    self.shape_manager.select_shape(event.pos())
                    if self.shape_manager.selected_shape:
                        self.shapeSelected.emit(self.shape_manager.selected_shape)
                        self.toolbar.show_shape_options_menu()
                    else:
                        self.shapeDeselected.emit()
                        self.toolbar.hide_shape_options_menu()
                else:
                    self.start_point = event.pos()
                    if self.toolbar.line_tool.isChecked():
                        self.shape_manager.current_shape = Line(self.start_point, self.start_point)
                    elif self.toolbar.rect_tool.isChecked():
                        self.shape_manager.current_shape = Rectangle(self.start_point, self.start_point)
        elif event.button() == Qt.RightButton:
            self.shape_manager.select_shape(event.pos())
            if self.shape_manager.selected_shape:
                self.shapeSelected.emit(self.shape_manager.selected_shape)
                self.toolbar.show_shape_options_menu()
            else:
                self.shapeDeselected.emit()
                self.toolbar.hide_shape_options_menu()

        self.update()

    def mouseMoveEvent(self, event):
        if self.shape_manager.current_shape:
            if isinstance(self.shape_manager.current_shape, Line):
                self.shape_manager.current_shape.end_point = event.pos()
            elif isinstance(self.shape_manager.current_shape, Rectangle):
                self.shape_manager.current_shape.end_point = event.pos()
        self.shape_manager.update_shape_position(event.pos())
        self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.shape_manager.current_shape:
            self.shape_manager.add_shape(self.shape_manager.current_shape)
            self.shape_manager.current_shape = None
        if event.button() == Qt.LeftButton:
            self.shape_manager.dragging = False
        self.start_point = None
        self.update()

    def handle_copy_shortcut(self):
        if self.shape_manager.selected_shape:
            self.toolbar.shape_options_widget.copy_button_clicked()

    def handle_delete_shortcut(self):
        if self.shape_manager.selected_shape:
            self.toolbar.shape_options_widget.delete_button_clicked()

    def toggle_selection(self, pos):
        # Check if any group is clicked
        for group in self.shape_manager.groups:
            if group.boundingRect().contains(pos):
                self.shape_manager.toggle_selection(group)
                return

        # Check if any individual shape is clicked
        shape = self.shape_manager.get_shape_at_pos(pos)
        if shape:
            self.shape_manager.toggle_selection(shape)
        else:
            # If no shape is clicked and no Ctrl key is pressed, clear the selection
            if not QApplication.keyboardModifiers() & Qt.ControlModifier:
                self.shape_manager.selected_shapes.clear()

        self.update()
