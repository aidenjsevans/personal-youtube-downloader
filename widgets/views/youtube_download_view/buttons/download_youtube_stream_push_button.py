from PySide6.QtWidgets import QPushButton, QWidget

class DownloadYoutubeStreamPushButton(QPushButton):

    def __init__(self, parent = None):
          
        super().__init__(parent = parent)
        
        self.setText("Download")