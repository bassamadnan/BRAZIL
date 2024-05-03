from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QMenu, QToolButton, QFileDialog
from PyQt5.QtCore import QPointF
from app.draw.shapeEdit import ShapeEditDialog
from copy import deepcopy
from app.shapes.line import Line
from app.shapes.rectangle import Rectangle
from app.shapes.group import Group
from app.utils.window_instance import get_window
import os

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
        group_button = QPushButton("Group")
        group_button.clicked.connect(self.group_button_clicked)
        group_button.clicked.connect(self.group_button_clicked)
        ungroup_button = QPushButton("Ungroup")
        ungroup_button.clicked.connect(self.ungroup_button_clicked)
        debug_button = QPushButton("Debug")
        debug_button.clicked.connect(self.debug_print)

        file_menu = QMenu(self)
        import_action = file_menu.addAction("Import")
        import_action.triggered.connect(self.import_file)
        export_action = file_menu.addAction("Export")
        export_action.triggered.connect(self.export_file)
        file_button = QToolButton(self)
        file_button.setText("File")
        file_button.setMenu(file_menu)
        file_button.setPopupMode(QToolButton.InstantPopup)
        
        layout.addWidget(delete_button)
        layout.addWidget(edit_button)
        layout.addWidget(copy_button)
        layout.addWidget(group_button)
        layout.addWidget(ungroup_button)
        layout.addWidget(debug_button)
        layout.addWidget(file_button)


    def edit_button_clicked(self):
        if self.parent().selected_shape:
            print(f"Edit button clicked for {self.parent().selected_shape}")
            edit_dialog = ShapeEditDialog(self.parent().selected_shape, self.parent())
            edit_dialog.exec_()
            self.parent().canvas.update()
        else:
            print("No shape selected")

    
    def delete_button_clicked(self):
        if self.parent().selected_shape:
            print(f"Delete button clicked for {self.parent().selected_shape}")
            if isinstance(self.parent().selected_shape, Group):
                self.parent().canvas.shape_manager.remove_group(self.parent().selected_shape)
            else:
                self.parent().canvas.shape_manager.remove_shape(self.parent().selected_shape)
            self.parent().canvas.update()
            self.parent().selected_shape = None
            self.parent().hide_shape_options_menu()
        else:
            print("No shape selected")


    def copy_button_clicked(self):
        if self.parent().selected_shape:
            print(f"Copy button clicked for {self.parent().selected_shape}")
            if isinstance(self.parent().selected_shape, Group):
                new_group = self.copy_group(self.parent().selected_shape)
                shift_x = 5
                shift_y = 5
                self.shift_group_position(new_group, shift_x, shift_y)
                self.parent().canvas.shape_manager.add_group(new_group)
            else:
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

    def copy_group(self, group):
        new_group = Group()
        for obj in group.objects:
            if isinstance(obj, Group):
                new_subgroup = self.copy_group(obj)
                new_group.add_object(new_subgroup)
            else:
                new_shape = deepcopy(obj)
                new_group.add_object(new_shape)
        return new_group
    
    def group_button_clicked(self):
        if self.parent().canvas.shape_manager.selected_shapes or self.parent().canvas.shape_manager.selected_groups:
            self.parent().canvas.shape_manager.create_group()
            self.parent().canvas.update()

    def ungroup_button_clicked(self):
        if self.parent().selected_shape and isinstance(self.parent().selected_shape, Group):
            self.parent().canvas.shape_manager.ungroup(self.parent().selected_shape)
            self.parent().selected_shape = None  
            self.parent().canvas.update()
        else:
            print("No group selected")

    def debug_print(self):
        self.parent().canvas.shape_manager.iterate_objects()

    def shift_group_position(self, group, shift_x, shift_y):
        for obj in group.objects:
            if isinstance(obj, Group):
                self.shift_group_position(obj, shift_x, shift_y)
            elif isinstance(obj, Rectangle):
                obj.start_point += QPointF(shift_x, shift_y)
                obj.end_point += QPointF(shift_x, shift_y)
            elif isinstance(obj, Line):
                obj.start_point += QPointF(shift_x, shift_y)
                obj.end_point += QPointF(shift_x, shift_y)

    def export_file(self):
        win = get_window()
        xml_string = win.drawing_area.canvas.shape_manager.export_all()
        xml_file_filter = "XML Files (*.xml)"
        file_path, _ = QFileDialog.getSaveFileName(self, "Export XML File", "", xml_file_filter)

        if file_path:
            # Remove the extension if it already exists
            root, ext = os.path.splitext(file_path)
            if ext.lower() == '.xml':
                file_path = root

            # Add the .xml extension if it's not present
            if not file_path.endswith('.xml'):
                file_path += '.xml'

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(xml_string)

    def import_file(self):
        pass