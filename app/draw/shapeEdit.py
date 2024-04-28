from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import QPointF
from app.shapes.rectangle import Rectangle
from app.shapes.line import Line

class ShapeEditDialog(QDialog):
    def __init__(self, shape, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Edit Shape")
        self.shape = shape

        layout = QVBoxLayout()

        if isinstance(shape, Line):
            start_point_label = QLabel("Start Point:")
            self.start_point_x_input = QLineEdit(str(shape.start_point.x()))
            self.start_point_y_input = QLineEdit(str(shape.start_point.y()))
            start_point_layout = QVBoxLayout()
            start_point_layout.addWidget(self.start_point_x_input)
            start_point_layout.addWidget(self.start_point_y_input)
            layout.addWidget(start_point_label)
            layout.addLayout(start_point_layout)

            end_point_label = QLabel("End Point:")
            self.end_point_x_input = QLineEdit(str(shape.end_point.x()))
            self.end_point_y_input = QLineEdit(str(shape.end_point.y()))
            end_point_layout = QVBoxLayout()
            end_point_layout.addWidget(self.end_point_x_input)
            end_point_layout.addWidget(self.end_point_y_input)
            layout.addWidget(end_point_label)
            layout.addLayout(end_point_layout)

        elif isinstance(shape, Rectangle):
            start_point_label = QLabel("Start Point:")
            self.start_point_x_input = QLineEdit(str(shape.start_point.x()))
            self.start_point_y_input = QLineEdit(str(shape.start_point.y()))
            start_point_layout = QVBoxLayout()
            start_point_layout.addWidget(self.start_point_x_input)
            start_point_layout.addWidget(self.start_point_y_input)
            layout.addWidget(start_point_label)
            layout.addLayout(start_point_layout)

            end_point_label = QLabel("End Point:")
            self.end_point_x_input = QLineEdit(str(shape.end_point.x()))
            self.end_point_y_input = QLineEdit(str(shape.end_point.y()))
            end_point_layout = QVBoxLayout()
            end_point_layout.addWidget(self.end_point_x_input)
            end_point_layout.addWidget(self.end_point_y_input)
            layout.addWidget(end_point_label)
            layout.addLayout(end_point_layout)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_changes)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def save_changes(self):
        if isinstance(self.shape, Line):
            start_point = QPointF(float(self.start_point_x_input.text()), float(self.start_point_y_input.text()))
            end_point = QPointF(float(self.end_point_x_input.text()), float(self.end_point_y_input.text()))
            self.shape.start_point = start_point
            self.shape.end_point = end_point
        elif isinstance(self.shape, Rectangle):
            start_point = QPointF(float(self.start_point_x_input.text()), float(self.start_point_y_input.text()))
            end_point = QPointF(float(self.end_point_x_input.text()), float(self.end_point_y_input.text()))
            self.shape.start_point = start_point
            self.shape.end_point = end_point

        self.accept()