from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PyQt5.QtCore import QPointF
from app.draw.shapeEdit import ShapeEditDialog
from copy import deepcopy
from app.shapes.line import Line
from app.shapes.rectangle import Rectangle

class ShapeOptionsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)

        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(self.delete_button_clicked)
        edit_button = QPushButton("Edit")
        edit_button.clicked.connect(self.edit_button_clicked)
        copy_button = QPushButton("Copy")
        copy_button.clicked.connect(self.copy_button_clicked)

        layout.addWidget(delete_button)
        layout.addWidget(edit_button)
        layout.addWidget(copy_button)

    def delete_button_clicked(self):
        if self.parent().selected_shape:
            print(f"Delete button clicked for {self.parent().selected_shape}")
            self.parent().canvas.shape_manager.remove_shape(self.parent().selected_shape)
            self.parent().canvas.update()
            self.parent().selected_shape = None
            self.parent().hide_shape_options_menu()
        else:
            print("No shape selected")

    def edit_button_clicked(self):
        if self.parent().selected_shape:
            print(f"Edit button clicked for {self.parent().selected_shape}")
            edit_dialog = ShapeEditDialog(self.parent().selected_shape, self.parent())
            edit_dialog.exec_()
            self.parent().canvas.update()
        else:
            print("No shape selected")

    def copy_button_clicked(self):
        if self.parent().selected_shape:
            print(f"Copy button clicked for {self.parent().selected_shape}")
            new_shape = deepcopy(self.parent().selected_shape)
            shift_x = 5
            shift_y = 5
            if isinstance(new_shape, Line):
                new_shape.start_point += QPointF(shift_x, shift_y)
                new_shape.end_point += QPointF(shift_x, shift_y)
            elif isinstance(new_shape, Rectangle):
                new_shape.start_point += QPointF(shift_x, shift_y)
                new_shape.end_point += QPointF(shift_x, shift_y)

            self.parent().canvas.shape_manager.add_shape(new_shape)
            self.parent().canvas.update()
        else:
            print("No shape selected")
