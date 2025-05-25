from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                            QLineEdit, QTextEdit, QDateTimeEdit, QComboBox,
                            QPushButton)
from PyQt5.QtCore import Qt, QDateTime
from services.task_service import TaskService
from services.category_service import CategoryService

class TaskDialog(QDialog):
    def __init__(self, parent=None, task=None):
        super().__init__(parent)
        self.task = task
        self.task_service = TaskService()
        self.category_service = CategoryService()
        self.setup_ui()
        if task:
            self.load_task_data()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # Title
        title_layout = QHBoxLayout()
        title_label = QLabel("Title:")
        self.title_edit = QLineEdit()
        title_layout.addWidget(title_label)
        title_layout.addWidget(self.title_edit)
        layout.addLayout(title_layout)
        
        # Description
        desc_label = QLabel("Description:")
        self.desc_edit = QTextEdit()
        layout.addWidget(desc_label)
        layout.addWidget(self.desc_edit)
        
        # Due Date
        due_date_layout = QHBoxLayout()
        due_date_label = QLabel("Due Date:")
        self.due_date_edit = QDateTimeEdit(QDateTime.currentDateTime())
        due_date_layout.addWidget(due_date_label)
        due_date_layout.addWidget(self.due_date_edit)
        layout.addLayout(due_date_layout)
        
        # Category
        category_layout = QHBoxLayout()
        category_label = QLabel("Category:")
        self.category_combo = QComboBox()
        self.load_categories()
        category_layout.addWidget(category_label)
        category_layout.addWidget(self.category_combo)
        layout.addLayout(category_layout)
        
        # Buttons
        button_layout = QHBoxLayout()
        save_button = QPushButton("Save")
        cancel_button = QPushButton("Cancel")
        save_button.clicked.connect(self.save_task)
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)

    def load_categories(self):
        categories = self.category_service.get_all_categories()
        self.category_combo.clear()
        self.category_combo.addItem("No Category", None)
        for category in categories:
            self.category_combo.addItem(category.name, category.id)

    def load_task_data(self):
        if self.task:
            self.title_edit.setText(self.task.title)
            self.desc_edit.setText(self.task.description)
            if self.task.due_date:
                self.due_date_edit.setDateTime(self.task.due_date)
            if self.task.category_id:
                index = self.category_combo.findData(self.task.category_id)
                if index >= 0:
                    self.category_combo.setCurrentIndex(index)

    def save_task(self):
        title = self.title_edit.text()
        description = self.desc_edit.toPlainText()
        due_date = self.due_date_edit.dateTime().toPyDateTime()
        category_id = self.category_combo.currentData()
        
        if self.task:
            self.task_service.update_task(
                self.task.id,
                title=title,
                description=description,
                due_date=due_date,
                category_id=category_id
            )
        else:
            self.task_service.create_task(
                title=title,
                description=description,
                due_date=due_date,
                category_id=category_id
            )
        
        self.accept()