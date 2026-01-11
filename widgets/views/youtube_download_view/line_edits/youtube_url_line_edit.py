from PySide6.QtWidgets import QLineEdit

class YouTubeUrlLineEdit(QLineEdit):

    def __init__(self):
        super().__init__()
        self.setPlaceholderText("YouTube URL")