from PySide6.QtCore import QObject, Signal

from pytubefix import YouTube, Playlist
from pytubefix.exceptions import RegexMatchError, VideoUnavailable

from mixins.method_log_mixin import MethodLogMixin

class YouTubeUrlSearchViewWorker(QObject, MethodLogMixin):

    search_for_youtube_playlist_finished_signal = Signal(Playlist)
    search_for_youtube_stream_finished_signal = Signal(YouTube)
    search_for_youtube_media_error_signal = Signal(str)

    def __init__(
            self,
            youtube_url: str,
            is_playlist_check_box_checked: bool,
            log_calls: bool = False):

        super().__init__()

        self.youtube_url = youtube_url
        self.is_playlist_check_box_checked = is_playlist_check_box_checked
        self.youtube_url_line_edit_error_text: str | None = None

        self.log_calls = log_calls

    def search_for_youtube_media(self):

        try:

            self.youtube_url_line_edit_error_text = None

            if not self.youtube_url:

                self.youtube_url_line_edit_error_text = "ERROR: YouTube URL required"
                return
            
            #   TODO user option to skip exception
            if self.is_playlist_check_box_checked:
                
                playlist = Playlist(url = self.youtube_url)

                for youtube in playlist.videos:
                    youtube.check_availability()
                
                self.search_for_youtube_playlist_finished_signal.emit(playlist)
                
            else:

                youtube = YouTube(url = self.youtube_url)
                youtube.check_availability()

                self.search_for_youtube_stream_finished_signal.emit(youtube)
        
        except RegexMatchError:
            self.youtube_url_line_edit_error_text = "ERROR: Invalid YouTube URL"

        except VideoUnavailable:
            self.youtube_url_line_edit_error_text = "ERROR: Video unavailable"

        finally:
            
            if self.youtube_url_line_edit_error_text:

                #self.fail_searching()
                self.search_for_youtube_media_error_signal.emit(self.youtube_url_line_edit_error_text)
                
                if self.log_calls:
                    self.log_call(message = f'"{self.youtube_url_line_edit_error_text}"')

            if self.log_calls:
                self.log_call()
