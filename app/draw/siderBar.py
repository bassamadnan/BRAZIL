from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout

class SidebarWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Shape Options")
        self.setFixedWidth(200)

        layout = QVBoxLayout()
        self.setLayout(layout)

        delete_button = QPushButton("Delete")
        edit_button = QPushButton("Edit")
        copy_button = QPushButton("Copy")

        layout.addWidget(delete_button)
        layout.addWidget(edit_button)
        layout.addWidget(copy_button)

        delete_button.clicked.connect(self.delete_shape)
        edit_button.clicked.connect(self.edit_shape)
        copy_button.clicked.connect(self.copy_shape)

    def delete_shape(self):
        print("Delete shape")

    def edit_shape(self):
        print("Edit shape")

    def copy_shape(self):
        print("Copy shape")