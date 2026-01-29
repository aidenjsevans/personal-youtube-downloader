from widgets.main_window import MainWindow

from PySide6.QtWidgets import QApplication

from enums.image_format import ImageFormat

from widgets.style_sheets.light_theme import light_theme
from widgets.style_sheets.dark_theme import dark_theme

from widgets.views.youtube_url_search_view.youtube_url_search_view import YouTubeUrlSearchView
from widgets.views.youtube_url_search_view.pixmaps.youtube_icon_pixmap import YouTubeIconPixmap
from widgets.views.youtube_url_search_view.labels.youtube_icon_label import YouTubeIconLabel
from widgets.views.youtube_url_search_view.labels.youtube_url_line_edit_label import YouTubeUrlLineEditLabel
from widgets.views.youtube_url_search_view.line_edits.youtube_url_line_edit import YouTubeUrlLineEdit
from widgets.views.youtube_url_search_view.buttons.search_youtube_media_push_button import SearchYoutubeMediaPushButton
from widgets.views.youtube_url_search_view.check_boxes.playlist_url_check_box import PlaylistUrlCheckBox

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

from widgets.views.youtube_playlist_download_view.youtube_playlist_download_view import YoutubePlaylistDownloadView

from widgets.views.loading_view.loading_view import LoadingView
from widgets.custom.circle_loading_widget import CircleLoadingWidget

from widgets.tool_bars.main_tool_bar.main_tool_bar import MainToolBar
from widgets.tool_bars.main_tool_bar.actions.return_to_previous_view_action import ReturnToPreviousViewAction

if __name__ == "__main__":

    app = QApplication()

    app.setStyleSheet(dark_theme)

    main_tool_bar = MainToolBar(
        return_to_previous_view_action = ReturnToPreviousViewAction()
        )

    youtube_url_search_view = YouTubeUrlSearchView(

        youtube_icon_label = YouTubeIconLabel(
            youtube_icon_pixmap = YouTubeIconPixmap()
            ),

        youtube_url_line_edit_label = YouTubeUrlLineEditLabel(),
        youtube_url_line_edit = YouTubeUrlLineEdit(),
        search_youtube_media_push_button = SearchYoutubeMediaPushButton(),
        playlist_url_check_box = PlaylistUrlCheckBox(),
        log_calls = True
        )
    
    youtube_download_view = YoutubeDownloadView(
        
        youtube_thumbnail_label = YoutubeThumbnailLabel(
            youtube_thumbnail_pixmap = YoutubeThumbnailPixmap(),
            ),
        
        download_folder_line_edit_label = DownloadFolderLineEditLabel(),
        download_folder_line_edit = DownloadFolderLineEdit(),
        select_download_folder_push_button = SelectDownloadFolderPushButton(),
        stream_type_options_combo_box_label = StreamTypeOptionsComboBoxLabel(),
        stream_type_options_combo_box = StreamTypeOptionsComboBox(),
        stream_quality_options_combo_box_label = StreamQualityOptionsComboBoxLabel(),
        stream_quality_options_combo_box = StreamQualityOptionsComboBox(),
        download_youtube_stream_push_button = DownloadYoutubeStreamPushButton(),
        stream_file_extension_options_combo_box_label = StreamFileExtensionOptionsComboBoxLabel(),
        stream_file_extension_options_combo_box = StreamFileExtensionOptionsComboBox(),
        thumbnail_metadata_format = ImageFormat.JPEG,
        )
    
    youtube_playlist_download_view = YoutubePlaylistDownloadView(

        youtube_thumbnail_label = YoutubeThumbnailLabel(
            youtube_thumbnail_pixmap = YoutubeThumbnailPixmap(),
            ),
        
        download_folder_line_edit_label = DownloadFolderLineEditLabel(),
        download_folder_line_edit = DownloadFolderLineEdit(),
        select_download_folder_push_button = SelectDownloadFolderPushButton(),
        stream_type_options_combo_box_label = StreamTypeOptionsComboBoxLabel(),
        stream_type_options_combo_box = StreamTypeOptionsComboBox(),
        stream_quality_options_combo_box_label = StreamQualityOptionsComboBoxLabel(),
        stream_quality_options_combo_box = StreamQualityOptionsComboBox(),
        download_youtube_stream_push_button = DownloadYoutubeStreamPushButton(),
        stream_file_extension_options_combo_box_label = StreamFileExtensionOptionsComboBoxLabel(),
        stream_file_extension_options_combo_box = StreamFileExtensionOptionsComboBox(),
        thumbnail_metadata_format = ImageFormat.JPEG,
        log_calls = True
        )
    
    loading_view = LoadingView(
        
        circle_loading_widget = CircleLoadingWidget(
            pen_width = 5,
            radius = 50
            )
        )
    
    window = MainWindow(
        x_position_px = 500,
        y_position_px = 500,
        width_px = 800,
        height_px = 400,
        tool_bar = main_tool_bar,
        youtube_url_search_view = youtube_url_search_view,
        youtube_download_view = youtube_download_view,
        youtube_playlist_download_view = youtube_playlist_download_view,
        loading_view = loading_view,
        )
    
    window.show()
    app.exec()