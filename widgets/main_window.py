from PySide6.QtWidgets import (
    QMainWindow, QStackedWidget, QWidget,
    QGridLayout)

class MainWindow(QMainWindow):

    def __init__(
            self,
            x_position_px: int,
            y_position_px: int,
            youtube_download_view: QWidget,
            width_px: int | None = None,
            height_px: int | None = None):
        
        super().__init__()

        if not width_px or not height_px:
            self.move(x_position_px, y_position_px)
        else:
            self.setGeometry(x_position_px, y_position_px, width_px, height_px)
            
        self.setWindowTitle("YouTubeDownloader")

        self.view_stack = QStackedWidget()

        self.view_stack.addWidget(youtube_download_view)

        container = QWidget()
        layout = QGridLayout()

        layout.addWidget(self.view_stack, 0, 0)

        container.setLayout(layout)
        self.setCentralWidget(container)


    
