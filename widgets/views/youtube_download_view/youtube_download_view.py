from PySide6.QtWidgets import (
    QWidget, QLabel, QGridLayout,
    QLineEdit, QPushButton, QComboBox)

from PySide6.QtCore import Qt, Signal, QThread

from PySide6.QtGui import QPixmap

from pytubefix import YouTube, StreamQuery

from mixins.method_log_mixin import MethodLogMixin

from enums.stream_type import StreamType
from enums.image_format import ImageFormat

from helpers.format_helper import FormatHelper
from helpers.youtube_helper import YouTubeHelper

from mutagen.mp4 import MP4Cover

from widgets.views.youtube_download_view.youtube_download_view_worker import YouTubeDownloadViewWorker

class YoutubeDownloadView(QWidget, MethodLogMixin):

    finished_youtube_download_signal = Signal()

    initialised_youtube_stream_combo_boxes_signal = Signal()

    initialised_youtube_stream_thumbnail_signal = Signal()

    def __init__(
            self,
            youtube_thumbnail_label: QLabel,
            download_folder_line_edit_label: QLabel,
            download_folder_line_edit: QLineEdit,
            select_download_folder_push_button: QPushButton,
            stream_type_options_combo_box_label: QLabel,
            stream_type_options_combo_box: QComboBox,
            stream_quality_options_combo_box_label: QLabel,
            stream_quality_options_combo_box: QComboBox,
            download_youtube_stream_push_button: QPushButton,
            stream_file_extension_options_combo_box_label: QLabel,
            stream_file_extension_options_combo_box: QComboBox,
            thumbnail_metadata_format: ImageFormat,
            log_calls: bool = False,
            parent = None):
        
        super().__init__(parent = parent)

        self.thumbnail_metadata_format = thumbnail_metadata_format
        self.log_calls = log_calls
        self.youtube: YouTube | None = None

        #=====YouTube thumbnail label=====
        self.youtube_thumbnail_label = youtube_thumbnail_label
        self.youtube_thumbnail_label.setParent(self)
        #=================================

        #=====Download folder line edit label=====
        self.download_folder_line_edit_label = download_folder_line_edit_label
        self.download_folder_line_edit_label.setParent(self)
        #=========================================
        
        #======Download folder line edit=====
        self.download_folder_line_edit = download_folder_line_edit
        self.download_folder_line_edit.setParent(self)
        self.download_folder_line_edit_error_text: str | None = None
        #====================================

        #======Select download folder push button======
        self.select_download_folder_push_button = select_download_folder_push_button
        self.select_download_folder_push_button.setParent(self)
        select_download_folder_push_button.clicked.connect(self.on_click_select_download_folder_push_button)
        #==============================================

        #=====Stream type options combo box label===== 
        self.stream_type_options_combo_box_label = stream_type_options_combo_box_label
        self.stream_type_options_combo_box_label.setParent(self)
        #=======================================

        #=====Stream type options combo box======
        self.stream_type_options_combo_box = stream_type_options_combo_box
        self.stream_type_options_combo_box.setParent(self)
        self.stream_type_options_combo_box.activated.connect(self.on_activate_stream_type_options_combo_box)
        #========================================

        #=====Stream quality options combo box label=====
        self.stream_quality_options_combo_box_label = stream_quality_options_combo_box_label
        self.stream_quality_options_combo_box_label.setParent(self)
        #================================================

        #=====Stream quality options combo box=====
        self.stream_quality_options_combo_box = stream_quality_options_combo_box
        self.stream_quality_options_combo_box.setParent(self)
        self.stream_quality_options_combo_box.activated.connect(self.on_activate_stream_quality_options_combo_box)
        #==========================================

        #=====Download YouTube stream push button=====
        self.download_youtube_stream_push_button = download_youtube_stream_push_button
        self.download_youtube_stream_push_button.setParent(self)
        self.download_youtube_stream_push_button.clicked.connect(self.on_click_download_youtube_stream_push_button)
        #=============================================

        #=====Stream file extension options combo box label=====
        self.stream_file_extension_options_combo_box_label = stream_file_extension_options_combo_box_label
        self.stream_file_extension_options_combo_box_label.setParent(self)
        #=======================================================

        #=====Stream file extension options combo box=====
        self.stream_file_extension_options_combo_box = stream_file_extension_options_combo_box
        self.stream_file_extension_options_combo_box.setParent(self)
        #=======================================================

        #=====Layout=====
        layout = QGridLayout()

        layout.addWidget(self.youtube_thumbnail_label, 0, 1)
        layout.addWidget(self.download_folder_line_edit_label, 1, 0)
        layout.addWidget(self.download_folder_line_edit, 1, 1)
        layout.addWidget(self.select_download_folder_push_button, 1, 2)
        layout.addWidget(self.stream_type_options_combo_box_label, 2, 0)
        layout.addWidget(self.stream_type_options_combo_box, 2, 1)
        layout.addWidget(self.stream_quality_options_combo_box_label, 3, 0)
        layout.addWidget(self.stream_quality_options_combo_box, 3, 1)
        layout.addWidget(self.stream_file_extension_options_combo_box_label, 4, 0)
        layout.addWidget(self.stream_file_extension_options_combo_box, 4, 1)       
        layout.addWidget(self.download_youtube_stream_push_button, 5, 1)

        self.setLayout(layout)
        #================

        #=====Connecting internal signals=====
        self.initialised_youtube_stream_combo_boxes_signal.connect(self.on_initialised_youtube_stream_combo_boxes_signal)
        #=====================================

    def on_click_select_download_folder_push_button(self):

        self.on_valid_youtube_stream_worker = YouTubeDownloadViewWorker(
            youtube = self.youtube,
            log_calls = self.log_calls
            )
        
        self.on_click_select_download_folder_thread = QThread()
        self.on_valid_youtube_stream_worker.moveToThread(self.on_click_select_download_folder_thread)

        #=====Connecting methods to call when the on click select download folder thread starts=====
        self.on_click_select_download_folder_thread.started.connect(
            self.on_valid_youtube_stream_worker.validate_download_folder_url
            )
        #===========================================================================================

        #=====Handling YouTube download worker signals=====
        self.on_valid_youtube_stream_worker.valid_download_folder_url_signal.connect(
            self.on_valid_download_folder_url_signal
            )
        self.on_valid_youtube_stream_worker.invalid_download_folder_url_signal.connect(
            self.on_invalid_download_folder_url_signal
            )
        #==================================================

        #=====Stopping thread=====
        self.on_valid_youtube_stream_worker.valid_download_folder_url_signal.connect(
            self.on_click_select_download_folder_thread.quit
            )
        self.on_valid_youtube_stream_worker.invalid_download_folder_url_signal.connect(
            self.on_click_select_download_folder_thread.quit
            )
        #=========================

        #=====Thread and worker clean up=====
        
        #-----Worker-----
        self.on_valid_youtube_stream_worker.valid_download_folder_url_signal.connect(
            self.on_valid_youtube_stream_worker.deleteLater
            )
        self.on_valid_youtube_stream_worker.invalid_download_folder_url_signal.connect(
            self.on_valid_youtube_stream_worker.deleteLater
            )
        #----------------

        #-----Thread-----
        self.on_click_select_download_folder_thread.finished.connect(
            self.on_click_select_download_folder_thread.deleteLater
            )
        #----------------

        #====================================

        self.on_click_select_download_folder_thread.start()

        if self.log_calls:
            self.log_call()

    def on_valid_download_folder_url_signal(self, download_folder_url: str):
        
        self.download_folder_line_edit.clear()
        self.download_folder_line_edit.reset()
        self.download_folder_line_edit.setText(download_folder_url)

        if self.log_calls:
            self.log_call()

    def on_invalid_download_folder_url_signal(self, error_text: str):

        self.download_folder_line_edit.clear()
        self.download_folder_line_edit.set_error_text(error_text)

        if self.log_calls:
            self.log_call()

    def on_retrieved_initial_youtube_stream_combo_boxes_values_signal(
            self,
            stream_type_options: list[StreamType],
            stream_quality_options: list[str],
            stream_file_extension_options: list[str]):
        
        for stream_type in stream_type_options:

            self.stream_type_options_combo_box.addItem(
                stream_type.value,
                userData = stream_type
                )
            
            self.stream_quality_options_combo_box.addItems(stream_quality_options)

            self.stream_file_extension_options_combo_box.addItems(stream_file_extension_options)

        self.initialised_youtube_stream_combo_boxes_signal.emit()

        if self.log_calls:
            self.log_call()
    
    def on_initialised_youtube_stream_combo_boxes_signal(self):
        
        self.on_initialised_combo_boxes_worker = YouTubeDownloadViewWorker(
            youtube = self.youtube,
            thumbnail_size = self.youtube_thumbnail_label.size(),
            log_calls = self.log_calls  
            )
        
        self.on_initialised_combo_boxes_thread = QThread()
        self.on_initialised_combo_boxes_worker.moveToThread(self.on_initialised_combo_boxes_thread)

        #=====Connecting methods to call when the initialised combo boxes signal is received=====
        self.on_initialised_combo_boxes_thread.started.connect(
            self.on_initialised_combo_boxes_worker.create_youtube_thumbnail_pixmap
            )
        #========================================================================================

        #=====Handling YouTube download worker signals=====
        self.on_initialised_combo_boxes_worker.created_youtube_thumbnail_pixmap_signal.connect(
            self.on_created_youtube_thumbnail_pixmap_signal
            )
        #==================================================

        #=====Stopping thread=====
        self.on_initialised_combo_boxes_worker.created_youtube_thumbnail_pixmap_signal.connect(
            self.on_initialised_combo_boxes_thread.quit
            )
        #=========================

        #=====Thread and worker clean up=====

        #-----Worker-----
        self.on_initialised_combo_boxes_worker.created_youtube_thumbnail_pixmap_signal.connect(
            self.on_initialised_combo_boxes_worker.deleteLater
            )
        #----------------

        #-----Thread-----
        self.on_initialised_combo_boxes_worker.created_youtube_thumbnail_pixmap_signal.connect(
            self.on_initialised_combo_boxes_thread.deleteLater
            )
        #----------------

        #====================================

        self.on_initialised_combo_boxes_thread.start()

        if self.log_calls:
            self.log_call()

    def on_created_youtube_thumbnail_pixmap_signal(self, thumbnail_pixmap: QPixmap):

        self.youtube_thumbnail_label.setPixmap(thumbnail_pixmap)

        self.initialised_youtube_stream_thumbnail_signal.emit()

        if self.log_calls:
            self.log_call()

    def on_valid_youtube_stream_signal(self, youtube: YouTube):

        self.youtube = youtube

        self.on_valid_youtube_stream_worker = YouTubeDownloadViewWorker(
            youtube = self.youtube,
            log_calls = self.log_calls
            )
        
        self.on_valid_youtube_stream_thread = QThread()
        self.on_valid_youtube_stream_worker.moveToThread(self.on_valid_youtube_stream_thread)

        #=====Handling YouTube download view worker signals=====
        self.on_valid_youtube_stream_worker.retrieved_initial_youtube_stream_combo_boxes_values_signal.connect(
            self.on_retrieved_initial_youtube_stream_combo_boxes_values_signal
            )
        #=======================================================

        #=====Connecting methods to call when the valid YouTube stream signal is received=====
        self.on_valid_youtube_stream_thread.started.connect(
            self.on_valid_youtube_stream_worker.retrieve_initial_youtube_stream_combo_boxes_values
            )
        #=====================================================================================

        #=====Stopping thread=====
        self.on_valid_youtube_stream_worker.retrieved_initial_youtube_stream_combo_boxes_values_signal.connect(
            self.on_valid_youtube_stream_thread.quit
            )
        #=========================

        #=====Thread and worker clean up=====

        #-----Worker-----
        self.on_valid_youtube_stream_worker.retrieved_initial_youtube_stream_combo_boxes_values_signal.connect(
            self.on_valid_youtube_stream_worker.deleteLater
            )
        #----------------

        #-----Thread-----
        self.on_valid_youtube_stream_worker.retrieved_initial_youtube_stream_combo_boxes_values_signal.connect(
            self.on_valid_youtube_stream_thread.deleteLater
            )
        #----------------

        #=====================================

        self.on_valid_youtube_stream_thread.start()

        if self.log_calls:
            self.log_call()

    def on_activate_stream_type_options_combo_box(self):
        
        current_stream_type: StreamType = self.stream_type_options_combo_box.currentData(Qt.UserRole)
        
        self.stream_quality_options_combo_box.set_combo_box_items_based_on_streams(
            streams = self.youtube.streams,
            stream_type = current_stream_type
            )
        
        current_stream_quality: str = self.stream_quality_options_combo_box.currentText()
        
        self.stream_file_extension_options_combo_box.set_combo_box_items_based_on_streams(
            streams = self.youtube.streams,
            stream_type = current_stream_type,
            stream_quality = current_stream_quality
            )
    
    def on_activate_stream_quality_options_combo_box(self):
        
        current_stream_type: StreamType = self.stream_type_options_combo_box.currentData(Qt.UserRole)

        current_stream_quality: str = self.stream_quality_options_combo_box.currentText()
        
        self.stream_file_extension_options_combo_box.set_combo_box_items_based_on_streams(
            streams = self.youtube.streams,
            stream_type = current_stream_type,
            stream_quality = current_stream_quality
            )
    
    def on_click_download_youtube_stream_push_button(self):

        current_stream_type: StreamType = self.stream_type_options_combo_box.currentData(Qt.UserRole)
        current_stream_quality: str = self.stream_quality_options_combo_box.currentText()
        current_download_folder_url: str = self.download_folder_line_edit.text()
        current_file_extension: str = self.stream_file_extension_options_combo_box.currentText()

        #   TODO handle empty download folder URL and URL that does not exist
        if not current_download_folder_url:
            return

        filtered_streams: StreamQuery | None = None

        if current_stream_type == StreamType.AUDIO_AND_VIDEO:

            filtered_streams = self.youtube.streams.filter(
                res = current_stream_quality,
                progressive = True,
                mime_type = f"video/{current_file_extension}",
                type = "video"
                )
            
        elif current_stream_type == StreamType.VIDEO_ONLY:

            filtered_streams = self.youtube.streams.filter(
                res = current_stream_quality,
                progressive = False,
                mime_type = f"video/{current_file_extension}",
                type = "video"
                )
            
        elif current_stream_type == StreamType.AUDIO_ONLY:

            filtered_streams = self.youtube.streams.filter(
                abr = current_stream_quality,
                progressive = False,
                mime_type = f"audio/{current_file_extension}",
                type = "audio"
                )
            
        if filtered_streams.first():
            
            stream_filepath: str = filtered_streams.first().download(
                output_path = current_download_folder_url
                )
            
            if current_stream_type == StreamType.AUDIO_AND_VIDEO or current_stream_type == StreamType.VIDEO_ONLY:

                return
            
            elif current_stream_type == StreamType.AUDIO_ONLY and current_file_extension == "mp4":

                mp4_cover: MP4Cover | None = None

                if self.youtube_thumbnail_label.thumbnail_bytes:

                    mp4_cover = FormatHelper.image_bytes_to_mp4_cover(
                        self.youtube_thumbnail_label.thumbnail_bytes,
                        self.thumbnail_metadata_format
                        )
                    
                if mp4_cover:
                    
                    YouTubeHelper.set_mp4_audio_file_metadata(
                        audio_filepath = stream_filepath,
                        title = self.youtube.title,
                        author = self.youtube.author,
                        thumbnail = [mp4_cover]
                        )
                
                else:

                    YouTubeHelper.set_mp4_audio_file_metadata(
                        audio_filepath = stream_filepath,
                        title = self.youtube.title,
                        author = self.youtube.author,
                        )
            
            self.finished_youtube_download_signal.emit()


        
                    
                    