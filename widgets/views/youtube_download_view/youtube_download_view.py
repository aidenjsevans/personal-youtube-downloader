from PySide6.QtWidgets import (
    QWidget, QGridLayout, QLineEdit,
    QLabel, QPushButton, QFileDialog)

from PySide6.QtCore import (
    QUrl)

from mixins.push_button_mixin import PushButtonMixin

class YouTubeDownloadView(QWidget):

    def __init__(
            self,
            youtube_url_line_edit_label: QLabel,
            youtube_url_line_edit: QLineEdit,
            download_folder_line_edit_label: QLabel,
            download_folder_line_edit: QLineEdit,
            select_download_folder_push_button: QPushButton | PushButtonMixin):
        
        self.youtube_url_line_edit_label = youtube_url_line_edit_label
        self.youtube_url_line_edit = youtube_url_line_edit
        self.download_folder_line_edit_label = download_folder_line_edit_label

        self.download_folder_line_edit = download_folder_line_edit
        self.download_folder_line_edit.textEdited.connect(self.on_edit_download_folder_line_edit)

        self.select_download_folder_push_button = select_download_folder_push_button
        select_download_folder_push_button.connect_method(self.select_download_folder)
        
        self.download_folder_url: QUrl = QUrl()
        self.download_folder_line_edit_error_text: str | None = None
        self.download_folder_line_edit_started_typing: bool = False

        super().__init__()

        layout = QGridLayout()

        layout.addWidget(self.youtube_url_line_edit_label, 0, 0)
        layout.addWidget(self.youtube_url_line_edit, 0, 1, 1, 2)
        layout.addWidget(self.download_folder_line_edit_label, 1, 0)
        layout.addWidget(self.download_folder_line_edit, 1, 1, 1, 2)
        layout.addWidget(self.select_download_folder_push_button, 2, 1)

        self.setLayout(layout)
    
    def select_download_folder(self):
        
        try:
            
            self.download_folder_url = QFileDialog.getExistingDirectoryUrl(self, caption = "Select Folder")
            
            if self.download_folder_url.isValid():
                url_text: str = self.download_folder_url.toLocalFile()
                self.download_folder_line_edit.setText(url_text)
            else:
                self.download_folder_line_edit_error_text: str = "ERROR: Invalid folder URL"
            
            if self.download_folder_line_edit_error_text:
                
                self.download_folder_line_edit.clear()
                self.download_folder_line_edit.setPlaceholderText(self.download_folder_line_edit_error_text)
                self.download_folder_line_edit.setStyleSheet(self.download_folder_line_edit.error_style_sheet)
                self.download_folder_line_edit.textEdited.connect(self.on_edit_download_folder_line_edit)
        
        except KeyboardInterrupt:

            self.download_folder_line_edit.clear()
            self.download_folder_line_edit.reset()
            self.download_folder_line_edit_error_text = None

    def on_edit_download_folder_line_edit(self):
        
        if self.download_folder_line_edit_started_typing:
            self.download_folder_line_edit.disconnect(self.on_edit_download_folder_line_edit)
        
        self.download_folder_line_edit.reset()
        self.download_folder_line_edit_error_text = None
    
