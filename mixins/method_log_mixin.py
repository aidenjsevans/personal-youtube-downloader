import inspect

from datetime import datetime

class MethodLogMixin:

    def log_call(obj, message: str = None):
        
        frame = inspect.currentframe().f_back
        class_name: str = obj.__class__.__name__
        method_name: str = frame.f_code.co_name
        
        print(f"({datetime.now()}) {class_name}.{method_name}: {message}")