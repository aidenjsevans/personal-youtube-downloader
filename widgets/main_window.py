from PySide6.QtWidgets import (
    QMainWindow, QStackedWidget, QWidget,
    QGridLayout)

from mixins.method_log_mixin import MethodLogMixin

class MainWindow(QMainWindow, MethodLogMixin):

    def __init__(
            self,
            x_position_px: int,
            y_position_px: int,
            youtube_url_search_view: QWidget,
            youtube_download_view: QWidget,
            width_px: int | None = None,
            height_px: int | None = None,
            log_calls: bool = False):
        
        super().__init__()

        self.log_calls = log_calls

        if not width_px or not height_px:
            self.move(x_position_px, y_position_px)
        else:
            self.setGeometry(x_position_px, y_position_px, width_px, height_px)
            
        self.setWindowTitle("YouTubeDownloader")

        #-----YouTube url search view-----
        self.youtube_url_search_view = youtube_url_search_view
        self.youtube_url_search_view.setParent(self)
        #---------------------------------

        #-----YouTube download view-----
        self.youtube_download_view = youtube_download_view
        self.youtube_download_view.setParent(self)

        #   The YouTube download view needs to be aware of the YouTube URL search view to listen for the valid YouTube URL signal
        self.youtube_download_view.connect_handle_valid_youtube_url_signal_methods(self.youtube_url_search_view)

        #   Need to change the main window view when a valid YouTube URL is emitted and the set thumbnail method has completed
        self.youtube_download_view.youtube_thumbnail_label.finished_set_thumbnail_signal.connect(self.handle_finished_set_thumbnail_signal)
        #-------------------------------

        #-----View stack-----
        self.view_stack = QStackedWidget()

        self.view_stack.addWidget(self.youtube_url_search_view)
        self.view_stack.addWidget(self.youtube_download_view)

        self.view_stack.setCurrentWidget(self.youtube_url_search_view)
        #--------------------

        #-----Layout-----
        container = QWidget()
        layout = QGridLayout()

        layout.addWidget(self.view_stack, 0, 0)

        container.setLayout(layout)
        self.setCentralWidget(container)
        #----------------
    
    def handle_finished_set_thumbnail_signal(self):

        self.view_stack.setCurrentWidget(self.youtube_download_view)

        if self.log_calls:
            self.log_call(message = "Success")
    



    
