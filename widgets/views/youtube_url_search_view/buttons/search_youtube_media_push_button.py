from PySide6.QtWidgets import QPushButton

from PySide6.QtGui import QIcon

class SearchYoutubeMediaPushButton(QPushButton):

    def __init__(
            self, 
            default_text: str = "Search",
            parent = None):
          
        super().__init__(parent = parent)

        self.default_text = default_text
        
        self.reset()
    
    def reset(self):
        self.setText(self.default_text)

    def set_searching(self):
        self.setText("")