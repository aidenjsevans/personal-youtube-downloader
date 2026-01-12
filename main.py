from widgets.main_window import MainWindow

from PySide6.QtWidgets import QApplication

from widgets.views.youtube_url_search_view.youtube_url_search_view import YouTubeUrlSearchView
from widgets.views.youtube_url_search_view.labels.youtube_url_line_edit_label import YouTubeUrlLineEditLabel
from widgets.views.youtube_url_search_view.line_edits.youtube_url_line_edit import YouTubeUrlLineEdit
from widgets.views.youtube_url_search_view.buttons.search_youtube_media_push_button import SearchYoutubeMediaPushButton

from widgets.views.youtube_download_view.youtube_download_view import YoutubeDownloadView
from widgets.views.youtube_download_view.labels.youtube_thumbnail_label import YoutubeThumbnailLabel
from widgets.views.youtube_download_view.pixmaps.youtube_thumbnail_pixmap import YoutubeThumbnailPixmap

if __name__ == "__main__":

    app = QApplication()

    app.setStyleSheet("""
        QPushButton {
            padding: 5px 5px 5px 5px;
        }
        QLabel {
            padding: 5px 5px 5px 5px;
        }
        QLineEdit {
            padding: 5px 5px 5px 5px;
        }             
                                 
    """)

    youtube_url_search_view = YouTubeUrlSearchView(
        youtube_url_line_edit_label = YouTubeUrlLineEditLabel(),
        youtube_url_line_edit = YouTubeUrlLineEdit(),
        #download_folder_line_edit_label = DownloadFolderLineEditLabel(),
        #download_folder_line_edit = DownloadFolderLineEdit(),
        #select_download_folder_push_button = SelectDownloadFolderPushButton(),
        search_youtube_media_push_button = SearchYoutubeMediaPushButton(),
        )
    
    youtube_download_view = YoutubeDownloadView(
        
        youtube_thumbnail_label = YoutubeThumbnailLabel(
            youtube_thumbnail_pixmap = YoutubeThumbnailPixmap()
            )
    )
    
    window = MainWindow(
        x_position_px = 500,
        y_position_px = 500,
        width_px = 600,
        height_px = 200,
        youtube_url_search_view = youtube_url_search_view,
        youtube_download_view = youtube_download_view
        )
    
    window.show()
    app.exec()