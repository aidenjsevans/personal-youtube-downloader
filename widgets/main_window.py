from PySide6.QtWidgets import (
    QMainWindow, QStackedWidget, QWidget,
    QGridLayout)

from PySide6.QtCore import Signal

from pytubefix import YouTube

class MainWindow(QMainWindow):

    valid_youtube_url_ready = Signal(YouTube)

    def __init__(
            self,
            x_position_px: int,
            y_position_px: int,
            youtube_url_search_view: QWidget,
            youtube_download_view: QWidget,
            width_px: int | None = None,
            height_px: int | None = None):
        
        super().__init__()

        if not width_px or not height_px:
            self.move(x_position_px, y_position_px)
        else:
            self.setGeometry(x_position_px, y_position_px, width_px, height_px)
            
        self.setWindowTitle("YouTubeDownloader")

        self.youtube_url_search_view = youtube_url_search_view
        self.youtube_url_search_view.setParent(self)
        self.youtube_url_search_view.valid_youtube_url_ready.connect(self.handle_valid_youtube_url_ready)

        self.youtube_download_view = youtube_download_view
        self.youtube_download_view.setParent(self)

        self.view_stack = QStackedWidget()

        self.view_stack.addWidget(self.youtube_url_search_view)
        self.view_stack.addWidget(self.youtube_download_view)

        #   TODO remove once coding YouTube download view
        self.view_stack.setCurrentWidget(self.youtube_download_view)

        container = QWidget()
        layout = QGridLayout()

        layout.addWidget(self.view_stack, 0, 0)

        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def handle_valid_youtube_url_ready(self, yt: YouTube):
        self.valid_youtube_url_ready.emit(yt)
        self.view_stack.setCurrentWidget(self.youtube_download_view)



    
