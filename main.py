import sys
from PyQt5.QtWidgets import QApplication
from gui.main_window import MainWindow
from utils.config_manager import ConfigManager
from utils.logger import Logger
from database.db_manager import DatabaseManager

def main():
    # Initialize logger
    logger = Logger.get_instance()
    logger.info("Starting ToDo Application")

    # Load configuration
    config = ConfigManager.get_instance()
    config.load_config()

    # Initialize database
    db = DatabaseManager.get_instance()
    db.initialize()

    # Start GUI application
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()