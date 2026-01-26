from PySide6.QtGui import QPixmap

class YouTubeIconPixmap(QPixmap):

    def __init__(self):

        super().__init__("icons/youtube.svg")

