from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QIcon

from mixins.push_button_mixin import PushButtonMixin

class SelectDownloadFolderPushButton(QPushButton, PushButtonMixin):

    def __init__(self,):
          
        super().__init__()

        self.setIcon(QIcon("icons/folder.svg"))
        

