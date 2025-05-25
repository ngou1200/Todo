import json
import os
from pathlib import Path

class ConfigManager:
    _instance = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = ConfigManager()
        return cls._instance
    
    def __init__(self):
        self.config_file = "config.json"
        self.config = {}
        self.load_config()
    
    def load_config(self):
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    self.config = json.load(f)
        except Exception as e:
            print(f"Error loading config: {str(e)}")
            self.config = self.get_default_config()
            self.save_config()
    
    def save_config(self):
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=4)
        except Exception as e:
            print(f"Error saving config: {str(e)}")
    
    def get(self, key, default=None):
        """Get a config value using dot notation (e.g., 'app.theme')"""
        try:
            value = self.config
            for k in key.split('.'):
                value = value[k]
            return value
        except (KeyError, TypeError):
            return default
    
    def set(self, key, value):
        """Set a config value using dot notation"""
        keys = key.split('.')
        current = self.config
        for k in keys[:-1]:
            current = current.setdefault(k, {})
        current[keys[-1]] = value
    
    def get_default_config(self):
        return {
            "database": {
                "type": "sqlite",
                "path": "todo.db"
            },
            "app": {
                "theme": "light",
                "language": "en",
                "backup_interval": 24,
                "backup_location": "backups/"
            },
            "notifications": {
                "enabled": True,
                "sound": True,
                "advance_notice": 15
            },
            "logging": {
                "level": "INFO",
                "file": "app.log"
            }
        }