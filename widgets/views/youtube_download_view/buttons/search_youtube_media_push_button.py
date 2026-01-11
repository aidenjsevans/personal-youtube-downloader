from PySide6.QtWidgets import QPushButton

from mixins.push_button_mixin import PushButtonMixin

class SearchYoutubeMediaPushButton(QPushButton, PushButtonMixin):

    def __init__(self,):
          
        super().__init__()
        
        self.setText("Search")