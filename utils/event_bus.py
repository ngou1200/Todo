from PyQt5.QtCore import QObject, pyqtSignal

class EventBus(QObject):
    _instance = None
    
    # Define signals
    task_created = pyqtSignal(object)
    task_updated = pyqtSignal(object)
    task_deleted = pyqtSignal(int)
    category_created = pyqtSignal(object)
    category_updated = pyqtSignal(object)
    category_deleted = pyqtSignal(int)
    settings_changed = pyqtSignal()
    reminder_triggered = pyqtSignal(object)
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = EventBus()
        return cls._instance
    
    def __init__(self):
        super().__init__()