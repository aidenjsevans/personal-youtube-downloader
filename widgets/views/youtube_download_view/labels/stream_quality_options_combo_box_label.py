from PySide6.QtWidgets import QLabel

class StreamQualityOptionsComboBoxLabel(QLabel):

    def __init__(self, parent = None):
        
        super().__init__(parent = parent)
        
        self.setText("Stream quality")