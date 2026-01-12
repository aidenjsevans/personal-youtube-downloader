from PySide6.QtWidgets import QLabel

from PySide6.QtGui import QPixmap

class YoutubeThumbnailLabel(QLabel):

    def __init__(
            self,
            youtube_thumbnail_pixmap: QPixmap,
            parent = None):
        
        super().__init__(parent = parent)

        self.setPixmap(youtube_thumbnail_pixmap)