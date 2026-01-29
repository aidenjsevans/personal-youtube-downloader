from PySide6.QtWidgets import (
    QWidget, QGridLayout, QLineEdit,
    QLabel, QPushButton, QCheckBox)

from PySide6.QtCore import (
    Signal, Qt)

from mixins.method_log_mixin import MethodLogMixin

from pytubefix import YouTube, Playlist
from pytubefix.exceptions import RegexMatchError, VideoUnavailable

from widgets.custom.circle_loading_widget import CircleLoadingWidget

import time

class YouTubeUrlSearchView(QWidget, MethodLogMixin):

    valid_youtube_url_signal = Signal(YouTube)
    valid_youtube_playlist_url_signal = Signal(Playlist)
    started_searching_signal = Signal()
    failed_search_signal = Signal()

    def __init__(
            self,
            youtube_icon_label: QLabel,
            youtube_url_line_edit_label: QLabel,
            youtube_url_line_edit: QLineEdit,
            search_youtube_media_push_button: QPushButton,
            playlist_url_check_box: QCheckBox,
            log_calls: bool = False,
            parent = None):
        
        super().__init__(parent = parent)

        self.log_calls = log_calls

        #-----YouTube icon label-----
        self.youtube_icon_label = youtube_icon_label
        self.youtube_icon_label.setParent(self)
        #----------------------------
        
        #-----YouTube URL line edit label-----
        self.youtube_url_line_edit_label = youtube_url_line_edit_label
        self.youtube_url_line_edit_label.setParent(self)
        #-------------------------------------

        #-----YouTube URL line edit-----
        self.youtube_url_line_edit = youtube_url_line_edit
        self.youtube_url_line_edit.setParent(self)
        self.youtube_url_line_edit.textEdited.connect(self.on_edit_youtube_url_line_edit)
        self.youtube_url_line_edit_error_text: str | None = None
        self.youtube_url_line_edit_started_typing: bool = False
        #-------------------------------

        #-----Search YouTube media push button-----
        self.search_youtube_media_push_button = search_youtube_media_push_button
        self.search_youtube_media_push_button.setParent(self)
        self.search_youtube_media_push_button.clicked.connect(self.on_click_search_youtube_media_push_button)
        #------------------------------------------

        #-----YouTube URL check box-----
        self.playlist_url_check_box = playlist_url_check_box
        self.playlist_url_check_box.setParent(self)
        #-------------------------------

        #-----Layout------
        self.view_layout = QGridLayout()

        self.view_layout.addWidget(self.youtube_icon_label, 0, 1, 1, 1)
        self.view_layout.addWidget(self.youtube_url_line_edit_label, 2, 0, 1, 1)
        self.view_layout.addWidget(self.youtube_url_line_edit, 2, 1, 1, 1)
        self.view_layout.addWidget(self.playlist_url_check_box, 2, 2, 1, 1)
        self.view_layout.addWidget(self.search_youtube_media_push_button, 3, 1, 1, 2)

        self.setLayout(self.view_layout)
        #-----------------

    def on_edit_youtube_url_line_edit(self):

        if self.youtube_url_line_edit_started_typing:
            self.youtube_url_line_edit.disconnect(self.on_edit_youtube_url_line_edit)
        
        self.youtube_url_line_edit.reset()
        self.youtube_url_line_edit_error_text = None

        if self.log_calls:
            self.log_call(message = "Success")
    
    def on_click_search_youtube_media_push_button(self):

        try:

            #self.start_searching()

            self.youtube_url = self.youtube_url_line_edit.text()

            if not self.youtube_url:
                self.youtube_url_line_edit_error_text = "ERROR: YouTube URL required"
            
            if self.youtube_url_line_edit_error_text:
                return
            
            #   TODO user option to skip exception
            if self.playlist_url_check_box.isChecked():
                
                playlist = Playlist(url = self.youtube_url)

                for youtube in playlist.videos:
                    
                    youtube.check_availability()
                
                self.emit_valid_youtube_playlist_url_signal(playlist)
                
            else:

                youtube = YouTube(url = self.youtube_url)
                
                youtube.check_availability()

                self.emit_valid_youtube_url_signal(youtube)

        except RegexMatchError:

            self.youtube_url_line_edit_error_text = "ERROR: Invalid YouTube URL"
            #self.fail_searching()

        except VideoUnavailable:
            
            self.youtube_url_line_edit_error_text = "ERROR: Video unavailable"
            #self.fail_searching()

        finally:
            
            if self.youtube_url_line_edit_error_text:

                #self.fail_searching()
                self.youtube_url_line_edit.clear()
                self.youtube_url_line_edit.setPlaceholderText(self.youtube_url_line_edit_error_text)
                self.youtube_url_line_edit.setStyleSheet(self.youtube_url_line_edit.error_style_sheet)
                self.youtube_url_line_edit.textEdited.connect(self.on_edit_youtube_url_line_edit)
                
                if self.log_calls:
                    self.log_call(message = self.youtube_url_line_edit_error_text)
            
    def emit_valid_youtube_url_signal(self, youtube: YouTube):
        
        self.valid_youtube_url_signal.emit(youtube)

        if self.log_calls:
            self.log_call(message = "Success")
    
    def emit_valid_youtube_playlist_url_signal(self, playlist: Playlist):

        self.valid_youtube_playlist_url_signal.emit(playlist)

        if self.log_calls:
            self.log_call(message = "Success")

    def start_searching(self):
        self.started_searching_signal.emit()

    def fail_searching(self):
        self.failed_search_signal.emit()




    

            
            

    
                
        



    
