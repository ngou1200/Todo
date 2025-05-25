from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from gui.sidebar import Sidebar
from gui.widgets.task_list_widget import TaskListWidget
from gui.widgets.custom_calendar import CustomCalendar
from gui.widgets.statistics_widget import StatisticsWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Todo App")
        self.setMinimumSize(1000, 600)
        
        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)
        
        # Create sidebar
        self.sidebar = Sidebar()
        main_layout.addWidget(self.sidebar)
        
        # Create central area
        central_widget = QWidget()
        central_layout = QVBoxLayout(central_widget)
        
        # Create and add task list
        self.task_list = TaskListWidget()
        central_layout.addWidget(self.task_list)
        
        # Create right panel
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        
        # Add calendar
        self.calendar = CustomCalendar()
        right_layout.addWidget(self.calendar)
        
        # Add statistics widget
        self.statistics = StatisticsWidget()
        right_layout.addWidget(self.statistics)
        
        # Add layouts to main layout
        main_layout.addWidget(central_widget)
        main_layout.addWidget(right_panel)
        
        # Set layout stretch
        main_layout.setStretch(0, 1)  # Sidebar
        main_layout.setStretch(1, 4)  # Central widget
        main_layout.setStretch(2, 2)  # Right panel
        
        self.setup_connections()

    def setup_connections(self):
        self.sidebar.category_selected.connect(self.task_list.filter_by_category)
        self.calendar.date_selected.connect(self.task_list.filter_by_date)