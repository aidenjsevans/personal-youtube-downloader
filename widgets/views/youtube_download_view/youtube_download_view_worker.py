from pytubefix import YouTube, StreamQuery

from enums.stream_type import StreamType

from PySide6.QtWidgets import (
    QFileDialog)

from PySide6.QtCore import (
    Qt, Signal, QObject,
    QSize)

from PySide6.QtGui import (
    QPixmap)

from mixins.method_log_mixin import MethodLogMixin

from mutagen.mp4 import MP4Cover

from helpers.format_helper import FormatHelper
from helpers.youtube_helper import YouTubeHelper

class YouTubeDownloadViewWorker(QObject, MethodLogMixin):

    finished_youtube_stream_download_signal = Signal()
    
    valid_download_folder_url_signal = Signal(str)
    invalid_download_folder_url_signal = Signal(str)

    retrieved_initial_youtube_stream_combo_boxes_values_signal = Signal(list, list, list)
    
    created_youtube_thumbnail_pixmap_signal = Signal(QPixmap)

    def __init__(
            self,
            youtube: YouTube,
            thumbnail_size: QSize | None = None,
            log_calls: bool = False):
        
        super().__init__()

        self.youtube = youtube
        self.thumbnail_url: str = self.youtube.thumbnail_url
        self.streams: StreamQuery = self.youtube.streams

        self.thumbnail_size = thumbnail_size

        self.download_folder_line_edit_error_text: str | None = None
        self.download_folder_url: str | None = None

        self.stream_type_options: list[StreamType] | None = None
        self.first_stream_type_option: StreamType | None = None

        self.stream_quality_options: list[str] | None = None
        self.first_stream_quality_option: str | None = None

        self.stream_file_extension_options: list[str] | None = None
        self.first_stream_file_extension_option: str | None = None

        self.log_calls = log_calls

    def retrieve_initial_youtube_stream_combo_boxes_values(self):

        self.stream_type_options = None
        self.stream_type_options = YouTubeHelper.get_stream_type_options(self.streams)
        
        self.first_stream_type_option = None

        if not self.stream_type_options:

            if self.log_calls:
                self.log_call("No stream type options")

            return
        
        self.first_stream_type_option = self.stream_type_options[0]
        
        self.stream_quality_options = None
        
        if self.first_stream_type_option == StreamType.AUDIO_AND_VIDEO:

            self.stream_quality_options = YouTubeHelper.get_stream_video_resolution_options(
                streams = self.streams,
                progressive = True
                )
        
        elif self.first_stream_type_option == StreamType.VIDEO_ONLY:

            self.stream_quality_options = YouTubeHelper.get_stream_video_resolution_options(
                streams = self.streams,
                progressive = False
                )
        
        elif self.first_stream_type_option == StreamType.AUDIO_ONLY:

            self.stream_quality_options = YouTubeHelper.get_stream_audio_resolution_options(
                streams = self.streams,
                )
        
        if not self.stream_quality_options:

            if self.log_calls:
                self.log_call("No stream quality options")

            return

        self.first_stream_quality_option = self.stream_quality_options[0]
        
        self.stream_file_extension_options = None
        
        if self.first_stream_type_option == StreamType.AUDIO_AND_VIDEO:

            self.stream_file_extension_options = YouTubeHelper.get_stream_video_file_extension_options(
                streams = self.streams,
                progressive = True,
                resolution = self.first_stream_quality_option
                )
        
        elif self.first_stream_type_option == StreamType.VIDEO_ONLY:

            self.stream_file_extension_options = YouTubeHelper.get_stream_video_file_extension_options(
                streams = self.streams,
                progressive = False,
                resolution = self.first_stream_quality_option
                )
        
        elif self.first_stream_type_option == StreamType.AUDIO_ONLY:

            self.stream_file_extension_options = YouTubeHelper.get_stream_audio_file_extension_options(
                streams = self.streams,
                abr = self.first_stream_quality_option
                )
        
        self.retrieved_initial_youtube_stream_combo_boxes_values_signal.emit(
            self.stream_type_options,
            self.stream_quality_options,
            self.stream_file_extension_options
            )

        if self.log_calls:
            self.log_call()
    
    def validate_download_folder_url(self):

        try:
            
            self.download_folder_line_edit_error_text = None
            self.download_folder_url = QFileDialog.getExistingDirectoryUrl(self, caption = "Select download folder")

            if self.download_folder_url.isValid():
                
                url_text: str = self.download_folder_url.toLocalFile()
                self.valid_download_folder_url_signal.emit(url_text)
            
            else:
                
                self.download_folder_url = None
                self.download_folder_line_edit_error_text = "ERROR: Invalid folder URL"
                
        except KeyboardInterrupt:

            self.download_folder_line_edit_error_text = "ERROR: Keyboard interrupt"

        except Exception:

            self.download_folder_line_edit_error_text = "ERROR: An error occured"
            
        finally:

            if self.download_folder_line_edit_error_text:

                self.invalid_download_folder_url_signal.emit(self.download_folder_line_edit_error_text)

    def create_youtube_thumbnail_pixmap(self):

        if not self.thumbnail_size:
            return

        thumbnail_pixmap: QPixmap = YouTubeHelper.get_thumbnail(
            size = self.thumbnail_size,
            url = self.thumbnail_url
            )
        
        self.created_youtube_thumbnail_pixmap_signal.emit(thumbnail_pixmap)

        if self.log_calls:
            self.log_call()
        
    def on_activate_stream_type_options_combo_box(self):

        current_stream_type: StreamType = self.stream_type_options_combo_box.currentData(Qt.UserRole)
        
        self.stream_quality_options_combo_box.set_combo_box_items_based_on_streams(
            streams = self.streams,
            stream_type = current_stream_type
            )
        
        current_stream_quality: str = self.stream_quality_options_combo_box.currentText()
        
        self.stream_file_extension_options_combo_box.set_combo_box_items_based_on_streams(
            streams = self.streams,
            stream_type = current_stream_type,
            stream_quality = current_stream_quality
            )
    
    def on_activate_stream_quality_options_combo_box(self):
        
        current_stream_type: StreamType = self.stream_type_options_combo_box.currentData(Qt.UserRole)

        current_stream_quality: str = self.stream_quality_options_combo_box.currentText()
        
        self.stream_file_extension_options_combo_box.set_combo_box_items_based_on_streams(
            streams = self.streams,
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
            
            self.finished_youtube_stream_download_signal.emit()
