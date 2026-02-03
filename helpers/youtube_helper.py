from pytubefix import StreamQuery

from helpers.format_helper import FormatHelper
from helpers.request_helper import RequestHelper

from enums.stream_type import StreamType

from mutagen.mp4 import MP4, MP4Cover

from PySide6.QtCore import QSize

from PySide6.QtGui import QPixmap, Qt

class YouTubeHelper:

    def get_stream_video_resolution_options(
            streams: StreamQuery,
            ascending_order: bool = True,
            progressive: bool = True,
            file_extension: str | None = None) -> list[str]:

        video_streams: StreamQuery = None

        if file_extension:

            video_streams = streams.filter(
                type = "video", 
                progressive = progressive,
                file_extension = file_extension
                )
        
        else:

            video_streams = streams.filter(
                type = "video", 
                progressive = progressive,
                )
        
        resolutions_set = set()

        for stream in video_streams:

            if stream.resolution not in resolutions_set:
                resolutions_set.add(stream.resolution)

        resolutions_list = []

        if resolutions_set:
            for resolution in resolutions_set:
                resolutions_list.append(resolution)
        
        if ascending_order:
            resolutions_list.sort(key = lambda x: FormatHelper.extract_first_consecutive_number_from_string(x))

        return resolutions_list
    
    def get_stream_audio_resolution_options(
            streams: StreamQuery,
            ascending_order: bool = True,
            file_extension: str | None = None) -> list[str]:
        
        audio_streams: StreamQuery = None

        if file_extension:
            
            audio_streams = streams.filter(
                type = "audio",
                file_extension = file_extension
                )
        
        else:

            audio_streams = streams.filter(type = "audio")

        resolutions_set = set()

        for stream in audio_streams:

            if stream.abr not in resolutions_set:
                resolutions_set.add(stream.abr)

        resolutions_list = []

        if resolutions_set:
            for resolution in resolutions_set:
                resolutions_list.append(resolution)
        
        if ascending_order:
            resolutions_list.sort(key = lambda x: FormatHelper.extract_first_consecutive_number_from_string(x))
        
        return resolutions_list

    def get_stream_type_options(streams: StreamQuery) -> list[StreamType]:
        
        stream_types_list = []

        video_and_audio_streams = streams.filter(
            type = "video",
            progressive = True
            )

        video_streams = streams.filter(
            type = "video",
            progressive = False
            )
        
        audio_streams = streams.filter(
            type = "audio",
            progressive = False
            )
        
        if len(video_and_audio_streams) >= 1:
            stream_types_list.append(StreamType.AUDIO_AND_VIDEO)
        
        if len(video_streams) >= 1:
            stream_types_list.append(StreamType.VIDEO_ONLY)
        
        if len(audio_streams) >= 1:
            stream_types_list.append(StreamType.AUDIO_ONLY)
        
        return stream_types_list
    
    def get_stream_video_file_extension_options(
            streams: StreamQuery,
            progressive: bool = True,
            resolution: str | None = None) -> list[str]:
        
        video_mime_types = set()
        
        filtered_streams: StreamQuery = None

        if resolution:

            filtered_streams: StreamQuery = streams.filter(
                type = "video",
                resolution = resolution,
                progressive = progressive
                )
        
        else:

            filtered_streams: StreamQuery = streams.filter(
                type = "video",
                progressive = progressive
                )
        
        for stream in filtered_streams:
            
            if stream.mime_type in video_mime_types:
                continue

            video_mime_types.add(stream.mime_type)

        video_file_extensions = []

        for mime_type in video_mime_types:

            file_extension: str = mime_type.replace("video/", "")
            video_file_extensions.append(file_extension)
        
        return video_file_extensions
    
    def get_stream_audio_file_extension_options(
            streams: StreamQuery,
            abr: str | None = None) -> list[str]:
        
        audio_mime_types = set()

        filtered_streams: StreamQuery = None

        if abr:
            
            filtered_streams: StreamQuery = streams.filter(
                type = "audio",
                abr = abr
                )
        
        else:

            filtered_streams: StreamQuery = streams.filter(
                type = "audio",
                )
        
        for stream in filtered_streams:
            
            if stream.mime_type in audio_mime_types:
                continue

            audio_mime_types.add(stream.mime_type)

        audio_file_extensions = []

        for mime_type in audio_mime_types:

            file_extension: str = mime_type.replace("audio/", "")
            audio_file_extensions.append(file_extension)
        
        return audio_file_extensions

    #   TODO handle exceptions
    def set_mp4_audio_file_metadata(
            audio_filepath: str,
            title: str | None = None,
            author: str | None = None,
            thumbnail: list[MP4Cover] | None = None
            ):
        
        audio_file = MP4(audio_filepath)

        if title:
            audio_file["\xa9nam"] = title
        
        if author:
            audio_file["\xa9ART"] = author

        if thumbnail:
            audio_file["covr"] = thumbnail
        
        audio_file.save()

    def get_thumbnail(size: QSize, url: str) -> QPixmap:

        response = RequestHelper.get(url)

        pixmap = QPixmap()
        pixmap.loadFromData(response.content)

        scaled_pixmap: QPixmap = pixmap.scaled(
            size,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
            )
        
        return scaled_pixmap

           







                

        


