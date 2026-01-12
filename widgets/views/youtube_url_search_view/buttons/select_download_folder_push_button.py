from PySide6.QtWidgets import QPushButton, QWidget
from PySide6.QtGui import QIcon

from mixins.push_button_mixin import PushButtonMixin

class SelectDownloadFolderPushButton(QPushButton, PushButtonMixin):

    def __init__(self, parent = None):
          
        super().__init__(parent = parent)
        
        self.setIcon(QIcon("icons/folder.svg"))

        

