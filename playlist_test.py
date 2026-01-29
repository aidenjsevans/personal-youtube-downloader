from pytubefix import Playlist, YouTube

from helpers.youtube_helper import YouTubeHelper
from helpers.format_helper import FormatHelper
from helpers.playlist_helper import PlaylistHelper

from PySide6.QtWidgets import QApplication, QMainWindow

from PySide6.QtCore import Qt

from widgets.views.youtube_download_view.combo_boxes.stream_type_options_combo_box import StreamTypeOptionsComboBox
from widgets.views.youtube_download_view.combo_boxes.stream_file_extension_options_combo_box import StreamFileExtensionOptionsComboBox
from widgets.views.youtube_download_view.combo_boxes.stream_quality_options_combo_box import StreamQualityOptionsComboBox

import sys

import re

if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    pl = Playlist(
        "https://www.youtube.com/watch?v=ApScvH2sgyE&list=PLr4HdpPJJEH0EZHLQVnfeDDWrnGVrFTgI&pp=gAQBsAgC"
        )

    stream_type_combo_box = StreamTypeOptionsComboBox()
    stream_type_combo_box.set_combo_box_items_based_on_playlist(pl)

    stream_file_extension_combo_box = StreamFileExtensionOptionsComboBox()
    stream_file_extension_combo_box.set_combo_box_items_based_on_playlist(pl, stream_type_combo_box.currentData(Qt.UserRole))

    stream_quality_combo_box = StreamQualityOptionsComboBox()
    stream_quality_combo_box.set_combo_box_items_based_on_playlist(pl, stream_type_combo_box.currentData(Qt.UserRole), stream_file_extension_combo_box.currentText())

    stream_quality_combo_box.show()

    sys.exit(app.exec())
    
    
    


    

