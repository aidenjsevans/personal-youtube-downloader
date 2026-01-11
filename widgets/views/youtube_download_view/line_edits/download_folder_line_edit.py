from PySide6.QtWidgets import QLineEdit

class DownloadFolderLineEdit(QLineEdit):

    def __init__(self):

        self.placeholder_text: str = "Download Folder URL"
        self.default_style_sheet: str = "color: white;"
        self.error_style_sheet: str = "color: red;"

        super().__init__()

        self.reset()
    
    def reset(self):
        self.setPlaceholderText(self.placeholder_text)
        self.setStyleSheet(self.default_style_sheet)