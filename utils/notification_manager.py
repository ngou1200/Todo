from PyQt5.QtCore import QObject, QTimer
from datetime import datetime, timedelta
from utils.config_manager import ConfigManager
from utils.logger import Logger
from services.reminder_service import ReminderService

class NotificationManager(QObject):
    _instance = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = NotificationManager()
        return cls._instance
    
    def __init__(self):
        super().__init__()
        self.config = ConfigManager.get_instance()
        self.logger = Logger.get_instance()
        self.reminder_service = ReminderService()
        self.check_timer = QTimer()
        self.check_timer.timeout.connect(self.check_reminders)
        self.check_timer.start(60000)  # Check every minute
    
    def check_reminders(self):
        if not self.config.get("notifications.enabled"):
            return
            
        current_time = datetime.utcnow()
        advance_notice = self.config.get("notifications.advance_notice", 15)
        check_time = current_time + timedelta(minutes=advance_notice)
        
        active_reminders = self.reminder_service.get_active_reminders()
        
        for reminder in active_reminders:
            if reminder.reminder_time <= check_time:
                self.show_notification(reminder)
    
    def show_notification(self, reminder):
        from PyQt5.QtWidgets import QSystemTrayIcon, QMessageBox
        
        if not QSystemTrayIcon.isSystemTrayAvailable():
            return
            
        title = "Task Reminder"
        message = reminder.message or f"Task: {reminder.task.title}"
        
        tray = QSystemTrayIcon()
        tray.show()
        tray.showMessage(title, message, QSystemTrayIcon.Information, 10000)
        
        if self.config.get("notifications.sound"):
            # Play notification sound
            pass