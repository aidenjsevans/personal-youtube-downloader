from PySide6.QtWidgets import QPushButton, QWidget

from mixins.push_button_mixin import PushButtonMixin

class SearchYoutubeMediaPushButton(QPushButton, PushButtonMixin):

    def __init__(self, parent = None):
          
        super().__init__(parent = parent)
        
        self.setText("Search")