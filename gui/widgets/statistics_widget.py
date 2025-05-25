from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QProgressBar
from services.task_service import TaskService

class StatisticsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.task_service = TaskService()
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # Add title
        title = QLabel("Statistics")
        layout.addWidget(title)
        
        # Add completion rate
        self.completion_rate = QProgressBar()
        layout.addWidget(self.completion_rate)
        
        # Add task count labels
        self.total_tasks = QLabel()
        self.completed_tasks = QLabel()
        layout.addWidget(self.total_tasks)
        layout.addWidget(self.completed_tasks)
        
        self.update_statistics()
        
    def update_statistics(self):
        # Here you would implement logic to update statistics
        self.total_tasks.setText("Total Tasks: 0")
        self.completed_tasks.setText("Completed Tasks: 0")
        self.completion_rate.setValue(0)