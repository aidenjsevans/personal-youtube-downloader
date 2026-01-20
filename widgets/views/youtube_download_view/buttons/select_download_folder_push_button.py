from PySide6.QtWidgets import QPushButton, QWidget
from PySide6.QtGui import QIcon

class SelectDownloadFolderPushButton(QPushButton):

    def __init__(self, parent = None):
          
        super().__init__(parent = parent)
        
        self.setIcon(QIcon("icons/folder.svg"))

        

