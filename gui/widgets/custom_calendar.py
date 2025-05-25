from PyQt5.QtWidgets import QCalendarWidget
from PyQt5.QtCore import pyqtSignal
from services.task_service import TaskService

class CustomCalendar(QCalendarWidget):
    date_selected = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        self.task_service = TaskService()
        self.setup_ui()
        
    def setup_ui(self):
        self.clicked.connect(self.on_date_clicked)
        self.setGridVisible(True)
        self.update_task_dates()
        
    def update_task_dates(self):
        # Here you would implement logic to highlight dates with tasks
        pass
        
    def on_date_clicked(self, date):
        self.date_selected.emit(date)