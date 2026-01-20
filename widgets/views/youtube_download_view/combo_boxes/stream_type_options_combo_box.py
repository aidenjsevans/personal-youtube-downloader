from PySide6.QtWidgets import QComboBox

from PySide6.QtCore import Qt, Signal

from pytubefix import StreamQuery

from helpers.youtube_helper import YouTubeHelper

from enums.stream_type import StreamType

from mixins.method_log_mixin import MethodLogMixin

class StreamTypeOptionsComboBox(QComboBox, MethodLogMixin):

    def __init__(
            self,
            log_calls: bool = False,
            parent = None):

        super().__init__(parent = parent)

        self.log_calls = log_calls

    def set_combo_box_items(self, streams: StreamQuery):

        self.clear()

        stream_type_options: list[StreamType] = YouTubeHelper.get_stream_type_options(streams)

        for stream_type in stream_type_options:
            
            self.addItem(
                stream_type.value,
                userData = stream_type
                )
        
        if self.log_calls:
            self.log_call(message = "Success")
    




