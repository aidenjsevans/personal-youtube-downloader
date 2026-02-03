from PySide6.QtWidgets import QLineEdit

from PySide6.QtGui import QIcon, QAction

class DownloadFolderLineEdit(QLineEdit):

    def __init__(self, parent = None):

        super().__init__(parent = parent)

        self.placeholder_text: str = "Download Folder URL"
        self.default_style_sheet: str = "color: white;"
        self.error_style_sheet: str = "color: red;"

        clear_action: QAction = self.addAction(
            QIcon("icons/backspace.svg"),
            QLineEdit.TrailingPosition
            )
        
        clear_action.triggered.connect(self.clear_action)

        self.setReadOnly(True)
        self.clear_action()
    
    def reset(self):

        self.setPlaceholderText(self.placeholder_text)
        self.setStyleSheet(self.default_style_sheet)
    
    def clear_action(self):

        self.clear()
        self.reset()

    def set_error_text(self, error_text: str):

        self.setPlaceholderText(error_text)
        self.setStyleSheet(self.error_style_sheet)
    