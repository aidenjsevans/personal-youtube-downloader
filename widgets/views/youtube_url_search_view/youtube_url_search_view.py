from PySide6.QtWidgets import (
    QWidget, QGridLayout, QLineEdit,
    QLabel, QPushButton, QCheckBox)

from PySide6.QtCore import (
    Signal, QThread)

from mixins.method_log_mixin import MethodLogMixin

from pytubefix import YouTube, Playlist

from widgets.views.youtube_url_search_view.youtube_url_search_view_worker import YouTubeUrlSearchViewWorker

class YouTubeUrlSearchView(QWidget, MethodLogMixin):

    valid_youtube_playlist_signal = Signal(Playlist)
    valid_youtube_stream_signal = Signal(YouTube)
    
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

        #=====YouTube icon label=====
        self.youtube_icon_label = youtube_icon_label
        self.youtube_icon_label.setParent(self)
        #============================
        
        #=====YouTube URL line edit label=====
        self.youtube_url_line_edit_label = youtube_url_line_edit_label
        self.youtube_url_line_edit_label.setParent(self)
        #=====================================

        #=====YouTube URL line edit=====
        self.youtube_url_line_edit = youtube_url_line_edit
        self.youtube_url_line_edit.setParent(self)
        self.youtube_url_line_edit.textEdited.connect(self.on_edit_youtube_url_line_edit)
        self.youtube_url_line_edit_first_edited: bool = False
        #===============================

        #=====Search YouTube media push button=====
        self.search_youtube_media_push_button = search_youtube_media_push_button
        self.search_youtube_media_push_button.setParent(self)
        self.search_youtube_media_push_button.clicked.connect(self.on_click_search_youtube_media_push_button)
        #==========================================

        #=====YouTube URL check box=====
        self.playlist_url_check_box = playlist_url_check_box
        self.playlist_url_check_box.setParent(self)
        #===============================

        #=====Layout======
        self.view_layout = QGridLayout()

        self.view_layout.addWidget(self.youtube_icon_label, 0, 1, 1, 1)
        self.view_layout.addWidget(self.youtube_url_line_edit_label, 2, 0, 1, 1)
        self.view_layout.addWidget(self.youtube_url_line_edit, 2, 1, 1, 1)
        self.view_layout.addWidget(self.playlist_url_check_box, 2, 2, 1, 1)
        self.view_layout.addWidget(self.search_youtube_media_push_button, 3, 1, 1, 2)

        self.setLayout(self.view_layout)
        #=================

    def on_edit_youtube_url_line_edit(self):

        if not self.youtube_url_line_edit_first_edited:

            self.youtube_url_line_edit_first_edited = True
            self.youtube_url_line_edit.reset()
        
        if self.log_calls:
            self.log_call()
    
    def on_click_search_youtube_media_push_button(self):

        youtube_url = self.youtube_url_line_edit.text()
        is_playlist_check_box_checked = self.playlist_url_check_box.isChecked()

        #   Need to create a new worker each time so that it can be safely deleted
        self.youtube_url_search_view_worker = YouTubeUrlSearchViewWorker(
            youtube_url = youtube_url,
            is_playlist_check_box_checked = is_playlist_check_box_checked,
            log_calls = self.log_calls
            )

        self.on_click_search_youtube_media_thread = QThread()
        self.youtube_url_search_view_worker.moveToThread(self.on_click_search_youtube_media_thread)

        #=====Connecting methods to call when the on click search YouTube media thread starts=====
        self.on_click_search_youtube_media_thread.started.connect(
            self.on_started_search_youtube_media_thread
            )
        self.on_click_search_youtube_media_thread.started.connect(
            self.youtube_url_search_view_worker.search_youtube_media
            )
        #=================================================================================

        #=====Handling search YouTube playlist worker signals=====
        self.youtube_url_search_view_worker.search_youtube_playlist_finished_signal.connect(
            self.on_search_youtube_playlist_finished_signal
            )
        self.youtube_url_search_view_worker.search_youtube_stream_finished_signal.connect(
            self.on_search_youtube_stream_finished_signal
            )
        self.youtube_url_search_view_worker.search_youtube_media_error_signal.connect(
            self.on_search_youtube_media_error_signal
            )
        #=========================================================

        #=====Stopping thread=====
        self.youtube_url_search_view_worker.search_youtube_playlist_finished_signal.connect(
            self.on_click_search_youtube_media_thread.quit
            )
        self.youtube_url_search_view_worker.search_youtube_stream_finished_signal.connect(
            self.on_click_search_youtube_media_thread.quit
            )
        self.youtube_url_search_view_worker.search_youtube_media_error_signal.connect(
            self.on_click_search_youtube_media_thread.quit
            )
        #=========================

        #=====Thread and worker clean up=====

        #-----Worker-----
        self.youtube_url_search_view_worker.search_youtube_playlist_finished_signal.connect(
            self.youtube_url_search_view_worker.deleteLater
            )
        self.youtube_url_search_view_worker.search_youtube_stream_finished_signal.connect(
            self.youtube_url_search_view_worker.deleteLater
        )
        self.youtube_url_search_view_worker.search_youtube_media_error_signal.connect(
            self.youtube_url_search_view_worker.deleteLater
            )
        #----------------
        
        #-----Thread-----
        self.on_click_search_youtube_media_thread.finished.connect(
            self.on_click_search_youtube_media_thread.deleteLater
            )
        #----------------

        #====================================

        self.on_click_search_youtube_media_thread.start()

        if self.log_calls:
            self.log_call()
    
    def on_started_search_youtube_media_thread(self):
        
        self.search_youtube_media_push_button.setEnabled(False)
        
        self.youtube_url_line_edit.reset()
        self.youtube_url_line_edit.setReadOnly(True)

        if self.log_calls:
            self.log_call()
        
    def on_search_youtube_playlist_finished_signal(self, playlist: Playlist):
        
        self.search_youtube_media_push_button.setEnabled(True)

        self.youtube_url_line_edit.setReadOnly(False)

        self.valid_youtube_playlist_signal.emit(playlist)

        if self.log_calls:
            self.log_call()

    def on_search_youtube_stream_finished_signal(self, youtube: YouTube):
        
        self.search_youtube_media_push_button.setEnabled(True)

        self.youtube_url_line_edit.setReadOnly(False)

        self.valid_youtube_stream_signal.emit(youtube)

        if self.log_calls:
            self.log_call()

    def on_search_youtube_media_error_signal(self, error_text: str):
        
        self.search_youtube_media_push_button.setEnabled(True)

        self.youtube_url_line_edit.setReadOnly(False)
        self.youtube_url_line_edit.clear()
        self.youtube_url_line_edit_first_edited = False
        self.youtube_url_line_edit.set_error_text(error_text = error_text)

        if self.log_calls:
            self.log_call()




    

            
            

    
                
        



    
