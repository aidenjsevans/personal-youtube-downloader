from PySide6.QtWidgets import QComboBox

from pytubefix import StreamQuery, Playlist

from helpers.youtube_helper import YouTubeHelper
from helpers.playlist_helper import PlaylistHelper

from enums.stream_type import StreamType

from mixins.method_log_mixin import MethodLogMixin

class StreamFileExtensionOptionsComboBox(QComboBox, MethodLogMixin):

    def __init__(
            self,
            log_calls: bool = False,
            parent = None):

        super().__init__(parent = parent)

        self.log_calls = log_calls

    def set_combo_box_items_based_on_streams(
            self, 
            streams: StreamQuery,
            stream_type: StreamType,
            stream_quality: str | None = None):

        self.clear()

        stream_file_extension_options: list[str] = []

        if stream_type == StreamType.AUDIO_AND_VIDEO:

            stream_file_extension_options = YouTubeHelper.get_stream_video_file_extension_options(
                streams = streams,
                resolution = stream_quality,
                progressive = True
                )
        
        elif stream_type == StreamType.VIDEO_ONLY:

            stream_file_extension_options = YouTubeHelper.get_stream_video_file_extension_options(
                streams = streams,
                resolution = stream_quality,
                progressive = False
                )
        
        elif stream_type == StreamType.AUDIO_ONLY:

            stream_file_extension_options = YouTubeHelper.get_stream_audio_file_extension_options(
                streams = streams,
                abr = stream_quality
                )
        
        for file_extension in stream_file_extension_options:
            self.addItem(file_extension)
        
        if self.log_calls:
            self.log_call(message = f"{stream_file_extension_options}")
    
    def set_combo_box_items_based_on_playlist(
            self, 
            playlist: Playlist,
            stream_type: StreamType,
            stream_quality: str | None = None):

        self.clear()

        common_stream_file_extension_options: list[str] = []

        if stream_type == StreamType.AUDIO_AND_VIDEO:

            common_stream_file_extension_options = PlaylistHelper.get_commmon_stream_video_file_extension_options(
                playlist = playlist,
                progressive = True,
                resolution = stream_quality
                )

        elif stream_type == StreamType.VIDEO_ONLY:

            common_stream_file_extension_options = PlaylistHelper.get_commmon_stream_video_file_extension_options(
                playlist = playlist,
                progressive = False,
                resolution = stream_quality
                )
        
        elif stream_type == StreamType.AUDIO_ONLY:

            common_stream_file_extension_options = PlaylistHelper.get_commmon_stream_audio_file_extension_options(
                playlist = playlist,
                abr = stream_quality
                )
        
        for common_file_extension in common_stream_file_extension_options:
            self.addItem(common_file_extension)
        
        if self.log_calls:
            self.log_call(message = f"{common_stream_file_extension_options}")
        
