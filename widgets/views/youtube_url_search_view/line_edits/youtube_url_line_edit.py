from PySide6.QtWidgets import QLineEdit

class YouTubeUrlLineEdit(QLineEdit):

    def __init__(self, parent = None):

        self.placeholder_text: str = "YouTube URL"
        self.default_style_sheet: str = "color: white;"
        self.error_style_sheet: str = "color: red;"

        super().__init__(parent = parent)

        self.reset()
    
    def reset(self):
        
        self.setPlaceholderText(self.placeholder_text)
        self.setStyleSheet(self.default_style_sheet)

    def set_error_text(self, error_text: str):
        
        self.setPlaceholderText(error_text)
        self.setStyleSheet(self.error_style_sheet)