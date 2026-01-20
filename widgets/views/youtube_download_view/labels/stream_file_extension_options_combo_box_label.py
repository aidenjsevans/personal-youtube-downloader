from PySide6.QtWidgets import QLabel

class StreamFileExtensionOptionsComboBoxLabel(QLabel):

    def __init__(self, parent = None):
        
        super().__init__(parent = parent)
        
        self.setText("File extension")