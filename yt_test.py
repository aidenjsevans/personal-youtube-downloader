from pytubefix import YouTube

from helpers.youtube_helper import YouTubeHelper

if __name__ == "__main__":

    yt = YouTube("https://youtu.be/HjTJ2aL_55U")
    streams = yt.streams

    for stream in streams:
        print(stream)

    print(f"\n")

    print(YouTubeHelper.get_stream_video_resolution_options(streams))
    print(YouTubeHelper.get_stream_audio_resolution_options(streams))
    print(YouTubeHelper.get_stream_type_options(streams))

    print(YouTubeHelper.get_stream_video_file_extension_options(
        streams = streams,
        resolution = "1080p",
        progressive = False
        ))
    
    print(YouTubeHelper.get_stream_audio_file_extension_options(
        streams = streams,
        abr = "160kbps"
        ))
    
    print(YouTubeHelper.get_stream_audio_resolution_options(
        streams = streams,
        file_extension = "mp4"
    ))