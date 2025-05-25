from database.db_manager import DatabaseManager
from models.reminder import Reminder
from utils.logger import Logger
from datetime import datetime

class ReminderService:
    def __init__(self):
        self.db = DatabaseManager.get_instance()
        self.logger = Logger.get_instance()

    def create_reminder(self, task_id, reminder_time, message=None):
        session = self.db.get_session()
        try:
            reminder = Reminder(
                task_id=task_id,
                reminder_time=reminder_time,
                message=message
            )
            session.add(reminder)
            session.commit()
            return reminder
        except Exception as e:
            self.logger.error(f"Error creating reminder: {str(e)}")
            session.rollback()
            raise
        finally:
            self.db.close_session(session)

    def get_reminder(self, reminder_id):
        session = self.db.get_session()
        try:
            return session.query(Reminder).get(reminder_id)
        finally:
            self.db.close_session(session)

    def get_active_reminders(self):
        session = self.db.get_session()
        try:
            return session.query(Reminder).filter(
                Reminder.is_active == True,
                Reminder.reminder_time > datetime.utcnow()
            ).all()
        finally:
            self.db.close_session(session)

    def update_reminder(self, reminder_id, reminder_time=None, message=None, is_active=None):
        session = self.db.get_session()
        try:
            reminder = session.query(Reminder).get(reminder_id)
            if reminder:
                if reminder_time:
                    reminder.reminder_time = reminder_time
                if message is not None:
                    reminder.message = message
                if is_active is not None:
                    reminder.is_active = is_active
                session.commit()
            return reminder
        except Exception as e:
            self.logger.error(f"Error updating reminder: {str(e)}")
            session.rollback()
            raise
        finally:
            self.db.close_session(session)

    def delete_reminder(self, reminder_id):
        session = self.db.get_session()
        try:
            reminder = session.query(Reminder).get(reminder_id)
            if reminder:
                session.delete(reminder)
                session.commit()
                return True
            return False
        except Exception as e:
            self.logger.error(f"Error deleting reminder: {str(e)}")
            session.rollback()
            raise
        finally:
            self.db.close_session(session)