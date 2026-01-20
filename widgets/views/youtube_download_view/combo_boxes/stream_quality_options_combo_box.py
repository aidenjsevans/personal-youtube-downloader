from PySide6.QtWidgets import QComboBox

from pytubefix import StreamQuery

from helpers.youtube_helper import YouTubeHelper

from enums.stream_type import StreamType

from mixins.method_log_mixin import MethodLogMixin

class StreamQualityOptionsComboBox(QComboBox, MethodLogMixin):

    def __init__(
            self,
            log_calls: bool = False,
            parent = None):

        super().__init__(parent = parent)

        self.log_calls = log_calls
    
    def set_combo_box_items(
            self, 
            streams: StreamQuery,
            stream_type: StreamType):
        
        self.clear()

        stream_quality_options: list[str] = []

        if stream_type == StreamType.AUDIO_AND_VIDEO:

            stream_quality_options = YouTubeHelper.get_stream_video_resolution_options(
                streams = streams,
                progressive = True
                )
        
        elif stream_type == StreamType.VIDEO_ONLY:

            stream_quality_options = YouTubeHelper.get_stream_video_resolution_options(
                streams = streams,
                progressive = False
                )
        
        elif stream_type == StreamType.AUDIO_ONLY:

            stream_quality_options = YouTubeHelper.get_stream_audio_resolution_options(streams)

        for stream_quality in stream_quality_options:
            self.addItem(stream_quality)
