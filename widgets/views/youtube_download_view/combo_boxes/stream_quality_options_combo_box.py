from PySide6.QtWidgets import QComboBox

from pytubefix import StreamQuery, Playlist

from helpers.youtube_helper import YouTubeHelper
from helpers.playlist_helper import PlaylistHelper

from enums.stream_type import StreamType

from mixins.method_log_mixin import MethodLogMixin

class StreamQualityOptionsComboBox(QComboBox, MethodLogMixin):

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
            file_extension: str | None = None):
        
        self.clear()

        stream_quality_options: list[str] = []

        if stream_type == StreamType.AUDIO_AND_VIDEO:

            stream_quality_options = YouTubeHelper.get_stream_video_resolution_options(
                streams = streams,
                progressive = True,
                file_extension = file_extension
                )
        
        elif stream_type == StreamType.VIDEO_ONLY:

            stream_quality_options = YouTubeHelper.get_stream_video_resolution_options(
                streams = streams,
                progressive = False,
                file_extension = file_extension
                )
        
        elif stream_type == StreamType.AUDIO_ONLY:

            stream_quality_options = YouTubeHelper.get_stream_audio_resolution_options(
                streams = streams,
                file_extension = file_extension
                )

        for stream_quality in stream_quality_options:
            self.addItem(stream_quality)
    
    def set_combo_box_items_based_on_playlist(
            self, 
            playlist: Playlist,
            stream_type: StreamType,
            file_extension: str | None = None):

            self.clear()

            common_stream_quality_options: list[str] = []

            if stream_type == StreamType.AUDIO_AND_VIDEO:

                common_stream_quality_options = PlaylistHelper.get_common_stream_video_resolution_options(
                    playlist = playlist,
                    progressive = True,
                    file_extension = file_extension
                    )

            elif stream_type == StreamType.VIDEO_ONLY:

                common_stream_quality_options = PlaylistHelper.get_common_stream_video_resolution_options(
                    playlist = playlist,
                    progressive = False,
                    file_extension = file_extension
                    )

            elif stream_type == StreamType.AUDIO_ONLY:

                common_stream_quality_options = PlaylistHelper.get_common_stream_audio_resolution_options(
                    playlist = playlist,
                    file_extension = file_extension
                    )

            for common_stream_quality in common_stream_quality_options:
                self.addItem(common_stream_quality)
