
from PyQt6.QtWidgets import QGridLayout, QWidget, QTextEdit, QMainWindow, QPushButton \
    , QFileDialog, QInputDialog

import os
from syntax_highlighter import MySyntaxHighlighter



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
        new_file_button = QPushButton("New")
        layout.addWidget(new_file_button, 0, 0)
        new_file_button.pressed.connect(self.new_file)

        open_file_button = QPushButton("Open")
        layout.addWidget(open_file_button, 0, 1)
        open_file_button.pressed.connect(self.open_file)

        save_file_button = QPushButton("Save")
        layout.addWidget(save_file_button, 0, 2)
        save_file_button.pressed.connect(self.save_file)

        run_file_button = QPushButton("Run")
        layout.addWidget(run_file_button, 0, 3)
        run_file_button.pressed.connect(self.run_file)

        # Text Edit
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("Code goes here")
        layout.addWidget(self.text_edit, 1, 0, 1, 4)

        # Syntax Highlighter
        self.highlighter = MySyntaxHighlighter()
        self.highlighter.setDocument(self.text_edit.document())

        # Style
        self.setStyleSheet("color: black")

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

    def run_file(self):
        os.system(f"start cmd /K python {self.file_path}")

    def new_file(self):
        input_dialogue = QInputDialog()
        input_dialogue.setWindowTitle("New File")
        input_dialogue.setLabelText("Enter address of the new file")
        input_dialogue.exec()
        path = input_dialogue.textValue()

        with open(path, "w") as file:
            file.write("")
            self.file_path = path


