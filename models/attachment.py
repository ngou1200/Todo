from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database.base import Base
from datetime import datetime

class Attachment(Base):
    __tablename__ = 'attachments'
    
    id = Column(Integer, primary_key=True)
    filename = Column(String(255), nullable=False)
    file_path = Column(String(1000), nullable=False)
    file_type = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Foreign keys
    task_id = Column(Integer, ForeignKey('tasks.id'))
    
    # Relationships
    task = relationship("Task", back_populates="attachments")