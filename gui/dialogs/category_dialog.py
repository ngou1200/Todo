from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, 
                           QLabel, QLineEdit, QPushButton, QTextEdit)
from services.category_service import CategoryService

class CategoryDialog(QDialog):
    def __init__(self, parent=None, category=None):
        super().__init__(parent)
        self.category_service = CategoryService()
        self.category = category
        self.setup_ui()
        
        if category:
            self.setWindowTitle("Edit Category")
            self.name_input.setText(category.name)
            if category.description:
                self.description_input.setText(category.description)
        else:
            self.setWindowTitle("Add Category")

    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # Name input
        name_layout = QHBoxLayout()
        name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        name_layout.addWidget(name_label)
        name_layout.addWidget(self.name_input)
        layout.addLayout(name_layout)
        
        # Description input
        description_layout = QVBoxLayout()
        description_label = QLabel("Description:")
        self.description_input = QTextEdit()
        self.description_input.setPlaceholderText("Enter category description (optional)")
        description_layout.addWidget(description_label)
        description_layout.addWidget(self.description_input)
        layout.addLayout(description_layout)
        
        # Buttons
        button_layout = QHBoxLayout()
        save_button = QPushButton("Save")
        cancel_button = QPushButton("Cancel")
        
        save_button.clicked.connect(self.save_category)
        cancel_button.clicked.connect(self.reject)
        
        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)
        
        # Set dialog size
        self.setMinimumWidth(300)
        
    def save_category(self):
        name = self.name_input.text().strip()
        description = self.description_input.toPlainText().strip()
        
        if not name:
            return
            
        if self.category:
            # Update existing category
            self.category_service.update_category(
                self.category.id,
                name,
                description
            )
        else:
            # Create new category
            self.category_service.create_category(name, description)
            
        self.accept()