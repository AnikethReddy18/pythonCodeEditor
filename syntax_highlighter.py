
from PyQt6.QtGui import QSyntaxHighlighter, QColor
import re


class MySyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mapping = {
            r"\b(if|else|elif|while|for|def|class|import|from|as|True|False|None)\b": QColor("#ff7700"),
            r"\".*?\"|\'.*?\'": QColor("#00ff66"),
            r'""".*?"""|\'\'\'.*?\'\'\'': QColor("#00ff66"),
            r"#.*": QColor("#96a89d")
        }

    def highlightBlock(self, text):
        for pattern, frmt in self.mapping.items():
            for match in re.finditer(pattern, text):
                start, end = match.span()
                self.setFormat(start, end - start, frmt)