from PySide6.QtWidgets import QLabel

class DownloadFolderLineEditLabel(QLabel):

    def __init__(self, parent = None):
        
        super().__init__(parent = parent)
        
        self.setText("Download Folder")