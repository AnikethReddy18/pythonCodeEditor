from PyQt6.QtWidgets import QGridLayout, QWidget, QTextEdit, QMainWindow, QPushButton \
    , QFileDialog, QInputDialog

import os
from code_editor import CodeEditor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Variables
        self.file_path = None

        # Layout and Window
        layout = QGridLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.setWindowTitle("Python Code Editor")

        # Buttons

        save_file_button = QPushButton("Save")
        layout.addWidget(save_file_button, 0, 0, 1, 2)
        save_file_button.pressed.connect(self.save_file)

        run_file_button = QPushButton("Run")
        layout.addWidget(run_file_button, 0, 2, 1, 2)
        run_file_button.pressed.connect(self.run_file)

        # Text Edit
        self.text_edit = CodeEditor()
        self.text_edit.setPlaceholderText("Code goes here")
        layout.addWidget(self.text_edit, 1, 0, 1, 4)

        # Style
        dark_stylesheet = """
                    QMainWindow {
                        background-color: #2E2E2E; 
                        color: #F0F0F0;  
                    }

                    QPushButton {
                        background-color: #2E2E2E;  
                        color: #F0F0F0; 
                        border: 2px solid #505050;
                    }
                    QPushButton:hover {
                         background-color: #404040;
                    }
                    
                """
        self.setStyleSheet(dark_stylesheet)

        self.showMaximized()

    def save_file(self):

        content = self.text_edit.toPlainText()

        if self.file_path is not None:
            with open(self.file_path, "w") as file:
                file.write(content)
        else:
            file_dialog = QFileDialog()
            file_dialog.exec()
            self.file_path = file_dialog.selectedFiles()[0]

            with open(self.file_path, "w") as py_file:
                py_file.write(content)

    def run_file(self):
        os.system(f"start cmd /K python {self.file_path}")
