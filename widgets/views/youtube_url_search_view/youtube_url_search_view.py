from PySide6.QtWidgets import (
    QWidget, QGridLayout, QLineEdit,
    QLabel, QPushButton, QFileDialog,
    QComboBox)

from PySide6.QtCore import (
    QUrl, Signal)

from mixins.push_button_mixin import PushButtonMixin

from pytubefix import YouTube, StreamQuery
from pytubefix.exceptions import RegexMatchError, VideoUnavailable

class YouTubeUrlSearchView(QWidget):

    valid_youtube_url_ready = Signal(YouTube)

    def __init__(
            self,
            youtube_url_line_edit_label: QLabel,
            youtube_url_line_edit: QLineEdit,
            search_youtube_media_push_button: QPushButton | PushButtonMixin,
            parent = None):
        
        super().__init__(parent = parent)
        
        #   YouTube URL line edit label
        self.youtube_url_line_edit_label = youtube_url_line_edit_label
        self.youtube_url_line_edit_label.setParent(self)
        
        #   YouTube URL line edit
        self.youtube_url_line_edit = youtube_url_line_edit
        self.youtube_url_line_edit.setParent(self)
        self.youtube_url_line_edit.textEdited.connect(self.on_edit_youtube_url_line_edit)
        self.youtube_url_line_edit_error_text: str | None = None
        self.youtube_url_line_edit_started_typing: bool = False
        
        #   Download folder line edit label
        #self.download_folder_line_edit_label = download_folder_line_edit_label
        #self.download_folder_line_edit_label.setParent(self)
        
        #   Download folder line edit
        #self.download_folder_line_edit = download_folder_line_edit
        #self.download_folder_line_edit.setParent(self)
        #self.download_folder_line_edit.textEdited.connect(self.on_edit_download_folder_line_edit)
        #self.download_folder_line_edit_error_text: str | None = None
        #self.download_folder_line_edit_started_typing: bool = False

        #   Select download folder push button
        #self.select_download_folder_push_button = select_download_folder_push_button
        #self.select_download_folder_push_button.setParent(self)
        #select_download_folder_push_button.connect_method(self.on_click_select_download_folder_push_button)

        #   Search YouTube media push button
        self.search_youtube_media_push_button = search_youtube_media_push_button
        self.search_youtube_media_push_button.setParent(self)
        self.search_youtube_media_push_button.connect_method(self.on_click_search_youtube_media_push_button)
        
        self.download_folder_url: QUrl | None = None
        self.youtube_url: str | None = None

        self.youtube_media_streams: StreamQuery | None = None

        layout = QGridLayout()

        layout.addWidget(self.youtube_url_line_edit_label, 0, 0)
        layout.addWidget(self.youtube_url_line_edit, 0, 1, 1, 2)
        #layout.addWidget(self.download_folder_line_edit_label, 1, 0)
        #layout.addWidget(self.download_folder_line_edit, 1, 1, 1, 2)
        #layout.addWidget(self.select_download_folder_push_button, 1, 3)
        layout.addWidget(self.search_youtube_media_push_button, 1, 1, 1, 2)
    
        self.setLayout(layout)
    
    #def on_click_select_download_folder_push_button(self):
        
    #    try:
            
    #        self.download_folder_url = QFileDialog.getExistingDirectoryUrl(self, caption = "Select download folder")
            
    #        if self.download_folder_url.isValid():
    #            url_text: str = self.download_folder_url.toLocalFile()
    #            self.download_folder_line_edit.setText(url_text)
    #        else:
    #            self.download_folder_line_edit_error_text: str = "ERROR: Invalid folder URL"
    #            self.download_folder_url = None
            
    #    except KeyboardInterrupt:

    #        self.download_folder_line_edit.clear()
    #        self.download_folder_line_edit.reset()
    #        self.download_folder_line_edit_error_text = None
        
    #    finally:

    #        if self.download_folder_line_edit_error_text:
                
    #            self.download_folder_line_edit.clear()
    #            self.download_folder_line_edit.setPlaceholderText(self.download_folder_line_edit_error_text)
    #            self.download_folder_line_edit.setStyleSheet(self.download_folder_line_edit.error_style_sheet)
    #            self.download_folder_line_edit.textEdited.connect(self.on_edit_download_folder_line_edit)
    
    #def on_edit_download_folder_line_edit(self):
        
    #    if self.download_folder_line_edit_started_typing:
    #        self.download_folder_line_edit.disconnect(self.on_edit_download_folder_line_edit)
        
    #    self.download_folder_line_edit.reset()
    #    self.download_folder_line_edit_error_text = None
    
    def on_edit_youtube_url_line_edit(self):

        if self.youtube_url_line_edit_started_typing:
            self.youtube_url_line_edit.disconnect(self.on_edit_youtube_url_line_edit)
        
        self.youtube_url_line_edit.reset()
        self.youtube_url_line_edit_error_text = None
    
    def on_click_search_youtube_media_push_button(self):

        try:

            self.youtube_url = self.youtube_url_line_edit.text()

            if not self.youtube_url:
                self.youtube_url_line_edit_error_text = "ERROR: YouTube URL required"
            
            if self.youtube_url_line_edit_error_text:
                return
            
            yt = YouTube(url = self.youtube_url)
            yt.check_availability()

            self.valid_youtube_url_ready.emit(yt)
            
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

    
                
        



    
