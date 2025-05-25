from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QPushButton, QLabel
from PyQt5.QtCore import Qt, QDate
from services.task_service import TaskService
from gui.dialogs.task_dialog import TaskDialog
from datetime import datetime

class TaskListWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.task_service = TaskService()
        self.current_category_id = None
        self.current_date = None
        self.setup_ui()
        self.load_tasks()

    def setup_ui(self):
        # Main layout
        layout = QVBoxLayout(self)
        
        # Create "Add Task" button
        add_button = QPushButton("Add Task")
        add_button.clicked.connect(self.show_add_task_dialog)
        layout.addWidget(add_button)
        
        # Create scroll area for tasks
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        # Container widget for tasks
        self.task_container = QWidget()
        self.task_layout = QVBoxLayout(self.task_container)
        
        scroll.setWidget(self.task_container)
        layout.addWidget(scroll)

    def load_tasks(self):
        # Clear existing tasks
        for i in reversed(range(self.task_layout.count())):
            widget = self.task_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()
        
        # Get tasks based on current filters
        tasks = self.get_filtered_tasks()
        
        # Add tasks to layout
        for task in tasks:
            task_widget = self.create_task_widget(task)
            self.task_layout.addWidget(task_widget)
        
        # Add stretch at the end
        self.task_layout.addStretch()

    def get_filtered_tasks(self):
        """Get tasks based on current filters"""
        if self.current_category_id and self.current_date:
            # Filter by both category and date
            return self.task_service.get_tasks_by_category_and_date(
                self.current_category_id,
                self.current_date
            )
        elif self.current_category_id:
            # Filter by category only
            return self.task_service.get_tasks_by_category(self.current_category_id)
        elif self.current_date:
            # Filter by date only
            return self.task_service.get_tasks_by_date(self.current_date)
        else:
            # No filters
            return self.task_service.get_all_tasks()

    def filter_by_category(self, category_id):
        """Filter tasks by category ID"""
        self.current_category_id = category_id
        self.load_tasks()

    def filter_by_date(self, date):
        """Filter tasks by date"""
        if isinstance(date, QDate):
            # Convert QDate to Python datetime
            self.current_date = datetime(date.year(), date.month(), date.day())
        else:
            self.current_date = date
        self.load_tasks()

    def show_add_task_dialog(self):
        """Show dialog to add a new task"""
        dialog = TaskDialog(self)
        if dialog.exec_():
            self.load_tasks()

    def create_task_widget(self, task):
        """Create a widget for displaying a task"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # Task title
        title_label = QLabel(task.title)
        title_label.setStyleSheet("font-weight: bold;")
        layout.addWidget(title_label)
        
        # Task description (if exists)
        if task.description:
            desc_label = QLabel(task.description)
            desc_label.setWordWrap(True)
            layout.addWidget(desc_label)
        
        # Due date (if exists)
        if task.due_date:
            due_date_label = QLabel(f"Due: {task.due_date.strftime('%Y-%m-%d %H:%M')}")
            layout.addWidget(due_date_label)
        
        # Edit button
        edit_button = QPushButton("Edit")
        edit_button.clicked.connect(lambda: self.show_edit_task_dialog(task))
        layout.addWidget(edit_button)
        
        # Add some styling
        widget.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
                border-radius: 5px;
                padding: 5px;
                margin: 2px;
            }
            QPushButton {
                background-color: #e0e0e0;
                border: none;
                padding: 5px;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #d0d0d0;
            }
        """)
        
        return widget

    def show_edit_task_dialog(self, task):
        """Show dialog to edit an existing task"""
        dialog = TaskDialog(self, task)
        if dialog.exec_():
            self.load_tasks()

    def clear_filters(self):
        """Clear all filters"""
        self.current_category_id = None
        self.current_date = None
        self.load_tasks()