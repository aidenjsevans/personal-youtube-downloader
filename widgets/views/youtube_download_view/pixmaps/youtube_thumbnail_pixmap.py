from PySide6.QtGui import QPixmap, QColor

class YoutubeThumbnailPixmap(QPixmap):

    def __init__(self):

        self.width_px: int = 400
        self.height_px: int = 225

        super().__init__(self.width_px, self.height_px)

        self.fill(QColor("lightgray"))
