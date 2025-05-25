from database.db_manager import DatabaseManager
from models.tag import Tag
from utils.logger import Logger

class TagService:
    def __init__(self):
        self.db = DatabaseManager.get_instance()
        self.logger = Logger.get_instance()

    def create_tag(self, name, color="#000000"):
        session = self.db.get_session()
        try:
            tag = Tag(name=name, color=color)
            session.add(tag)
            session.commit()
            return tag
        except Exception as e:
            self.logger.error(f"Error creating tag: {str(e)}")
            session.rollback()
            raise
        finally:
            self.db.close_session(session)

    def get_tag(self, tag_id):
        session = self.db.get_session()
        try:
            return session.query(Tag).get(tag_id)
        finally:
            self.db.close_session(session)

    def get_all_tags(self):
        session = self.db.get_session()
        try:
            return session.query(Tag).all()
        finally:
            self.db.close_session(session)

    def update_tag(self, tag_id, name=None, color=None):
        session = self.db.get_session()
        try:
            tag = session.query(Tag).get(tag_id)
            if tag:
                if name:
                    tag.name = name
                if color:
                    tag.color = color
                session.commit()
            return tag
        except Exception as e:
            self.logger.error(f"Error updating tag: {str(e)}")
            session.rollback()
            raise
        finally:
            self.db.close_session(session)

    def delete_tag(self, tag_id):
        session = self.db.get_session()
        try:
            tag = session.query(Tag).get(tag_id)
            if tag:
                session.delete(tag)
                session.commit()
                return True
            return False
        except Exception as e:
            self.logger.error(f"Error deleting tag: {str(e)}")
            session.rollback()
            raise
        finally:
            self.db.close_session(session)