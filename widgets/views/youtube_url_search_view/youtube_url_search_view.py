from PySide6.QtWidgets import (
    QWidget, QGridLayout, QLineEdit,
    QLabel, QPushButton)

from PySide6.QtCore import (
    QUrl, Signal)

from mixins.method_log_mixin import MethodLogMixin

from pytubefix import YouTube, StreamQuery
from pytubefix.exceptions import RegexMatchError, VideoUnavailable

class YouTubeUrlSearchView(QWidget, MethodLogMixin):

    valid_youtube_url_signal = Signal(YouTube)

    def __init__(
            self,
            youtube_url_line_edit_label: QLabel,
            youtube_url_line_edit: QLineEdit,
            search_youtube_media_push_button: QPushButton,
            log_calls: bool = False,
            parent = None):
        
        super().__init__(parent = parent)

        self.log_calls = log_calls
        
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

        #-----Layout------
        layout = QGridLayout()

        layout.addWidget(self.youtube_url_line_edit_label, 0, 0)
        layout.addWidget(self.youtube_url_line_edit, 0, 1, 1, 2)
        layout.addWidget(self.search_youtube_media_push_button, 1, 1, 1, 2)
    
        self.setLayout(layout)
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

            self.youtube_url = self.youtube_url_line_edit.text()

            if not self.youtube_url:
                self.youtube_url_line_edit_error_text = "ERROR: YouTube URL required"
            
            if self.youtube_url_line_edit_error_text:
                return
            
            yt = YouTube(url = self.youtube_url)
            yt.check_availability()

            self.emit_valid_youtube_url_signal(yt)

        except RegexMatchError:

            self.youtube_url_line_edit_error_text = "ERROR: Invalid YouTube URL"

        except VideoUnavailable:
            
            self.youtube_url_line_edit_error_text = "ERROR: Video unavailable"

        finally:
            
            if self.youtube_url_line_edit_error_text:

                self.youtube_url_line_edit.clear()
                self.youtube_url_line_edit.setPlaceholderText(self.youtube_url_line_edit_error_text)
                self.youtube_url_line_edit.setStyleSheet(self.youtube_url_line_edit.error_style_sheet)
                self.youtube_url_line_edit.textEdited.connect(self.on_edit_youtube_url_line_edit)
                
                if self.log_calls:
                    self.log_call(message = self.youtube_url_line_edit_error_text)

    def emit_valid_youtube_url_signal(self, yt: YouTube):
        
        self.valid_youtube_url_signal.emit(yt)

        if self.log_calls:
            self.log_call(message = "Success")
    

            
            

    
                
        



    
