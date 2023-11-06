from PyQt6.QtWidgets import QGridLayout, QWidget, QTextEdit, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Layout and Window
        layout = QGridLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.showMaximized()
        self.setWindowTitle("Python Code Editor")

        # Widgets
        text_edit = QTextEdit()
        text_edit.setPlaceholderText("Code goes here")
        layout.addWidget(text_edit, 0, 0)


