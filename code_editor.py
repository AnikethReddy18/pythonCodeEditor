from PyQt6.QtWidgets import QTextEdit
from syntax_highlighter import MySyntaxHighlighter
from PyQt6.QtCore import Qt


class CodeEditor(QTextEdit):
    def __init__(self):
        super().__init__()

        # Style
        self.setStyleSheet("""
                        background-color: #1E1E1E;
                        color: #F0F0F0;
                        border: 2px solid #505050;
                        font-family: Roboto;
                        font-size: 20px;
                    }""")

        # Syntax Highlighter
        self.highlighter = MySyntaxHighlighter()
        self.highlighter.setDocument(self.document())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Return:
            cursor = self.textCursor()
            line_text = cursor.block().text().strip()
            self.insertPlainText("\n")
            try:
                if line_text[-1] == ":":
                    self.insertPlainText("     ")
            except IndexError:
                pass

        elif event.key() == Qt.Key.Key_ParenLeft:
            self.insertPlainText("()")
            self.move_cursor_left()

        elif event.key() == Qt.Key.Key_QuoteDbl:
            self.insertPlainText("\"\"")
            self.move_cursor_left()

        elif event.key() == Qt.Key.Key_Apostrophe:
            self.insertPlainText("\'\'")
            self.move_cursor_left()

        else:
            super().keyPressEvent(event)

    def move_cursor_left(self):
        self.moveCursor(self.textCursor().MoveOperation.Left)
