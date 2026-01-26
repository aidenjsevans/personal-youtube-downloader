from PySide6.QtWidgets import QCheckBox

class PlaylistUrlCheckBox(QCheckBox):

    def __init__(self):

        super().__init__()

        self.setText("Playlist URL")