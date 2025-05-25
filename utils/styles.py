class Styles:
    LIGHT_THEME = """
        QMainWindow {
            background-color: #f0f0f0;
        }
        QWidget {
            color: #333333;
        }
        QPushButton {
            background-color: #2196F3;
            color: white;
            border: none;
            padding: 5px 15px;
            border-radius: 3px;
        }
        QPushButton:hover {
            background-color: #1976D2;
        }
        QPushButton:pressed {
            background-color: #0D47A1;
        }
        QLineEdit, QTextEdit {
            border: 1px solid #BDBDBD;
            border-radius: 3px;
            padding: 5px;
            background-color: white;
        }
        QLineEdit:focus, QTextEdit:focus {
            border: 2px solid #2196F3;
        }
        QLabel {
            color: #333333;
        }
        QComboBox {
            border: 1px solid #BDBDBD;
            border-radius: 3px;
            padding: 5px;
            background-color: white;
        }
        QCalendarWidget {
            background-color: white;
        }
    """
    
    DARK_THEME = """
        QMainWindow {
            background-color: #2C2C2C;
        }
        QWidget {
            color: #FFFFFF;
        }
        QPushButton {
            background-color: #0D47A1;
            color: white;
            border: none;
            padding: 5px 15px;
            border-radius: 3px;
        }
        QPushButton:hover {
            background-color: #1565C0;
        }
        QPushButton:pressed {
            background-color: #1976D2;
        }
        QLineEdit, QTextEdit {
            border: 1px solid #555555;
            border-radius: 3px;
            padding: 5px;
            background-color: #3C3C3C;
            color: white;
        }
        QLineEdit:focus, QTextEdit:focus {
            border: 2px solid #1E88E5;
        }
        QLabel {
            color: #FFFFFF;
        }
        QComboBox {
            border: 1px solid #555555;
            border-radius: 3px;
            padding: 5px;
            background-color: #3C3C3C;
            color: white;
        }
        QCalendarWidget {
            background-color: #2C2C2C;
            color: white;
        }
    """
    
    @classmethod
    def get_theme(cls, theme_name):
        if theme_name.lower() == "dark":
            return cls.DARK_THEME
        return cls.LIGHT_THEME
    
    @classmethod
    def get_task_priority_color(cls, priority):
        if priority >= 8:
            return "#FF5252"  # High priority - Red
        elif priority >= 4:
            return "#FFA726"  # Medium priority - Orange
        return "#66BB6A"  # Low priority - Green
    
    @classmethod
    def get_task_card_style(cls, is_completed, priority, theme="light"):
        base_color = "#FFFFFF" if theme == "light" else "#3C3C3C"
        border_color = cls.get_task_priority_color(priority)
        text_color = "#333333" if theme == "light" else "#FFFFFF"
        
        if is_completed:
            base_color = "#E0E0E0" if theme == "light" else "#2C2C2C"
            
        return f"""
            QWidget {{
                background-color: {base_color};
                border: 2px solid {border_color};
                border-radius: 5px;
                padding: 10px;
                margin: 5px;
                color: {text_color};
            }}
        """