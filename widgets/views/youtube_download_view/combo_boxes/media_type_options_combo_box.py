from PySide6.QtWidgets import QComboBox

from enums.stream_type import StreamType

class MediaTypeOptionsComboBox(QComboBox):

    def __init__(self):

        super().__init__()

        self.addItem(StreamType.AUDIO_ONLY.value)
        self.addItem(StreamType.VIDEO_ONLY.value)
        self.addItem(StreamType.AUDIO_AND_VIDEO.value)

