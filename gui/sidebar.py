from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import pyqtSignal
from services.category_service import CategoryService

class Sidebar(QWidget):
    category_selected = pyqtSignal(int)  # Signal for category selection

    def __init__(self):
        super().__init__()
        self.category_service = CategoryService()
        self.setup_ui()
        self.load_categories()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # Add header
        header = QLabel("Categories")
        layout.addWidget(header)
        
        # Add "All Tasks" button
        all_tasks_btn = QPushButton("All Tasks")
        all_tasks_btn.clicked.connect(lambda: self.category_selected.emit(None))
        layout.addWidget(all_tasks_btn)
        
        # Container for category buttons
        self.category_layout = QVBoxLayout()
        layout.addLayout(self.category_layout)
        
        # Add "Add Category" button
        add_category_btn = QPushButton("+ Add Category")
        add_category_btn.clicked.connect(self.show_add_category_dialog)
        layout.addWidget(add_category_btn)
        
        # Add stretch to push everything up
        layout.addStretch()

    def load_categories(self):
        # Clear existing category buttons
        for i in reversed(range(self.category_layout.count())):
            self.category_layout.itemAt(i).widget().deleteLater()
        
        # Add category buttons
        categories = self.category_service.get_all_categories()
        for category in categories:
            btn = QPushButton(category.name)
            btn.clicked.connect(lambda c=category.id: self.category_selected.emit(c))
            self.category_layout.addWidget(btn)

    def show_add_category_dialog(self):
        from gui.dialogs.category_dialog import CategoryDialog
        dialog = CategoryDialog(self)
        if dialog.exec_():
            self.load_categories()