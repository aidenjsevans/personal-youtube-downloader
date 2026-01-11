from PySide6.QtWidgets import QLabel

class DownloadFolderLineEditLabel(QLabel):

    def __init__(self):
        super().__init__()
        self.setText("Download Folder")