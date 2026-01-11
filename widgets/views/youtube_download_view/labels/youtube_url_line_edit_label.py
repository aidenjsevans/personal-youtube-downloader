from PySide6.QtWidgets import QLabel

class YouTubeUrlLineEditLabel(QLabel):

    def __init__(self):
        super().__init__()
        self.setText("YouTube URL")