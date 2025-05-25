from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from utils.config_manager import ConfigManager
from utils.logger import Logger
from database.base import Base

class DatabaseManager:
    _instance = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = DatabaseManager()
        return cls._instance

    def __init__(self):
        self.logger = Logger.get_instance()
        self.config = ConfigManager.get_instance()
        self.engine = None
        self.session_factory = None
        
    def initialize(self):
        db_path = self.config.get("database.path")
        self.engine = create_engine(f'sqlite:///{db_path}')
        self.session_factory = scoped_session(sessionmaker(bind=self.engine))
        
        # Import all models to ensure they are registered
        import models
        
        # Create all tables
        Base.metadata.create_all(self.engine)
        self.logger.info("Database initialized successfully")
    
    def get_session(self):
        return self.session_factory()
    
    def close_session(self, session):
        if session:
            session.close()