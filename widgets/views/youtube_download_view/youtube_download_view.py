from PySide6.QtWidgets import (
    QWidget, QLabel, QGridLayout)

class YoutubeDownloadView(QWidget):

    def __init__(
            self,
            youtube_thumbnail_label: QLabel,
            parent = None):
        
        super().__init__(parent = parent)

        self.youtube_thumbnail_label = youtube_thumbnail_label
        self.youtube_thumbnail_label.setParent(self)

        layout = QGridLayout()

        layout.addWidget(self.youtube_thumbnail_label, 0, 0)

        self.setLayout(layout)

