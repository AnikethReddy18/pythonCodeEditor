from PyQt6.QtWidgets import QTextEdit
from syntax_highlighter import MySyntaxHighlighter
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QTextCursor


class CodeEditor(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
                        background-color: #1E1E1E;
                        color: #F0F0F0;
                        border: 2px solid #505050;
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
            except:
                pass

        elif event.key() == Qt.Key.Key_ParenLeft:
            self.insertPlainText("()")

        else:
            super().keyPressEvent(event)
