from PySide6.QtGui import QPixmap, QColor

class YoutubeThumbnailPixmap(QPixmap):

    def __init__(self):

        super().__init__(400,225)

        self.fill(QColor("lightgray"))
