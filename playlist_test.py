from pytubefix import Playlist, YouTube

from helpers.youtube_helper import YouTubeHelper
from helpers.format_helper import FormatHelper
from helpers.playlist_helper import PlaylistHelper

import re

if __name__ == "__main__":
    
    invalid_playlist_url = "https://www.youtube.com/watch?v=ApScvH2sgyE&list=PLr4HdpPJJEH0EZHLQVnfeDDWrnGVrFTgI"

    valid_playlist_url = FormatHelper.playlist_url_to_valid_format(invalid_playlist_url)

    print(valid_playlist_url)

    pl = Playlist("https://www.youtube.com/watch?v=ApScvH2sgyE&list=PLr4HdpPJJEH0EZHLQVnfeDDWrnGVrFTgI&pp=gAQBsAgC")

    print(PlaylistHelper.get_common_stream_audio_resolution_options(
        playlist = pl,
        file_extension = "mp4"
        ))
    
    print(PlaylistHelper.get_common_stream_type_options(
        playlist = pl
        ))
    
    print(PlaylistHelper.get_commmon_stream_audio_file_extension_options(
        playlist = pl
    ))


    

