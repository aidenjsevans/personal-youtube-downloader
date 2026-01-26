from PySide6.QtWidgets import QLabel

from PySide6.QtGui import QPixmap

from PySide6.QtCore import Qt

class YouTubeIconLabel(QLabel):

    def __init__(
        self,
        youtube_icon_pixmap: QPixmap,
        parent = None):

        super().__init__(parent = parent)

        self.youtube_icon_pixmap = youtube_icon_pixmap
        self.setPixmap(self.youtube_icon_pixmap)
        self.adjustSize()
        self.setAlignment(Qt.AlignCenter)

        self.setStyleSheet("""
            background-color: white;
            color: black;
            border-radius: 20px;  /* Rounds the corners */
            border: 2px solid gray;  /* Optional border */
            padding: 10px;
            """
            )