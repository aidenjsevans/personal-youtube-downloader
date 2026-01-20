from pytubefix import YouTube, StreamQuery

from helpers.format_helper import FormatHelper

from enums.stream_type import StreamType

import re

class YouTubeHelper:

    def get_stream_video_resolution_options(
            streams: StreamQuery,
            ascending_order: bool = True,
            progressive: bool = True) -> list[str]:

        video_streams = streams.filter(
            type = "video", 
            progressive = progressive
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
            ascending_order: bool = True) -> list[str]:
        
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
            resolution: str,
            progressive: bool = True) -> list[str]:
        
        video_mime_types = set()
        
        filtered_streams: StreamQuery = streams.filter(
            type = "video",
            resolution = resolution,
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
            abr: str) -> list[str]:
        
        audio_mime_types = set()
        
        filtered_streams: StreamQuery = streams.filter(
            type = "audio",
            abr = abr
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
        





                

        


