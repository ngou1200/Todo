import os
import shutil
import sqlite3
from datetime import datetime
from utils.config_manager import ConfigManager
from utils.logger import Logger

class BackupManager:
    _instance = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = BackupManager()
        return cls._instance
    
    def __init__(self):
        self.config = ConfigManager.get_instance()
        self.logger = Logger.get_instance()
    
    def create_backup(self):
        try:
            # Create backup directory if it doesn't exist
            backup_dir = self.config.get("app.backup_location", "backups/")
            os.makedirs(backup_dir, exist_ok=True)
            
            # Generate backup filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            db_path = self.config.get("database.path")
            backup_path = os.path.join(
                backup_dir, 
                f"todo_backup_{timestamp}.db"
            )
            
            # Create backup
            shutil.copy2(db_path, backup_path)
            
            # Clean old backups
            self.cleanup_old_backups()
            
            self.logger.info(f"Backup created successfully: {backup_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"Backup creation failed: {str(e)}")
            return False
    
    def restore_backup(self, backup_path):
        try:
            db_path = self.config.get("database.path")
            
            # Create backup of current database
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            current_backup = f"todo_pre_restore_{timestamp}.db"
            shutil.copy2(db_path, current_backup)
            
            # Restore selected backup
            shutil.copy2(backup_path, db_path)
            
            self.logger.info(f"Backup restored successfully from: {backup_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"Backup restoration failed: {str(e)}")
            return False
    
    def cleanup_old_backups(self):
        try:
            backup_dir = self.config.get("app.backup_location", "backups/")
            max_backups = 10  # Keep last 10 backups
            
            # Get list of backup files
            backups = [f for f in os.listdir(backup_dir) 
                      if f.startswith("todo_backup_")]
            backups.sort(reverse=True)
            
            # Remove old backups
            for backup in backups[max_backups:]:
                os.remove(os.path.join(backup_dir, backup))
                
        except Exception as e:
            self.logger.error(f"Backup cleanup failed: {str(e)}")