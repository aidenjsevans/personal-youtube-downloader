from PySide6.QtWidgets import (
    QWidget, QGridLayout)

class LoadingView(QWidget):

    def __init__(
            self,
            circle_loading_widget: QWidget):

        super().__init__()

        #-----Circle loading widget-----
        self.circle_loading_widget = circle_loading_widget
        #-------------------------------

        #-----Layout-----
        self.view_layout = QGridLayout()

        self.view_layout.addWidget(self.circle_loading_widget)

        self.setLayout(self.view_layout)
        #----------------



        