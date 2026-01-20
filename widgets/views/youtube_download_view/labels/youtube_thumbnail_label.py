from PySide6.QtWidgets import QLabel

from PySide6.QtGui import QPixmap

from PySide6.QtCore import Qt, Signal

from mixins.method_log_mixin import MethodLogMixin

import requests

class YoutubeThumbnailLabel(QLabel, MethodLogMixin):

    finished_set_thumbnail_signal = Signal()

    def __init__(
            self,
            youtube_thumbnail_pixmap: QPixmap,
            log_calls: bool = False,
            parent = None):
        
        super().__init__(parent = parent)

        self.log_calls = log_calls

        self.youtube_thumbnail_pixmap = youtube_thumbnail_pixmap

        self.setPixmap(youtube_thumbnail_pixmap)
        self.adjustSize()
        self.setAlignment(Qt.AlignCenter)
    
    def set_thumbnail(self, thumbnail_url: str):

        response = requests.get(thumbnail_url)

        if response.status_code == 200:

            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            
            scaled_pixmap: QPixmap = pixmap.scaled(
                self.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
                )
            
            self.setPixmap(scaled_pixmap)
            self.youtube_thumbnail_pixmap = scaled_pixmap
        
            if self.log_calls:
                self.log_call(message = "Success")

            self.emit_finished_set_thumbnail_signal()

            return

        self.log_call(message = str(response.status_code))

        self.emit_finished_set_thumbnail_signal()
    
    def emit_finished_set_thumbnail_signal(self):

        self.finished_set_thumbnail_signal.emit()

        if self.log_calls:
            self.log_call(message = "Success")
        
