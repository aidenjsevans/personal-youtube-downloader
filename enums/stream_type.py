from enum import Enum

class StreamType(Enum):
    AUDIO_ONLY = "Audio"
    VIDEO_ONLY = "Video"
    AUDIO_AND_VIDEO = "Audio + Video"