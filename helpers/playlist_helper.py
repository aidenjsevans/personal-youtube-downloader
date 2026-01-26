from helpers.youtube_helper import YouTubeHelper

from pytubefix import YouTube, Playlist

from helpers.format_helper import FormatHelper

from enums.stream_type import StreamType

class PlaylistHelper:

    def get_common_stream_video_resolution_options(
        playlist: Playlist,
        ascending_order: bool = True,
        progressive: bool = True,
        file_extension: str | None = None) -> list[str]:

        all_resolutions_list: list[set] = []

        for youtube in playlist.videos:
            
            resolutions_list: list[str] = YouTubeHelper.get_stream_video_resolution_options(
                streams = youtube.streams,
                ascending_order = False,
                progressive = progressive,
                file_extension = file_extension
                )
            
            all_resolutions_list.append(set(resolutions_list))
        
        common_resolutions_set = set.intersection(*all_resolutions_list)
        common_resolutions_list = list(common_resolutions_set)

        if ascending_order:
            common_resolutions_list.sort(key = lambda x: FormatHelper.extract_first_consecutive_number_from_string(x))

        return common_resolutions_list

    def get_common_stream_audio_resolution_options(
            playlist: Playlist,
            ascending_order: bool = True,
            file_extension: str | None = None):
        
        all_resolutions_list: list[set] = []

        for youtube in playlist.videos:
            
            resolutions_list: list[str] = YouTubeHelper.get_stream_audio_resolution_options(
                streams = youtube.streams,
                ascending_order = False,
                file_extension = file_extension
                )
            
            all_resolutions_list.append(set(resolutions_list))
        
        common_resolutions_set = set.intersection(*all_resolutions_list)
        common_resolutions_list = list(common_resolutions_set)

        if ascending_order:
            common_resolutions_list.sort(key = lambda x: FormatHelper.extract_first_consecutive_number_from_string(x))

        return common_resolutions_list
    
    def get_common_stream_type_options(playlist: Playlist):

        all_stream_types_list: list[set] = []

        for youtube in playlist.videos:

            stream_types_list: list[StreamType] = YouTubeHelper.get_stream_type_options(youtube.streams)
            all_stream_types_list.append(set(stream_types_list))
        
        common_stream_types_set = set.intersection(*all_stream_types_list)
        common_stream_types_list = list(common_stream_types_set)

        return common_stream_types_list

    def get_commmon_stream_video_file_extension_options(
            playlist: Playlist,
            progressive: bool = True,
            resolution: str | None = None):

        all_video_file_extensions_options: list[set] = []

        for youtube in playlist.videos:

            video_file_extensions_list: list[str] = YouTubeHelper.get_stream_video_file_extension_options(
                streams = youtube.streams,
                progressive = progressive,
                resolution = resolution
                )

            all_video_file_extensions_options.append(set(video_file_extensions_list))
        
        common_video_file_extensions_set = set.intersection(*all_video_file_extensions_options)
        common_video_file_extensions_list = list(common_video_file_extensions_set)

        return common_video_file_extensions_list

    def get_commmon_stream_audio_file_extension_options(
            playlist: Playlist,
            abr: str | None = None):

        all_audio_file_extensions_options: list[set] = []

        for youtube in playlist.videos:

            audio_file_extensions_list: list[str] = YouTubeHelper.get_stream_audio_file_extension_options(
                streams = youtube.streams,
                abr = abr
                )

            all_audio_file_extensions_options.append(set(audio_file_extensions_list))
        
        common_audio_file_extensions_set = set.intersection(*all_audio_file_extensions_options)
        common_audio_file_extensions_list = list(common_audio_file_extensions_set)

        return common_audio_file_extensions_list
        




