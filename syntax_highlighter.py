from PyQt6.QtCore import Qt
from PyQt6.QtGui import QSyntaxHighlighter
import re


class MySyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mapping = {"class": Qt.GlobalColor.blue}

    def highlightBlock(self, text):
        for pattern, frmt in self.mapping.items():
            for match in re.finditer(pattern, text):
                start, end = match.span()
                self.setFormat(start, end - start, frmt)

# highlighter = MySyntaxHighlighter()
# highlighter.setDocument(text_input.document())
