from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database.base import Base
from datetime import datetime

class Subtask(Base):
    __tablename__ = 'subtasks'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Foreign keys
    task_id = Column(Integer, ForeignKey('tasks.id'))
    
    # Relationships
    parent_task = relationship("Task", back_populates="subtasks")