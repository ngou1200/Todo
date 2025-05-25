from database.db_manager import DatabaseManager
from models.task import Task
from datetime import datetime

class TaskService:
    def __init__(self):
        self.db_manager = DatabaseManager.get_instance()

    def create_task(self, title, description=None, due_date=None, category_id=None):
        session = self.db_manager.get_session()
        try:
            task = Task(
                title=title,
                description=description,
                due_date=due_date,
                category_id=category_id
            )
            session.add(task)
            session.commit()
            return task
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def get_all_tasks(self):
        session = self.db_manager.get_session()
        try:
            return session.query(Task).all()
        finally:
            session.close()

    def get_task_by_id(self, task_id):
        session = self.db_manager.get_session()
        try:
            return session.query(Task).filter(Task.id == task_id).first()
        finally:
            session.close()

    def get_tasks_by_category(self, category_id):
        session = self.db_manager.get_session()
        try:
            return session.query(Task).filter(Task.category_id == category_id).all()
        finally:
            session.close()

    def update_task(self, task_id, **kwargs):
        session = self.db_manager.get_session()
        try:
            task = session.query(Task).filter(Task.id == task_id).first()
            if task:
                for key, value in kwargs.items():
                    if hasattr(task, key):
                        setattr(task, key, value)
                task.updated_at = datetime.utcnow()
                session.commit()
                return task
            return None
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def delete_task(self, task_id):
        session = self.db_manager.get_session()
        try:
            task = session.query(Task).filter(Task.id == task_id).first()
            if task:
                session.delete(task)
                session.commit()
                return True
            return False
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def complete_task(self, task_id):
        return self.update_task(task_id, completed=True)

    def uncomplete_task(self, task_id):
        return self.update_task(task_id, completed=False)

    def get_tasks_by_date_range(self, start_date, end_date):
        session = self.db_manager.get_session()
        try:
            return session.query(Task).filter(
                Task.due_date >= start_date,
                Task.due_date <= end_date
            ).all()
        finally:
            session.close()

    def get_overdue_tasks(self):
        session = self.db_manager.get_session()
        try:
            return session.query(Task).filter(
                Task.due_date < datetime.utcnow(),
                Task.completed == False
            ).all()
        finally:
            session.close()

    def get_completed_tasks(self):
        session = self.db_manager.get_session()
        try:
            return session.query(Task).filter(Task.completed == True).all()
        finally:
            session.close()

    def get_incomplete_tasks(self):
        session = self.db_manager.get_session()
        try:
            return session.query(Task).filter(Task.completed == False).all()
        finally:
            session.close()