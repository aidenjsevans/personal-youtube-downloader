from PySide6.QtWidgets import (
    QMainWindow, QStackedWidget, QWidget,
    QGridLayout, QToolBar)

from mixins.method_log_mixin import MethodLogMixin

class MainWindow(QMainWindow, MethodLogMixin):

    def __init__(
            self,
            x_position_px: int,
            y_position_px: int,
            youtube_url_search_view: QWidget,
            youtube_download_view: QWidget,
            youtube_playlist_download_view: QWidget,
            loading_view: QWidget,
            tool_bar: QToolBar,
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

        #=====Tool Bar=====
        self.tool_bar = tool_bar
        self.addToolBar(tool_bar)
        self.tool_bar.setParent(self)
        self.tool_bar.actions()[0].return_to_previous_view_action_signal.connect(self.change_to_previous_view_and_remove_from_route_stack)
        self.tool_bar.actions()[0].setEnabled(False)
        #==================

        #=====YouTube URL search view=====
        self.youtube_url_search_view = youtube_url_search_view
        self.youtube_url_search_view.setParent(self)
        #=================================

        #=====YouTube download view=====
        self.youtube_download_view = youtube_download_view
        self.youtube_download_view.setParent(self)
        self.youtube_download_view.initialised_youtube_stream_thumbnail_signal.connect(self.on_initialised_youtube_stream_thumbnail_signal)
        self.youtube_url_search_view.valid_youtube_stream_signal.connect(self.youtube_download_view.on_valid_youtube_stream_signal)
        #===============================

        #=====YouTube playlist download view=====
        self.youtube_playlist_download_view = youtube_playlist_download_view
        self.youtube_playlist_download_view.setParent(self)
        #========================================

        #=====Loading view=====
        self.loading_view = loading_view
        #======================

        #=====View stack=====
        self.view_stack = QStackedWidget()

        self.view_stack.addWidget(self.youtube_url_search_view)
        self.view_stack.addWidget(self.youtube_download_view)
        self.view_stack.addWidget(self.youtube_playlist_download_view)
        self.view_stack.addWidget(self.loading_view)

        self.view_stack.setCurrentWidget(self.youtube_url_search_view)
        #====================

        #=====Route Stack=====
        self.route_stack = []
        #=====================

        #=====Layout=====
        container = QWidget()
        layout = QGridLayout()

        layout.addWidget(self.view_stack, 0, 0)

        container.setLayout(layout)
        self.setCentralWidget(container)
        #================
    
    def on_initialised_youtube_stream_thumbnail_signal(self):

        self.change_view_and_add_current_view_to_route_stack(self.youtube_download_view)

        if self.log_calls:
            self.log_call()
        
    def on_finished_set_youtube_playlist_thumbnail_signal(self):

        self.change_view_and_add_current_view_to_route_stack(self.youtube_playlist_download_view)

        if self.log_calls:
            self.log_call()
    
    def on_finished_download_signal(self):

        self.view_stack.setCurrentWidget(self.youtube_url_search_view)
        self.clear_route_stack()

        if self.log_calls:
            self.log_call()
        
    def on_started_searching_signal(self):
        
        self.change_view_and_add_current_view_to_route_stack(self.loading_view)

        if self.log_calls:
            self.log_call()

    def on_failed_search_signal(self):
        
        self.change_to_previous_view_and_remove_from_route_stack()

        if self.log_calls:
            self.log_call()
    
    def change_view_and_add_current_view_to_route_stack(self, view: QWidget):

        self.route_stack.append(self.view_stack.currentWidget())
        self.tool_bar.actions()[0].setEnabled(True)

        self.view_stack.setCurrentWidget(view)

        if self.log_calls:
            self.log_call()
    
    def change_view_and_do_not_add_current_view_to_route_stack(self, view: QWidget):
        
        self.view_stack.setCurrentWidget(view)

        if self.log_calls:
            self.log_call()
    
    def change_to_previous_view_and_remove_from_route_stack(self):

        if len(self.route_stack) == 0:
            return
        
        previous_view: QWidget = self.route_stack[-1]
        self.view_stack.setCurrentWidget(previous_view)
        self.route_stack.pop()

        if len(self.route_stack) == 0:
            self.tool_bar.actions()[0].setEnabled(False)
        
        if self.log_calls:
            self.log_call()
    
    def clear_route_stack(self):

        self.route_stack.clear()
        self.tool_bar.actions()[0].setEnabled(False)

        if self.log_calls:
            self.log_call()

    def pop_current_route_from_route_stack(self):

        if len(self.route_stack) == 0:
            return
        else:
            self.route_stack.pop()
        
        if self.log_calls:
            self.log_call()
    
