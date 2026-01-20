from PySide6.QtWidgets import QLabel

from PySide6.QtGui import QPixmap

from PySide6.QtCore import Qt, Signal

from mixins.method_log_mixin import MethodLogMixin

import requests

from helpers.request_helper import RequestHelper

class YoutubeThumbnailLabel(QLabel, MethodLogMixin):

    finished_set_thumbnail_signal = Signal()

    def __init__(
            self,
            youtube_thumbnail_pixmap: QPixmap,
            log_calls: bool = False,
            parent = None):
        
        super().__init__(parent = parent)

        self.log_calls = log_calls
        self.thumbnail_bytes: bytes | None = None

        self.youtube_thumbnail_pixmap = youtube_thumbnail_pixmap

        self.setPixmap(youtube_thumbnail_pixmap)
        self.adjustSize()
        self.setAlignment(Qt.AlignCenter)
    
    def set_thumbnail(self, thumbnail_url: str):

        try:

            response = RequestHelper.get(thumbnail_url)

            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            
            scaled_pixmap: QPixmap = pixmap.scaled(
                self.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
                )
            
            self.setPixmap(scaled_pixmap)
            self.youtube_thumbnail_pixmap = scaled_pixmap

            self.emit_finished_set_thumbnail_signal()

            self.thumbnail_bytes = response.content

            if self.log_calls:
                self.log_call(message = "Success")

        except requests.HTTPError as error:
            
            status_code: int = error.response.status_code
            self.log_call(message = f"HTTPError: {status_code}")

    def emit_finished_set_thumbnail_signal(self):

        self.finished_set_thumbnail_signal.emit()

        if self.log_calls:
            self.log_call(message = "Success")
        
