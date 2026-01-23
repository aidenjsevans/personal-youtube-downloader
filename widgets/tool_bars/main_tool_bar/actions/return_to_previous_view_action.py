from PySide6.QtGui import QAction, QIcon

from PySide6.QtCore import Signal

class ReturnToPreviousViewAction(QAction):

    return_to_previous_view_action_signal = Signal()

    def __init__(
            self,
            parent = None):

        super().__init__(parent = parent)

        self.setIcon(
            QIcon("icons/arrow-left.svg")
            )
        
        self.triggered.connect(self.on_trigger)
    
    def on_trigger(self):
        self.return_to_previous_view_action_signal.emit()

        


