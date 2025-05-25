from database.db_manager import DatabaseManager
from models.category import Category

class CategoryService:
    def __init__(self):
        self.db = DatabaseManager.get_instance()

    def create_category(self, name, description=None):
        session = self.db.get_session()
        try:
            category = Category(name=name, description=description)
            session.add(category)
            session.commit()
            return category
        finally:
            session.close()

    def update_category(self, category_id, name, description=None):
        session = self.db.get_session()
        try:
            category = session.query(Category).get(category_id)
            if category:
                category.name = name
                category.description = description
                session.commit()
                return category
            return None
        finally:
            session.close()

    def delete_category(self, category_id):
        session = self.db.get_session()
        try:
            category = session.query(Category).get(category_id)
            if category:
                session.delete(category)
                session.commit()
                return True
            return False
        finally:
            session.close()

    def get_category(self, category_id):
        session = self.db.get_session()
        try:
            return session.query(Category).get(category_id)
        finally:
            session.close()

    def get_all_categories(self):
        session = self.db.get_session()
        try:
            return session.query(Category).all()
        finally:
            session.close()