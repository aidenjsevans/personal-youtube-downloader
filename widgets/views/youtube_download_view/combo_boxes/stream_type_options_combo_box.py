from PySide6.QtWidgets import QComboBox

from pytubefix import StreamQuery, Playlist

from helpers.youtube_helper import YouTubeHelper
from helpers.playlist_helper import PlaylistHelper

from enums.stream_type import StreamType

from mixins.method_log_mixin import MethodLogMixin

class StreamTypeOptionsComboBox(QComboBox, MethodLogMixin):

    def __init__(
            self,
            log_calls: bool = False,
            parent = None):

        super().__init__(parent = parent)

        self.log_calls = log_calls

    def set_combo_box_items_based_on_streams(
            self, 
            streams: StreamQuery):

        self.clear()

        stream_type_options: list[StreamType] = YouTubeHelper.get_stream_type_options(streams)

        for stream_type in stream_type_options:
            
            self.addItem(
                stream_type.value,
                userData = stream_type
                )
        
        if self.log_calls:
            self.log_call(message = "Success")
        
    def set_combo_box_items_based_on_playlist(
            self, 
            playlist: Playlist):

        self.clear()

        common_stream_type_options: list[StreamType] = PlaylistHelper.get_common_stream_type_options(playlist)

        for common_stream_type in common_stream_type_options:
            
            self.addItem(
                common_stream_type.value,
                userData = common_stream_type
                )
        
        if self.log_calls:
            self.log_call(message = "Success")
        



