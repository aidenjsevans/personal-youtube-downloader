from widgets.main_window import MainWindow

from PySide6.QtWidgets import QApplication

from enums.image_format import ImageFormat

from widgets.views.youtube_url_search_view.youtube_url_search_view import YouTubeUrlSearchView
from widgets.views.youtube_url_search_view.labels.youtube_url_line_edit_label import YouTubeUrlLineEditLabel
from widgets.views.youtube_url_search_view.line_edits.youtube_url_line_edit import YouTubeUrlLineEdit
from widgets.views.youtube_url_search_view.buttons.search_youtube_media_push_button import SearchYoutubeMediaPushButton

from widgets.views.youtube_download_view.youtube_download_view import YoutubeDownloadView
from widgets.views.youtube_download_view.labels.youtube_thumbnail_label import YoutubeThumbnailLabel
from widgets.views.youtube_download_view.pixmaps.youtube_thumbnail_pixmap import YoutubeThumbnailPixmap
from widgets.views.youtube_download_view.labels.download_folder_line_edit_label import DownloadFolderLineEditLabel
from widgets.views.youtube_download_view.line_edits.download_folder_line_edit import DownloadFolderLineEdit
from widgets.views.youtube_download_view.buttons.select_download_folder_push_button import SelectDownloadFolderPushButton
from widgets.views.youtube_download_view.combo_boxes.stream_type_options_combo_box import StreamTypeOptionsComboBox
from widgets.views.youtube_download_view.labels.stream_type_options_combo_box_label import StreamTypeOptionsComboBoxLabel
from widgets.views.youtube_download_view.labels.stream_quality_options_combo_box_label import StreamQualityOptionsComboBoxLabel
from widgets.views.youtube_download_view.combo_boxes.stream_quality_options_combo_box import StreamQualityOptionsComboBox
from widgets.views.youtube_download_view.buttons.download_youtube_stream_push_button import DownloadYoutubeStreamPushButton
from widgets.views.youtube_download_view.labels.stream_file_extension_options_combo_box_label import StreamFileExtensionOptionsComboBoxLabel
from widgets.views.youtube_download_view.combo_boxes.stream_file_extension_options_combo_box import StreamFileExtensionOptionsComboBox

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
        search_youtube_media_push_button = SearchYoutubeMediaPushButton(),
        log_calls = True
        )
    
    youtube_download_view = YoutubeDownloadView(
        
        youtube_thumbnail_label = YoutubeThumbnailLabel(
            youtube_thumbnail_pixmap = YoutubeThumbnailPixmap(),
            log_calls = True
            ),
        
        download_folder_line_edit_label = DownloadFolderLineEditLabel(),
        download_folder_line_edit = DownloadFolderLineEdit(),
        select_download_folder_push_button = SelectDownloadFolderPushButton(),
        stream_type_options_combo_box_label = StreamTypeOptionsComboBoxLabel(),
        stream_type_options_combo_box = StreamTypeOptionsComboBox(log_calls = True),
        stream_quality_options_combo_box_label = StreamQualityOptionsComboBoxLabel(),
        stream_quality_options_combo_box = StreamQualityOptionsComboBox(),
        download_youtube_stream_push_button = DownloadYoutubeStreamPushButton(),
        stream_file_extension_options_combo_box_label = StreamFileExtensionOptionsComboBoxLabel(),
        stream_file_extension_options_combo_box = StreamFileExtensionOptionsComboBox(log_calls = True),
        thumbnail_metadata_format = ImageFormat.JPEG,
        log_calls = True
        )
    
    window = MainWindow(
        x_position_px = 500,
        y_position_px = 500,
        width_px = 600,
        height_px = 200,
        youtube_url_search_view = youtube_url_search_view,
        youtube_download_view = youtube_download_view,
        log_calls = True
        )
    
    window.show()
    app.exec()