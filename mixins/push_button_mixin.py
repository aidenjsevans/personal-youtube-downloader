from typing import Callable

class PushButtonMixin:

    def connect_method(self, method: Callable):
        self.clicked.connect(method)