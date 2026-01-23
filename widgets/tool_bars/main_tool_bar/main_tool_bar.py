from PySide6.QtWidgets import QToolBar

from PySide6.QtGui import QAction

class MainToolBar(QToolBar):

    def __init__(
            self,
            return_to_previous_view_action: QAction,
            parent = None):

        super().__init__(parent = parent)

        #-----Return to previous view action-----
        self.return_to_previous_view_action = return_to_previous_view_action
        self.addAction(self.return_to_previous_view_action)
        self.return_to_previous_view_action.setParent(self)
        #----------------------------------------
        

        