from PyQt6.QtWidgets import QGridLayout, QWidget, QTextEdit, QMainWindow, QPushButton \
    , QFileDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Variables
        self.file_path = ""

        # Layout and Window
        layout = QGridLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.setWindowTitle("Python Code Editor")

        # Buttons
        open_file_button = QPushButton("Open")
        layout.addWidget(open_file_button, 0, 0)
        open_file_button.pressed.connect(self.open_file)

        save_file_button = QPushButton("Save")
        layout.addWidget(save_file_button, 0, 1)
        save_file_button.pressed.connect(self.save_file)

        # Text Edit
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("Code goes here")
        layout.addWidget(self.text_edit, 1, 0, 1 , 2)

        self.showMaximized()

    def open_file(self):
        file_dialog = QFileDialog()
        file_dialog.exec()
        self.file_path = file_dialog.selectedFiles()[0]

        with open(self.file_path, "r") as py_file:
            content = py_file.read()
            self.text_edit.setText(content)

    def save_file(self):
        content = self.text_edit.toPlainText()
        with open(self.file_path, "w") as file:
            file.write(content)


